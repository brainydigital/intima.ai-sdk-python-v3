from intimai.servicos.solicitar_atualizacao.servico_solicita_atualizacao import ServicoSolicitaAtualizacao
from intimai.servicos.endpoint import EndpointMixin
from intimai.modelos.certificado import Certificado


class CertificadoSolicitaAtualizacao(ServicoSolicitaAtualizacao, EndpointMixin):
    def __init__(self, id: int | str, certificado: Certificado):
        self._id = id
        self._certificado = certificado

    def get_endpoint(self) -> str:
        return f'{self.CERTIFICADO_ENDPOINT}/{self._id}{self.SOLICITAR_ATUALIZACAO_ENDPOINT}'

    def get_request(self) -> dict:
        return {'multipart': self._certificado.em_array()}
