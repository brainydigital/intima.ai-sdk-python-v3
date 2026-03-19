from intimai.servicos.atualizar.servico_atualizacao import ServicoAtualizacao
from intimai.servicos.endpoint import EndpointMixin


class NotificacaoEmailAtualizacao(ServicoAtualizacao, EndpointMixin):
    def __init__(self, id: str, email: str):
        self._id = id
        self._email = email

    def get_endpoint(self) -> str:
        return f'{self.NOTIFICACAO_ENDPOINT}{self.EMAIL_ENDPOINT}/{self._id}{self.ATUALIZAR_ENDPOINT}'

    def get_request(self) -> dict:
        return {
            'form_params': {
                'email': self._email,
            }
        }
