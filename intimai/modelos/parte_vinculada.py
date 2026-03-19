class ParteVinculada:
    def __init__(self, nome: str, participacao: str | None = None):
        self._nome = nome
        self._participacao = participacao

    def get_nome(self) -> str:
        return self._nome

    def get_participacao(self) -> str | None:
        return self._participacao
