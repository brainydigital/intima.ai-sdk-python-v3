from intimai.servicos.atualizar.servico_atualizacao import ServicoAtualizacao
from intimai.servicos.endpoint import EndpointMixin


class AutenticadorAlterarParaRegularAtualizacao(ServicoAtualizacao, EndpointMixin):
    def __init__(self, id: int | str, usuario: str, senha: str):
        self._id = id
        self._usuario = usuario
        self._senha = senha

    def get_endpoint(self) -> str:
        return f'{self.AUTENTICADOR_ENDPOINT}/{self._id}{self.ALTERAR_PARA_REGULAR_ENDPOINT}'

    def get_request(self) -> dict:
        return {
            'form_params': {
                'usuario': self._usuario,
                'senha': self._senha,
            }
        }
