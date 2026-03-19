from intimai.servicos.cadastrar.servico_cadastro import ServicoCadastro
from intimai.servicos.endpoint import EndpointMixin


class NotificacaoEmailCadastro(ServicoCadastro, EndpointMixin):
    def __init__(self, email: str):
        self._email = email

    def get_endpoint(self) -> str:
        return f'{self.NOTIFICACAO_ENDPOINT}{self.EMAIL_ENDPOINT}{self.CADASTRAR_ENDPOINT}'

    def get_request(self) -> dict:
        return {
            'form_params': {
                'email': self._email,
            }
        }
