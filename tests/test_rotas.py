from intimai.servicos.atualizar.autenticador.autenticador_alterar_para_certificado_atualizacao import AutenticadorAlterarParaCertificadoAtualizacao
from intimai.servicos.atualizar.autenticador.autenticador_alterar_para_regular_atualizacao import AutenticadorAlterarParaRegularAtualizacao
from intimai.servicos.atualizar.autenticador.autenticador_ativar_captura_intimacao_atualizacao import AutenticadorAtivarCapturaIntimacaoAtualizacao
from intimai.servicos.atualizar.autenticador.autenticador_desativar_captura_intimacao_atualizacao import AutenticadorDesativarCapturaIntimacaoAtualizacao
from intimai.servicos.atualizar.autenticador.autenticador_regular_atualizacao import AutenticadorRegularAtualizacao
from intimai.servicos.buscar.credito.credito_cotacao_busca import CreditoCotacaoBusca
from intimai.servicos.buscar.credito.credito_historico_busca import CreditoHistoricoBusca
from intimai.servicos.buscar.credito.credito_saldo_busca import CreditoSaldoBusca
from intimai.servicos.buscar.transacao.transacao_historico_busca import TransacaoHistoricoBusca
from tests.apoio import Caso


class TestRotas(Caso):
    def test_rotas_que_apontavam_para_endpoints_inexistentes(self):
        casos = [
            ('atualizar', AutenticadorAlterarParaCertificadoAtualizacao(5, 8), 'PUT', '/autenticador/certificado/5/alterar-para-certificado'),
            ('atualizar', AutenticadorAlterarParaRegularAtualizacao(5, 'usuario', 'senha'), 'PUT', '/autenticador/regular/5/alterar-para-regular'),
            ('atualizar', AutenticadorAtivarCapturaIntimacaoAtualizacao(5, ['aba'], [1], ['10:00']), 'PUT', '/autenticador/5/ativar-captura-intimacao'),
            ('atualizar', AutenticadorDesativarCapturaIntimacaoAtualizacao(5), 'PUT', '/autenticador/5/desativar-captura-intimacao'),
            ('atualizar', AutenticadorRegularAtualizacao(5, 'usuario'), 'PUT', '/autenticador/regular/5/atualizar'),
            ('buscar', CreditoCotacaoBusca(), 'GET', '/credito/cotacao-acoes'),
            ('buscar', CreditoHistoricoBusca(), 'GET', '/credito/historico'),
            ('buscar', CreditoSaldoBusca(), 'GET', '/credito/saldo'),
            ('buscar', TransacaoHistoricoBusca(), 'GET', '/transacao/historico'),
        ]
        intimai = self.criar([(200, {}, {})] * len(casos))

        for indice, (metodo_sdk, servico, metodo, caminho) in enumerate(casos):
            with self.subTest(servico=type(servico).__name__):
                getattr(intimai.servicos, metodo_sdk)(servico)
                self.assertEqual(self.requisicao(indice).method, metodo)
                self.assertEqual(self.caminho(indice), '/api/v3' + caminho)
