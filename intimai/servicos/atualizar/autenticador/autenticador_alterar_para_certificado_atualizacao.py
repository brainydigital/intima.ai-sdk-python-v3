from intimai.servicos.atualizar.servico_atualizacao import ServicoAtualizacao
from intimai.servicos.endpoint import EndpointMixin


class AutenticadorAlterarParaCertificadoAtualizacao(ServicoAtualizacao, EndpointMixin):
    def __init__(self, id: int | str, id_certificado: int | str):
        self._id = id
        self._id_certificado = id_certificado

    def get_endpoint(self) -> str:
        return f'{self.AUTENTICADOR_ENDPOINT}/{self._id}{self.ALTERAR_PARA_CERTIFICADO_ENDPOINT}'

    def get_request(self) -> dict:
        return {
            'form_params': {
                'certificado_id': self._id_certificado,
            }
        }
