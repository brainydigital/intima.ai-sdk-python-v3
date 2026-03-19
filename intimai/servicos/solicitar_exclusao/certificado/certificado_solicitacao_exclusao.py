from intimai.servicos.solicitar_exclusao.servico_solicitacao_exclusao import ServicoSolicitacaoExclusao
from intimai.servicos.endpoint import EndpointMixin


class CertificadoSolicitacaoExclusao(ServicoSolicitacaoExclusao, EndpointMixin):
    def __init__(self, id: int | str):
        self._id = id

    def get_endpoint(self) -> str:
        return f'{self.CERTIFICADO_ENDPOINT}/{self._id}{self.SOLICITAR_EXCLUSAO_ENDPOINT}'
