from intimai.servicos.solicitar.servico_solicitacao import ServicoSolicitacao
from intimai.servicos.endpoint import EndpointMixin
from intimai.servicos.helpers import HelpersMixin
from intimai.modelos.peticao import Peticao


class ProtocoloTjrjSegundoPassoSolicitacao(ServicoSolicitacao, EndpointMixin, HelpersMixin):
    def __init__(self, id: int | str, id_classe: int | str, partes_vinculadas: list, peticao: Peticao, documentos: list = None):
        self._id = id
        self._id_classe = id_classe
        self._partes_vinculadas = partes_vinculadas
        self._peticao = peticao
        self._documentos = documentos or []

    def get_endpoint(self) -> str:
        return f'{self.TJRJ_ENDPOINT}{self.PROTOCOLO_ENDPOINT}/{self._id}{self.SEGUNDA_ETAPA_ENDPOINT}'

    def get_request(self) -> dict:
        parametros = {
            'classe_id': self._id_classe,
        }
        self._definir_partes(self._partes_vinculadas, parametros)
        self._definir_peticao(self._peticao, parametros)
        self._definir_documentos(self._documentos, parametros)
        return {'multipart': self._definir_multipart(parametros)}
