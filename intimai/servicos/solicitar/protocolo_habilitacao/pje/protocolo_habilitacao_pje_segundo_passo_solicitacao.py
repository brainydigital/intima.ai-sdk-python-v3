from intimai.modelos.parte_vinculada import ParteVinculada
from intimai.servicos.solicitar.servico_solicitacao import ServicoSolicitacao
from intimai.servicos.endpoint import EndpointMixin
from intimai.servicos.helpers import HelpersMixin


class ProtocoloHabilitacaoPjeSegundoPassoSolicitacao(ServicoSolicitacao, EndpointMixin, HelpersMixin):
    def __init__(
        self,
        id: int | str,
        tipo_solicitacao: int,
        tipo_declaracao: int,
        polo: int,
        partes_vinculadas: list,
        tipo_documento_mensagem_geral: int | str,
        descricao: str = None,
        mensagem_geral: str = None,
        documentos: list = None,
    ):
        self._id = id
        self._tipo_solicitacao = tipo_solicitacao
        self._tipo_declaracao = tipo_declaracao
        self._polo = polo
        self._partes_vinculadas = partes_vinculadas
        self._tipo_documento_mensagem_geral = tipo_documento_mensagem_geral
        self._descricao = descricao
        self._mensagem_geral = mensagem_geral
        self._documentos = documentos or []

    def get_endpoint(self) -> str:
        return f'{self.PJE_ENDPOINT}{self.PROTOCOLO_HABILITACAO_ENDPOINT}/{self._id}{self.SEGUNDA_ETAPA_ENDPOINT}'

    def get_request(self) -> dict:
        parametros = {
            'tipo_solicitacao': self._tipo_solicitacao,
            'tipo_declaracao': self._tipo_declaracao,
            'polo': self._polo,
            'tipo_documento_mensagem_geral': self._tipo_documento_mensagem_geral,
            'descricao': self._descricao,
            'mensagem_geral': self._mensagem_geral,
        }

        for indice, parte in enumerate(self._partes_vinculadas):
            parametros[f'partes_vinculadas[{indice}]'] = parte.get_nome() if isinstance(parte, ParteVinculada) else parte

        self._definir_documentos(self._documentos, parametros)

        return {'multipart': self._definir_multipart(parametros)}
