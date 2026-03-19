from intimai.servicos.cadastrar.servico_cadastro import ServicoCadastro
from intimai.servicos.endpoint import EndpointMixin


class NotificacaoWebhookCadastro(ServicoCadastro, EndpointMixin):
    def __init__(self, tipo_acao: int | str, verbo_http: str, url: str):
        self._tipo_acao = tipo_acao
        self._verbo_http = verbo_http
        self._url = url

    def get_endpoint(self) -> str:
        return f'{self.NOTIFICACAO_ENDPOINT}{self.WEBHOOK_ENDPOINT}{self.CADASTRAR_ENDPOINT}'

    def get_request(self) -> dict:
        return {
            'form_params': {
                'tipo_acao': self._tipo_acao,
                'verbo_http': self._verbo_http,
                'url': self._url,
            }
        }
