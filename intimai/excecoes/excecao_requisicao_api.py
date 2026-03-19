import json


class ExcecaoRequisicaoAPI(Exception):
    def __init__(self, message: str, code: int = 0):
        super().__init__(message)
        self.code = code

    def para_dict(self) -> dict:
        try:
            error = json.loads(str(self))
        except (json.JSONDecodeError, TypeError):
            error = str(self)
        return {
            'code': self.code,
            'error': error
        }
