from intimai.servicos.solicitar.servico_solicitacao import ServicoSolicitacao
from intimai.servicos.endpoint import EndpointMixin
from intimai.servicos.helpers import HelpersMixin


class ProtocoloProjudiSolicitacao(ServicoSolicitacao, EndpointMixin, HelpersMixin):
    def __init__(self, id_autenticador: int | str, numero_do_processo: str, tipo_documento_mensagem_geral: int | str, documentos: list = None):
        self._id_autenticador = id_autenticador
        self._numero_do_processo = numero_do_processo
        self._tipo_documento_mensagem_geral = tipo_documento_mensagem_geral
        self._documentos = documentos or []

    def get_endpoint(self) -> str:
        return f'{self.PROJUDI_ENDPOINT}{self.PROTOCOLO_ENDPOINT}{self.SOLICITAR_ENDPOINT}'

    def get_request(self) -> dict:
        parametros = {
            'autenticacao_id': self._id_autenticador,
            'numero_processo': self._numero_do_processo,
            'tipo_documento_mensagem_geral': self._tipo_documento_mensagem_geral,
        }
        self._definir_documentos(self._documentos, parametros)
        return {'multipart': self._definir_multipart(parametros)}
