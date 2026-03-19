from intimai.servicos.solicitar_cadastro.servico_solicitacao_cadastro import ServicoSolicitacaoCadastro
from intimai.servicos.endpoint import EndpointMixin
from intimai.modelos.certificado import Certificado


class CertificadoSolicitacaoCadastro(ServicoSolicitacaoCadastro, EndpointMixin):
    def __init__(self, certificado: Certificado):
        self._certificado = certificado

    def get_endpoint(self) -> str:
        return f'{self.CERTIFICADO_ENDPOINT}{self.SOLICITAR_CADASTRO_ENDPOINT}'

    def get_request(self) -> dict:
        return {'multipart': self._certificado.em_array()}
