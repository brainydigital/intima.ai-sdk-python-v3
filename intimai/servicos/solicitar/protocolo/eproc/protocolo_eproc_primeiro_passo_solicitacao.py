from intimai.servicos.solicitar.servico_solicitacao import ServicoSolicitacao
from intimai.servicos.endpoint import EndpointMixin


class ProtocoloEprocPrimeiroPassoSolicitacao(ServicoSolicitacao, EndpointMixin):
    def __init__(self, id_autenticador: int | str, numero_do_processo: str):
        self._id_autenticador = id_autenticador
        self._numero_do_processo = numero_do_processo

    def get_endpoint(self) -> str:
        return f'{self.EPROC_ENDPOINT}{self.PROTOCOLO_ENDPOINT}{self.PRIMEIRA_ETAPA_ENDPOINT}'

    def get_request(self) -> dict:
        return {
            'form_params': {
                'autenticacao_id': self._id_autenticador,
                'numero_processo': self._numero_do_processo,
            }
        }
