from intimai.servicos.atualizar.servico_atualizacao import ServicoAtualizacao
from intimai.servicos.endpoint import EndpointMixin


class EscutaAtualizacao(ServicoAtualizacao, EndpointMixin):
    def __init__(self, id: int | str, dias_de_captura: list | str, horarios_de_captura: list | str):
        self._id = id
        self._dias_de_captura = dias_de_captura
        self._horarios_de_captura = horarios_de_captura

    def get_endpoint(self) -> str:
        return f'{self.ESCUTA_ENDPOINT}/{self._id}{self.ATUALIZAR_ENDPOINT}'

    def get_request(self) -> dict:
        return {
            'form_params': {
                'dias_de_captura': self._dias_de_captura,
                'horarios_de_captura': self._horarios_de_captura,
            }
        }
