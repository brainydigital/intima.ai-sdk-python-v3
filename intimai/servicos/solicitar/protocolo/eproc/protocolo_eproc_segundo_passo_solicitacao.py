from intimai.servicos.solicitar.servico_solicitacao import ServicoSolicitacao
from intimai.servicos.endpoint import EndpointMixin
from intimai.servicos.helpers import HelpersMixin


class ProtocoloEprocSegundoPassoSolicitacao(ServicoSolicitacao, EndpointMixin, HelpersMixin):
    def __init__(self, id: int | str, tipo_documento_mensagem_geral: int | str, partes_vinculadas: list, documentos: list = None):
        self._id = id
        self._tipo_documento_mensagem_geral = tipo_documento_mensagem_geral
        self._partes_vinculadas = partes_vinculadas
        self._documentos = documentos or []

    def get_endpoint(self) -> str:
        return f'{self.EPROC_ENDPOINT}{self.PROTOCOLO_ENDPOINT}/{self._id}{self.SEGUNDA_ETAPA_ENDPOINT}'

    def get_request(self) -> dict:
        parametros = {
            'tipo_documento_mensagem_geral': self._tipo_documento_mensagem_geral,
        }
        self._definir_partes(self._partes_vinculadas, parametros)
        self._definir_documentos(self._documentos, parametros)
        return {'multipart': self._definir_multipart(parametros)}
