from intimai.servicos.atualizar.servico_atualizacao import ServicoAtualizacao
from intimai.servicos.endpoint import EndpointMixin


class NotificacaoWebhookAtualizacao(ServicoAtualizacao, EndpointMixin):
    def __init__(self, id: str, tipo_acao: str, verbo_http: str, url: str):
        self._id = id
        self._tipo_acao = tipo_acao
        self._verbo_http = verbo_http
        self._url = url

    def get_endpoint(self) -> str:
        return f'{self.NOTIFICACAO_ENDPOINT}{self.WEBHOOK_ENDPOINT}/{self._id}{self.ATUALIZAR_ENDPOINT}'

    def get_request(self) -> dict:
        return {
            'form_params': {
                'tipo_acao': self._tipo_acao,
                'verbo_http': self._verbo_http,
                'url': self._url,
            }
        }
