from intimai import Certificado, Dia, Horario
from intimai.api.api import API
from intimai.servicos.atualizar.autenticador.autenticador_ativar_captura_intimacao_atualizacao import AutenticadorAtivarCapturaIntimacaoAtualizacao
from intimai.servicos.atualizar.autenticador.autenticador_oab_atualizacao import AutenticadorOabAtualizacao
from intimai.servicos.atualizar.escuta.escuta_atualizacao import EscutaAtualizacao
from intimai.servicos.buscar.acao.acao_busca import AcaoBusca
from intimai.servicos.cadastrar.notificacao.notificacao_email_cadastro import NotificacaoEmailCadastro
from intimai.servicos.solicitar_cadastro.certificado.certificado_solicitacao_cadastro import CertificadoSolicitacaoCadastro
from tests.apoio import Caso


class TestAPI(Caso):
    def test_envia_token_na_query_e_headers_da_collection(self):
        self.criar().servicos.cadastrar(NotificacaoEmailCadastro('a@b.com'))

        requisicao = self.requisicao()
        self.assertEqual(requisicao.method, 'POST')
        self.assertEqual(self.caminho(), '/api/v3/notificacao/email/cadastrar')
        self.assertEqual(self.query(), {'api_token': 'token-teste', 'page': '1'})
        self.assertEqual(requisicao.headers['Accept'], 'application/json')
        self.assertEqual(requisicao.headers['Content-Type'], 'application/x-www-form-urlencoded')
        self.assertEqual(requisicao.headers['User-Agent'], API.USER_AGENT)
        self.assertNotIn('X-Codigo-2FA', requisicao.headers)
        self.assertNotIn('Authorization', requisicao.headers)
        self.assertEqual(self.corpo(), [('email', 'a@b.com')])

    def test_corpo_de_formulario_usa_colchetes_para_listas_e_dicionarios(self):
        intimai = self.criar([(200, {}, {})] * 3)

        intimai.servicos.atualizar(AutenticadorAtivarCapturaIntimacaoAtualizacao(5, ['aba'], [Dia.SEGUNDA_FEIRA, Dia.SEXTA_FEIRA], [Horario.DEZ_HORAS], True))
        intimai.servicos.atualizar(EscutaAtualizacao(7, [Dia.SEGUNDA_FEIRA], [Horario.DEZ_HORAS, Horario.DEZOITO_HORAS]))
        intimai.servicos.atualizar(AutenticadorOabAtualizacao(5, {'numero': '123', 'uf': 'RJ'}))

        self.assertEqual(self.caminho(0), '/api/v3/autenticador/5/ativar-captura-intimacao')
        self.assertEqual(self.corpo(0), [
            ('abas[0]', 'aba'),
            ('dias_de_captura[0]', '1'),
            ('dias_de_captura[1]', '5'),
            ('horarios_de_captura[0]', '10:00'),
            ('capturar_procuradorias', '1'),
        ])
        self.assertEqual(self.caminho(1), '/api/v3/escuta-processual/7/atualizar')
        self.assertEqual(self.corpo(1), [
            ('dias_de_captura[0]', '1'),
            ('horarios_de_captura[0]', '10:00'),
            ('horarios_de_captura[1]', '18:00'),
        ])
        self.assertEqual(self.corpo(2), [('oab_numero', '123'), ('oab_uf', 'RJ')])

    def test_codigo_2fa_vai_no_header_e_nunca_na_query(self):
        self.criar(opcoes={'codigo_2fa': '482913'}).servicos.buscar(AcaoBusca())

        self.assertEqual(self.requisicao().headers['X-Codigo-2FA'], '482913')
        self.assertNotIn('codigo_2fa', self.query())

    def test_codigo_2fa_por_funcao_e_gerado_a_cada_request(self):
        codigos = ['111111', '222222']
        intimai = self.criar([(200, {}, {})] * 2, {'codigo_2fa': lambda: codigos.pop(0)})

        intimai.servicos.buscar(AcaoBusca())
        intimai.servicos.buscar(AcaoBusca())

        self.assertEqual(self.requisicao(0).headers['X-Codigo-2FA'], '111111')
        self.assertEqual(self.requisicao(1).headers['X-Codigo-2FA'], '222222')

    def test_definir_codigo_2fa_troca_ou_remove_o_codigo(self):
        intimai = self.criar([(200, {}, {})] * 2)

        intimai.definir_codigo_2fa('654321')
        intimai.servicos.buscar(AcaoBusca())
        intimai.definir_codigo_2fa(None)
        intimai.servicos.buscar(AcaoBusca())

        self.assertEqual(self.requisicao(0).headers['X-Codigo-2FA'], '654321')
        self.assertNotIn('X-Codigo-2FA', self.requisicao(1).headers)

    def test_codigo_2fa_vazio_nao_envia_header(self):
        self.criar(opcoes={'codigo_2fa': ''}).servicos.buscar(AcaoBusca())

        self.assertNotIn('X-Codigo-2FA', self.requisicao().headers)

    def test_headers_e_params_das_opcoes_somam_aos_padrao_sem_vazar_entre_requests(self):
        headers = {'X-Rastreio': 'abc'}
        intimai = self.criar([(200, {}, {})] * 2, {'headers': headers, 'params': {'extra': '1'}})

        intimai.definir_codigo_2fa('111111')
        intimai.servicos.buscar(AcaoBusca())
        intimai.servicos.buscar(AcaoBusca())

        self.assertEqual(self.requisicao().headers['X-Rastreio'], 'abc')
        self.assertEqual(self.requisicao().headers['Accept'], 'application/json')
        self.assertEqual(self.query(), {'api_token': 'token-teste', 'page': '1', 'extra': '1'})
        self.assertEqual(headers, {'X-Rastreio': 'abc'})

    def test_filtros_vao_na_query_direto_ou_dentro_de_filtros(self):
        intimai = self.criar([(200, {}, {})] * 2)

        intimai.servicos.buscar(AcaoBusca(), 3, {'filtros': {'status': '13,14', 'per_page': 50}})
        intimai.servicos.buscar(AcaoBusca(), 1, {'status': '1,2'})

        self.assertEqual(self.query(0), {'api_token': 'token-teste', 'page': '3', 'status': '13,14', 'per_page': '50'})
        self.assertEqual(self.query(1), {'api_token': 'token-teste', 'page': '1', 'status': '1,2'})

    def test_multipart_envia_o_arquivo_com_nome(self):
        caminho = self.arquivo_temporario('pfx')

        self.criar().servicos.solicitar_cadastro(CertificadoSolicitacaoCadastro(Certificado(caminho, 'senha')))

        requisicao = self.requisicao()
        self.assertEqual(self.caminho(), '/api/v3/certificado/solicitar-cadastro')
        self.assertTrue(requisicao.headers['Content-Type'].startswith('multipart/form-data; boundary='))
        self.assertEqual(requisicao.headers['Accept'], 'application/json')
        self.assertEqual(self.query(), {'api_token': 'token-teste', 'page': '1'})
        self.assertIn(b'name="arquivo"; filename="arquivo.pdf"', requisicao.body)
        self.assertEqual(self.campos(), {'arquivo': 'pfx', 'senha': 'senha', 'senha_confirmation': 'senha'})

    def test_arquivo_inexistente_falha_antes_de_chamar_a_api(self):
        intimai = self.criar()

        with self.assertRaisesRegex(Exception, 'O caminho do arquivo informado é inválido!'):
            intimai.servicos.solicitar_cadastro(CertificadoSolicitacaoCadastro(Certificado('/nao/existe.pfx', 'senha')))

        self.assertEqual(self.requisicoes, [])

    def test_resposta_sem_corpo_devolve_dicionario_vazio(self):
        self.assertEqual(self.criar([(204, None, {})]).servicos.buscar(AcaoBusca()), {})
