from intimai.api.api import API
from intimai.servicos.servicos import Servicos


class Intimai:
    def __init__(self, api_token: str, opcoes: dict = None):
        self._api = API(api_token, opcoes or {})
        self.servicos = Servicos(self._api)

    def definir_codigo_2fa(self, codigo) -> None:
        self._api.definir_codigo_2fa(codigo)
