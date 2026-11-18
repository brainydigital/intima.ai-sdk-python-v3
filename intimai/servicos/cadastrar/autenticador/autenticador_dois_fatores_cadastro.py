from intimai.servicos.cadastrar.servico_cadastro import ServicoCadastro
from intimai.servicos.endpoint import EndpointMixin


class AutenticadorDoisFatoresCadastro(ServicoCadastro, EndpointMixin):
    def __init__(self, ids: int | str | list, secret: str):
        self._ids = ids
        self._secret = secret

    def get_endpoint(self) -> str:
        ids = ','.join(str(id) for id in self._ids) if isinstance(self._ids, (list, tuple)) else self._ids
        return f'{self.AUTENTICADOR_ENDPOINT}/{ids}{self.DOIS_FATORES_ENDPOINT}'

    def get_request(self) -> dict:
        return {'form_params': {'secret': self._secret}}
