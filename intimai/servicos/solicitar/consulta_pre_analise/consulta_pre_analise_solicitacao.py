from intimai.servicos.solicitar.servico_solicitacao import ServicoSolicitacao
from intimai.servicos.endpoint import EndpointMixin


class ConsultaPreAnaliseSolicitacao(ServicoSolicitacao, EndpointMixin):
    def __init__(
        self,
        id_autenticador: int | str,
        numero_do_processo: str = '',
        nome_parte: str = '',
        nome_representante: str = '',
        oab: dict = None,
        numero_documento_parte: str = '',
    ):
        self._id_autenticador = id_autenticador
        self._numero_do_processo = numero_do_processo
        self._nome_parte = nome_parte
        self._nome_representante = nome_representante
        self._oab = oab
        self._numero_documento_parte = numero_documento_parte

    def get_endpoint(self) -> str:
        return f'{self.CONSULTA_PRE_ANALISE_ENDPOINT}{self.SOLICITAR_ENDPOINT}'

    def get_request(self) -> dict:
        form_params = {
            'autenticacao_id': self._id_autenticador,
            'numero_processo': self._numero_do_processo,
            'nome_parte': self._nome_parte,
            'nome_representante': self._nome_representante,
            'oab': self._oab,
            'numero_documento_parte': self._numero_documento_parte,
        }
        return {'form_params': form_params}
