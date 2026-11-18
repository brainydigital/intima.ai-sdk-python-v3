from intimai.servicos.atualizar.servico_atualizacao import ServicoAtualizacao
from intimai.servicos.endpoint import EndpointMixin


class AutenticadorRegularAtualizacao(ServicoAtualizacao, EndpointMixin):
    def __init__(self, id: int | str, usuario: str = None, senha: str = None, id_certificado: int | str = None):
        self._id = id
        self._usuario = usuario
        self._senha = senha
        self._id_certificado = id_certificado

    def get_endpoint(self) -> str:
        return f'{self.AUTENTICADOR_ENDPOINT}{self.REGULAR_ENDPOINT}/{self._id}{self.ATUALIZAR_ENDPOINT}'

    def get_request(self) -> dict:
        form_params = {}
        if self._usuario is not None:
            form_params['usuario'] = self._usuario
        if self._senha is not None:
            form_params['senha'] = self._senha
        if self._id_certificado is not None:
            form_params['certificado_id'] = self._id_certificado
        return {'form_params': form_params}
