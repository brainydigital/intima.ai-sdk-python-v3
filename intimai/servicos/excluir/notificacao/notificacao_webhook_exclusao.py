from intimai.servicos.excluir.servico_exclusao import ServicoExclusao
from intimai.servicos.endpoint import EndpointMixin


class NotificacaoWebhookExclusao(ServicoExclusao, EndpointMixin):
    def __init__(self, id: int | str):
        self._id = id

    def get_endpoint(self) -> str:
        return f'{self.NOTIFICACAO_ENDPOINT}{self.WEBHOOK_ENDPOINT}/{self._id}{self.EXCLUIR_ENDPOINT}'
