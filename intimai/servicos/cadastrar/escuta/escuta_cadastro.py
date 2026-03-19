from intimai.servicos.cadastrar.servico_cadastro import ServicoCadastro
from intimai.servicos.endpoint import EndpointMixin


class EscutaCadastro(ServicoCadastro, EndpointMixin):
    def __init__(self, id_autenticador: int | str, numero_do_processo: str, dias_de_captura: list | str, horarios_de_captura: list | str):
        self._id_autenticador = id_autenticador
        self._numero_do_processo = numero_do_processo
        self._dias_de_captura = dias_de_captura
        self._horarios_de_captura = horarios_de_captura

    def get_endpoint(self) -> str:
        return f'{self.ESCUTA_ENDPOINT}{self.CADASTRAR_ENDPOINT}'

    def get_request(self) -> dict:
        return {
            'form_params': {
                'autenticacao_id': self._id_autenticador,
                'numero_processo': self._numero_do_processo,
                'dias_de_captura': self._dias_de_captura,
                'horarios_de_captura': self._horarios_de_captura,
            }
        }
