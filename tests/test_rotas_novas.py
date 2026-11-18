from intimai import SituacaoCapturaAgendada, SituacaoNovaTentativa, StatusAcao, TipoCapturaAgendada, ExcecaoRequisicaoAPI
from intimai.servicos.atualizar.autenticador.autenticador_desabilitar_atualizacao import AutenticadorDesabilitarAtualizacao
from intimai.servicos.atualizar.autenticador.autenticador_habilitar_atualizacao import AutenticadorHabilitarAtualizacao
from intimai.servicos.atualizar.autenticador.autenticador_perfil_atualizacao import AutenticadorPerfilAtualizacao
from intimai.servicos.buscar.acao.acao_busca import AcaoBusca
from intimai.servicos.buscar.captura_agendada.captura_agendada_busca import CapturaAgendadaBusca
from intimai.servicos.buscar.codigo_ajuda.codigo_ajuda_busca import CodigoAjudaBusca
from intimai.servicos.buscar.credito.credito_consumo_mensal_busca import CreditoConsumoMensalBusca
from intimai.servicos.buscar.protocolo.tipo_documento_mensagem_geral.tipo_documento_mensagem_geral_projudi_busca import TipoDocumentoMensagemGeralProjudiBusca
from intimai.servicos.cadastrar.autenticador.autenticador_dois_fatores_cadastro import AutenticadorDoisFatoresCadastro
from intimai.servicos.solicitar.acao.acao_cancelar_consulta_solicitacao import AcaoCancelarConsultaSolicitacao
from intimai.servicos.solicitar.acao.acao_confirmar_consulta_solicitacao import AcaoConfirmarConsultaSolicitacao
from intimai.servicos.solicitar.autenticador.autenticador_capturar_intimacoes_solicitacao import AutenticadorCapturarIntimacoesSolicitacao
from tests.apoio import Caso


class TestRotasNovas(Caso):
    def confere(self, indice, metodo, caminho, corpo=None):
        self.assertEqual(self.requisicao(indice).method, metodo)
        self.assertEqual(self.caminho(indice), '/api/v3' + caminho)
        self.assertEqual(self.query(indice)['api_token'], 'token-teste')
        self.assertEqual(self.corpo(indice), corpo or [])

    def test_confirmar_consulta(self):
        resposta = {'message': 'Consulta Processual confirmada!', 'data': {'id': 9, 'status': StatusAcao.NA_FILA}}

        resultado = self.criar([(200, resposta, {})]).servicos.solicitar(AcaoConfirmarConsultaSolicitacao(9))

        self.confere(0, 'POST', '/acao/9/confirmar-consulta')
        self.assertEqual(resultado, resposta)

    def test_cancelar_consulta(self):
        resultado = self.criar([(200, {'data': {'id': 9, 'status': 14}}, {})]).servicos.solicitar(AcaoCancelarConsultaSolicitacao(9))

        self.confere(0, 'POST', '/acao/9/cancelar-consulta')
        self.assertEqual(resultado['data']['status'], StatusAcao.CANCELADA)

    def test_confirmar_consulta_de_outro_usuario_da_404(self):
        intimai = self.criar([(404, {'message': 'Ação não encontrada.'}, {})])

        with self.assertRaises(ExcecaoRequisicaoAPI) as contexto:
            intimai.servicos.solicitar(AcaoConfirmarConsultaSolicitacao(1))

        self.assertEqual(contexto.exception.get_status(), 404)
        self.assertEqual(contexto.exception.get_mensagem(), 'Ação não encontrada.')

    def test_atualizar_perfil_do_autenticador(self):
        intimai = self.criar([(200, {}, {})] * 2)

        intimai.servicos.atualizar(AutenticadorPerfilAtualizacao(5, 'ADV', 'Escritório'))
        intimai.servicos.atualizar(AutenticadorPerfilAtualizacao(5, usuario_descricao='Escritório'))

        self.confere(0, 'PUT', '/autenticador/5/atualizar-perfil', [('usuario_sigla', 'ADV'), ('usuario_descricao', 'Escritório')])
        self.confere(1, 'PUT', '/autenticador/5/atualizar-perfil', [('usuario_descricao', 'Escritório')])

    def test_capturar_intimacoes_agora(self):
        self.criar().servicos.solicitar(AutenticadorCapturarIntimacoesSolicitacao(5))

        self.confere(0, 'POST', '/autenticador/5/capturar-intimacoes')

    def test_capturar_intimacoes_com_captura_desligada_da_422(self):
        mensagem = 'Ative a captura de intimações deste autenticador para capturar agora.'
        intimai = self.criar([(422, {'message': mensagem}, {})])

        with self.assertRaises(ExcecaoRequisicaoAPI) as contexto:
            intimai.servicos.solicitar(AutenticadorCapturarIntimacoesSolicitacao(5))

        self.assertEqual(contexto.exception.get_status(), 422)
        self.assertEqual(contexto.exception.get_mensagem(), mensagem)

    def test_habilitar_e_desabilitar_autenticador(self):
        intimai = self.criar([(200, {}, {})] * 2)

        intimai.servicos.atualizar(AutenticadorHabilitarAtualizacao(5))
        intimai.servicos.atualizar(AutenticadorDesabilitarAtualizacao(5))

        self.confere(0, 'PUT', '/autenticador/5/habilitar')
        self.confere(1, 'PUT', '/autenticador/5/desabilitar')

    def test_armazenar_2fa_em_um_ou_varios_autenticadores(self):
        intimai = self.criar([(200, {}, {})] * 2)

        intimai.servicos.cadastrar(AutenticadorDoisFatoresCadastro(5, 'JBSWY3DPEHPK3PXP'))
        intimai.servicos.cadastrar(AutenticadorDoisFatoresCadastro([5, 6, 7], 'JBSWY3DPEHPK3PXP'))

        self.confere(0, 'POST', '/autenticador/5/2fa/armazenar', [('secret', 'JBSWY3DPEHPK3PXP')])
        self.confere(1, 'POST', '/autenticador/5,6,7/2fa/armazenar', [('secret', 'JBSWY3DPEHPK3PXP')])

    def test_consumo_mensal_com_e_sem_data(self):
        intimai = self.criar([(200, {}, {})] * 2)

        intimai.servicos.buscar(CreditoConsumoMensalBusca(), 1, {'date': '2026-10'})
        intimai.servicos.buscar(CreditoConsumoMensalBusca())

        self.confere(0, 'GET', '/credito/consumo-mensal')
        self.assertEqual(self.query(0)['date'], '2026-10')
        self.assertNotIn('date', self.query(1))

    def test_buscar_capturas_agendadas_com_filtros(self):
        self.criar().servicos.buscar(CapturaAgendadaBusca(), 2, {
            'data_inicial': '01/11/2026',
            'data_final': '13/11/2026',
            'autenticadores_ids': '5,6',
            'tipos': TipoCapturaAgendada.INTIMACAO,
            'situacoes': f'{SituacaoCapturaAgendada.NAO_EXECUTADA},{SituacaoCapturaAgendada.ERRO}',
        })

        self.confere(0, 'GET', '/captura-agendada/buscar')
        self.assertEqual(self.query(0), {
            'api_token': 'token-teste',
            'page': '2',
            'data_inicial': '01/11/2026',
            'data_final': '13/11/2026',
            'autenticadores_ids': '5,6',
            'tipos': 'intimacao',
            'situacoes': 'nao_executada,erro',
        })

    def test_buscar_uma_captura_agendada(self):
        self.criar().servicos.buscar(CapturaAgendadaBusca(31))

        self.confere(0, 'GET', '/captura-agendada/31/buscar')

    def test_buscar_tipos_documento_mensagem_geral_do_projudi(self):
        resposta = {'message': 'Tipos documentos mensagem geral encontrados para o tribunal do autenticador selecionado!', 'data': [{'id': 1, 'nome': 'Petição'}]}

        resultado = self.criar([(200, resposta, {})]).servicos.buscar(TipoDocumentoMensagemGeralProjudiBusca(5))

        self.confere(0, 'GET', '/projudi/protocolo-processual/5/tipos-documento-mensagem-geral')
        self.assertEqual(resultado, resposta)

    def test_tipos_documento_mensagem_geral_com_autenticador_fora_do_projudi_da_422(self):
        mensagem = 'Este autenticador não pertence ao sistema Projudi'
        intimai = self.criar([(422, {'message': mensagem}, {})])

        with self.assertRaises(ExcecaoRequisicaoAPI) as contexto:
            intimai.servicos.buscar(TipoDocumentoMensagemGeralProjudiBusca(5))

        self.assertEqual(contexto.exception.get_status(), 422)
        self.assertEqual(contexto.exception.get_mensagem(), mensagem)

    def test_buscar_catalogo_de_codigos_de_ajuda(self):
        resposta = {'message': 'Códigos encontrados!', 'data': {
            'faixas': [{'value': 'isenta', 'titulo': 'Sem cobrança', 'total': 47}],
            'nova_tentativa_aviso': 'A nova tentativa automática só acontece nos códigos marcados, em ações criadas no mesmo dia.',
            'grupos': [{'nome': 'Erros Gerais', 'slug': 'erros-gerais', 'codigos': [
                {'codigo': 606, 'faixa': 'isenta', 'nova_tentativa': 'Nova tentativa automática: até 3×, a cada 30 min.'},
            ]}],
        }}

        resultado = self.criar([(200, resposta, {})]).servicos.buscar(CodigoAjudaBusca())

        self.confere(0, 'GET', '/codigo-ajuda/buscar')
        self.assertNotIn('codigo', self.query(0))
        self.assertEqual(resultado, resposta)

    def test_buscar_codigo_de_ajuda_pelo_codigo(self):
        self.criar([(200, {}, {})]).servicos.buscar(CodigoAjudaBusca(), 1, {'codigo': 606})

        self.confere(0, 'GET', '/codigo-ajuda/buscar')
        self.assertEqual(self.query(0)['codigo'], '606')

    def test_codigo_de_ajuda_fora_do_catalogo_da_404(self):
        mensagem = 'Nenhum código encontrado no catálogo.'
        intimai = self.criar([(404, {'message': mensagem}, {})])

        with self.assertRaises(ExcecaoRequisicaoAPI) as contexto:
            intimai.servicos.buscar(CodigoAjudaBusca(), 1, {'codigo': 99999})

        self.assertEqual(contexto.exception.get_status(), 404)
        self.assertEqual(contexto.exception.get_mensagem(), mensagem)

    def test_acao_com_erro_traz_a_nova_tentativa_automatica(self):
        nova_tentativa = {
            'automatica': True,
            'situacao': SituacaoNovaTentativa.AGENDADA,
            'tentativa': 1,
            'max_tentativas': 3,
            'prevista_para': '2026-11-18 10:30:00',
            'mensagem': 'Nova tentativa automática 1 de 3 a partir de 10:30. Não é preciso criar outra ação.',
        }

        resultado = self.criar([(200, {'data': {'id': 9, 'status': StatusAcao.ERRO, 'nova_tentativa': nova_tentativa}}, {})]).servicos.buscar(AcaoBusca(9))

        self.confere(0, 'GET', '/acao/9/buscar')
        self.assertEqual(resultado['data']['nova_tentativa'], nova_tentativa)

    def test_situacoes_da_nova_tentativa_batem_com_a_api(self):
        self.assertEqual(
            [SituacaoNovaTentativa.AGENDADA, SituacaoNovaTentativa.AGUARDANDO_CONDICAO, SituacaoNovaTentativa.ENCERRADA, SituacaoNovaTentativa.SEM_NOVA_TENTATIVA],
            ['agendada', 'aguardando_condicao', 'encerrada', 'sem_nova_tentativa'],
        )
