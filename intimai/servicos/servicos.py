from intimai.api.api import API
from intimai.servicos.solicitar.servico_solicitacao import ServicoSolicitacao
from intimai.servicos.buscar.servico_busca import ServicoBusca
from intimai.servicos.cadastrar.servico_cadastro import ServicoCadastro
from intimai.servicos.atualizar.servico_atualizacao import ServicoAtualizacao
from intimai.servicos.excluir.servico_exclusao import ServicoExclusao
from intimai.servicos.resultado.servico_resultado import ServicoResultado
from intimai.servicos.solicitar_cadastro.servico_solicitacao_cadastro import ServicoSolicitacaoCadastro
from intimai.servicos.solicitar_atualizacao.servico_solicita_atualizacao import ServicoSolicitaAtualizacao
from intimai.servicos.solicitar_exclusao.servico_solicitacao_exclusao import ServicoSolicitacaoExclusao
from intimai.servicos.tentar_novamente.servico_tenta_novamente import ServicoTentaNovamente


class Servicos:
    def __init__(self, api: API):
        self._api = api

    def solicitar(self, servico: ServicoSolicitacao) -> dict:
        return self._api.post(servico.get_endpoint(), servico.get_request())

    def buscar(self, servico: ServicoBusca, pagina: int = 1, filtros: dict = None) -> dict:
        return self._api.get(servico.get_endpoint(), pagina, filtros or {})

    def cadastrar(self, servico: ServicoCadastro) -> dict:
        return self._api.post(servico.get_endpoint(), servico.get_request())

    def atualizar(self, servico: ServicoAtualizacao) -> dict:
        return self._api.put(servico.get_endpoint(), servico.get_request())

    def excluir(self, servico: ServicoExclusao) -> dict:
        return self._api.delete(servico.get_endpoint())

    def solicitar_cadastro(self, servico: ServicoSolicitacaoCadastro) -> dict:
        return self._api.post(servico.get_endpoint(), servico.get_request())

    def solicitar_atualizacao(self, servico: ServicoSolicitaAtualizacao) -> dict:
        return self._api.post(servico.get_endpoint(), servico.get_request())

    def solicitar_exclusao(self, servico: ServicoSolicitacaoExclusao) -> dict:
        return self._api.delete(servico.get_endpoint())

    def resultado(self, servico: ServicoResultado) -> dict:
        return self._api.get(servico.get_endpoint())

    def tentar_novamente(self, servico: ServicoTentaNovamente) -> dict:
        return self._api.get(servico.get_endpoint())
