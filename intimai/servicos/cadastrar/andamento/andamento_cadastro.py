from intimai.servicos.cadastrar.servico_cadastro import ServicoCadastro
from intimai.servicos.endpoint import EndpointMixin


class AndamentoCadastro(ServicoCadastro, EndpointMixin):
    def __init__(self, id_autenticador: int | str, numero_do_processo: str):
        self._id_autenticador = id_autenticador
        self._numero_do_processo = numero_do_processo

    def get_endpoint(self) -> str:
        return f'{self.ANDAMENTO_ENDPOINT}{self.CADASTRAR_ENDPOINT}'

    def get_request(self) -> dict:
        return {
            'form_params': {
                'autenticacao_id': self._id_autenticador,
                'numero_processo': self._numero_do_processo,
            }
        }
