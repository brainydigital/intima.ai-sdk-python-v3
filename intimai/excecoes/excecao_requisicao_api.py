class ExcecaoRequisicaoAPI(Exception):
    def __init__(self, message: str, code: int = 0, corpo=None, headers: dict = None):
        super().__init__(message)
        self.code = code
        self.corpo = corpo
        self.headers = dict(headers or {})

    @classmethod
    def da_resposta(cls, resposta) -> 'ExcecaoRequisicaoAPI':
        try:
            corpo = resposta.json()
        except ValueError:
            corpo = resposta.text

        status = resposta.status_code
        mensagem = _mensagem_do_corpo(corpo, apenas_message=True)

        if status == 401 and isinstance(mensagem, str) and '2FA' in mensagem:
            classe = ExcecaoDoisFatores
        elif status == 429:
            classe = ExcecaoLimiteDeRequisicoes
        else:
            classe = ExcecaoRequisicaoAPI

        return classe(f'{status} {resposta.reason or ""}'.strip(), status, corpo, resposta.headers)

    def get_status(self) -> int:
        return self.code

    def get_corpo(self):
        return self.corpo

    def get_mensagem(self) -> str:
        mensagem = _mensagem_do_corpo(self.corpo)
        return mensagem if isinstance(mensagem, str) else str(self)

    def get_erros(self) -> dict:
        if self.code != 422 or not isinstance(self.corpo, dict):
            return {}
        return {chave: valor for chave, valor in self.corpo.items() if isinstance(valor, list)}

    def get_header(self, nome: str):
        for chave, valor in self.headers.items():
            if chave.lower() == nome.lower():
                return valor
        return None

    def para_dict(self) -> dict:
        return {
            'code': self.code,
            'error': self.corpo if self.corpo is not None else str(self),
        }


class ExcecaoDoisFatores(ExcecaoRequisicaoAPI):
    pass


class ExcecaoLimiteDeRequisicoes(ExcecaoRequisicaoAPI):
    def get_retry_after(self):
        valor = self.get_header('Retry-After')
        return int(valor) if isinstance(valor, str) and valor.isdigit() else None


def _mensagem_do_corpo(corpo, apenas_message: bool = False):
    if not isinstance(corpo, dict):
        return None

    dados = corpo.get('data')

    if isinstance(dados, dict) and dados.get('message') is not None:
        return dados['message']

    if corpo.get('message') is not None:
        return corpo['message']

    return None if apenas_message else corpo.get('error')
