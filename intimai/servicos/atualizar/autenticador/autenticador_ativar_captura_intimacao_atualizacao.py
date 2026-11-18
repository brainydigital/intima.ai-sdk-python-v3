from intimai.servicos.atualizar.servico_atualizacao import ServicoAtualizacao
from intimai.servicos.endpoint import EndpointMixin


class AutenticadorAtivarCapturaIntimacaoAtualizacao(ServicoAtualizacao, EndpointMixin):
    def __init__(self, id: int | str, abas: list | str, dias_de_captura: list | str, horarios_de_captura: list | str, capturar_procuradorias: bool | int = False):
        self._id = id
        self._abas = abas
        self._dias_de_captura = dias_de_captura
        self._horarios_de_captura = horarios_de_captura
        self._capturar_procuradorias = capturar_procuradorias

    def get_endpoint(self) -> str:
        return f'{self.AUTENTICADOR_ENDPOINT}/{self._id}/ativar-captura-intimacao'

    def get_request(self) -> dict:
        return {
            'form_params': {
                'abas': self._abas,
                'dias_de_captura': self._dias_de_captura,
                'horarios_de_captura': self._horarios_de_captura,
                'capturar_procuradorias': self._capturar_procuradorias,
            }
        }
