from intimai import Documento, ParteVinculada, Peticao, Polo, TipoDeclaracao, TipoSolicitacao
from intimai.servicos.atualizar.autenticador.autenticador_alterar_para_regular_atualizacao import AutenticadorAlterarParaRegularAtualizacao
from intimai.servicos.atualizar.autenticador.autenticador_regular_atualizacao import AutenticadorRegularAtualizacao
from intimai.servicos.cadastrar.autenticador.autenticador_certificado_cadastro import AutenticadorCertificadoCadastro
from intimai.servicos.cadastrar.autenticador.autenticador_regular_cadastro import AutenticadorRegularCadastro
from intimai.servicos.solicitar.consulta.consulta_solicitacao import ConsultaSolicitacao
from intimai.servicos.solicitar.consulta_pre_analise.consulta_pre_analise_solicitacao import ConsultaPreAnaliseSolicitacao
from intimai.servicos.solicitar.protocolo.pje.protocolo_pje_solicitacao import ProtocoloPjeSolicitacao
from intimai.servicos.solicitar.protocolo.tjrj.protocolo_tjrj_segundo_passo_solicitacao import ProtocoloTjrjSegundoPassoSolicitacao
from intimai.servicos.solicitar.protocolo_habilitacao.pje.protocolo_habilitacao_pje_segundo_passo_solicitacao import ProtocoloHabilitacaoPjeSegundoPassoSolicitacao
from tests.apoio import Caso

OAB = {'numero': '12345', 'letra': 'A', 'uf': 'RJ'}


class TestRequestsAtualizadas(Caso):
    def test_consulta_e_pre_consulta_nao_enviam_token_e_mandam_a_oab_como_a_api_espera(self):
        intimai = self.criar([(200, {}, {})] * 3)
        esperado = [
            ('autenticacao_id', '5'),
            ('numero_processo', '0000001-00.2026.8.19.0001'),
            ('nome_parte', ''),
            ('nome_representante', ''),
            ('oab[numero]', '12345'),
            ('oab[letra]', 'A'),
            ('oab[uf]', 'RJ'),
            ('numero_documento_parte', ''),
        ]

        intimai.servicos.solicitar(ConsultaSolicitacao(5, '0000001-00.2026.8.19.0001', oab=OAB))
        intimai.servicos.solicitar(ConsultaPreAnaliseSolicitacao(5, '0000001-00.2026.8.19.0001', oab=OAB))
        intimai.servicos.solicitar(ConsultaSolicitacao(5, '0000001-00.2026.8.19.0001'))

        self.assertEqual(self.caminho(0), '/api/v3/consulta-processual/solicitar')
        self.assertEqual(self.corpo(0), esperado)
        self.assertEqual(self.caminho(1), '/api/v3/pre-consulta-processual/solicitar')
        self.assertEqual(self.corpo(1), esperado)
        self.assertEqual([chave for chave, _ in self.corpo(2)], ['autenticacao_id', 'numero_processo', 'nome_parte', 'nome_representante', 'numero_documento_parte'])

    def test_cadastro_regular_continua_igual_sem_os_campos_novos(self):
        self.criar().servicos.cadastrar(AutenticadorRegularCadastro(3, OAB, 'usuario', 'senha'))

        self.assertEqual(self.corpo(), [
            ('tribunal_id', '3'),
            ('oab_numero', '12345'),
            ('oab_uf', 'RJ'),
            ('usuario', 'usuario'),
            ('senha', 'senha'),
            ('oab_letra', 'A'),
        ])

    def test_cadastro_regular_com_varios_tribunais_certificado_perfil_e_secret(self):
        self.criar().servicos.cadastrar(AutenticadorRegularCadastro(
            [3, 4], OAB, 'usuario', 'senha',
            id_certificado=8, usuario_sigla='ADV', usuario_descricao='Escritório', secret='JBSWY3DPEHPK3PXP',
        ))

        self.assertEqual(self.caminho(), '/api/v3/autenticador/regular/cadastrar')
        self.assertEqual(dict(self.corpo()), {
            'tribunal_id[0]': '3',
            'tribunal_id[1]': '4',
            'oab_numero': '12345',
            'oab_uf': 'RJ',
            'usuario': 'usuario',
            'senha': 'senha',
            'oab_letra': 'A',
            'certificado_id': '8',
            'usuario_sigla': 'ADV',
            'usuario_descricao': 'Escritório',
            'secret': 'JBSWY3DPEHPK3PXP',
        })

    def test_cadastro_por_certificado_com_varios_tribunais_e_secret(self):
        self.criar().servicos.cadastrar(AutenticadorCertificadoCadastro('3,4', OAB, 8, secret='JBSWY3DPEHPK3PXP'))

        self.assertEqual(self.caminho(), '/api/v3/autenticador/certificado/cadastrar')
        self.assertEqual(dict(self.corpo()), {
            'tribunal_id': '3,4',
            'oab_numero': '12345',
            'oab_uf': 'RJ',
            'certificado_id': '8',
            'oab_letra': 'A',
            'secret': 'JBSWY3DPEHPK3PXP',
        })

    def test_login_regular_aceita_certificado(self):
        intimai = self.criar([(200, {}, {})] * 4)

        intimai.servicos.atualizar(AutenticadorRegularAtualizacao(5, 'usuario', 'senha', 8))
        intimai.servicos.atualizar(AutenticadorRegularAtualizacao(5, senha='nova'))
        intimai.servicos.atualizar(AutenticadorAlterarParaRegularAtualizacao(5, 'usuario', 'senha', 8))
        intimai.servicos.atualizar(AutenticadorAlterarParaRegularAtualizacao(5, 'usuario', 'senha'))

        self.assertEqual(self.caminho(0), '/api/v3/autenticador/regular/5/atualizar')
        self.assertEqual(self.corpo(0), [('usuario', 'usuario'), ('senha', 'senha'), ('certificado_id', '8')])
        self.assertEqual(self.corpo(1), [('senha', 'nova')])
        self.assertEqual(self.caminho(2), '/api/v3/autenticador/regular/5/alterar-para-regular')
        self.assertEqual(self.corpo(2), [('usuario', 'usuario'), ('senha', 'senha'), ('certificado_id', '8')])
        self.assertEqual(self.corpo(3), [('usuario', 'usuario'), ('senha', 'senha')])

    def test_protocolo_pje_sem_peticao_nao_envia_peticao(self):
        documento = Documento(self.arquivo_temporario('doc'), 1, 21, 'Documento')

        self.criar().servicos.solicitar(ProtocoloPjeSolicitacao(5, '0000001-00.2026.8.19.0001', 2, None, [documento]))

        self.assertEqual(self.caminho(), '/api/v3/pje/protocolo-processual/solicitar')
        self.assertTrue(self.requisicao().headers['Content-Type'].startswith('multipart/form-data'))
        self.assertEqual(self.campos(), {
            'autenticacao_id': '5',
            'numero_processo': '0000001-00.2026.8.19.0001',
            'tipo_documento_mensagem_geral': '2',
            'documentos[0][arquivo]': 'doc',
            'documentos[0][tipo_documento]': '21',
            'documentos[0][descricao_documento]': 'Documento',
            'documentos[0][ordem]': '1',
        })

    def test_protocolo_pje_trabalhista_envia_peticao(self):
        peticao = Peticao(self.arquivo_temporario('peticao'), 7, 'Petição')

        self.criar().servicos.solicitar(ProtocoloPjeSolicitacao(5, '0000001-00.2026.5.01.0001', 2, peticao))

        campos = self.campos()
        self.assertEqual(campos['peticao[arquivo]'], 'peticao')
        self.assertEqual(campos['peticao[tipo_documento]'], '7')
        self.assertEqual(campos['peticao[descricao_documento]'], 'Petição')

    def test_segunda_etapa_tjrj_envia_categoria_quando_informada(self):
        intimai = self.criar([(200, {}, {})] * 2)
        partes = [ParteVinculada('Fulano', 'Autor')]

        intimai.servicos.solicitar(ProtocoloTjrjSegundoPassoSolicitacao(9, 100, partes, Peticao(self.arquivo_temporario('p'), '', 'Petição'), [], 200))
        intimai.servicos.solicitar(ProtocoloTjrjSegundoPassoSolicitacao(9, 100, partes, Peticao(self.arquivo_temporario('p'), '', 'Petição')))

        self.assertEqual(self.caminho(0), '/api/v3/tjrj/protocolo-processual/9/segunda-etapa')
        campos = self.campos(0)
        self.assertEqual(campos['classe_id'], '100')
        self.assertEqual(campos['categoria_id'], '200')
        self.assertEqual(campos['partes_vinculadas[0][nome]'], 'Fulano')
        self.assertEqual(campos['partes_vinculadas[0][participacao]'], 'Autor')
        self.assertNotIn('categoria_id', self.campos(1))

    def test_segunda_etapa_da_habilitacao_envia_como_a_collection(self):
        intimai = self.criar([(200, {}, {})] * 2)
        documento = Documento(self.arquivo_temporario('procuracao'), 1, 21, 'Procuração')

        intimai.servicos.solicitar(ProtocoloHabilitacaoPjeSegundoPassoSolicitacao(
            9, TipoSolicitacao.HABILITACAO_SIMPLES, TipoDeclaracao.DECLARACAO_SOB_PENA_DE_LEI, Polo.PASSIVO,
            [ParteVinculada('node-1'), 'node-2'], 3, 'Descrição', 'Mensagem', [documento],
        ))
        intimai.servicos.solicitar(ProtocoloHabilitacaoPjeSegundoPassoSolicitacao(
            9, TipoSolicitacao.HABILITACAO_SIMPLES, TipoDeclaracao.TRT_NA_FORMA_DE_EXCECAO, Polo.ATIVO, ['node-1'], 3,
        ))

        self.assertEqual(self.caminho(0), '/api/v3/pje/protocolo-habilitacao/9/segunda-etapa')
        self.assertEqual(self.campos(0), {
            'tipo_solicitacao': '0',
            'tipo_declaracao': '0',
            'polo': '1',
            'tipo_documento_mensagem_geral': '3',
            'descricao': 'Descrição',
            'mensagem_geral': 'Mensagem',
            'partes_vinculadas[0]': 'node-1',
            'partes_vinculadas[1]': 'node-2',
            'documentos[0][arquivo]': 'procuracao',
            'documentos[0][tipo_documento]': '21',
            'documentos[0][descricao_documento]': 'Procuração',
            'documentos[0][ordem]': '1',
        })
        campos = self.campos(1)
        self.assertNotIn('descricao', campos)
        self.assertNotIn('mensagem_geral', campos)
        self.assertEqual(campos['tipo_declaracao'], '1')
