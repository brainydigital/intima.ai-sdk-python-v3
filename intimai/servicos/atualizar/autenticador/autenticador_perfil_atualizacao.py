from intimai.servicos.atualizar.servico_atualizacao import ServicoAtualizacao
from intimai.servicos.endpoint import EndpointMixin


class AutenticadorPerfilAtualizacao(ServicoAtualizacao, EndpointMixin):
    def __init__(self, id: int | str, usuario_sigla: str = None, usuario_descricao: str = None):
        self._id = id
        self._usuario_sigla = usuario_sigla
        self._usuario_descricao = usuario_descricao

    def get_endpoint(self) -> str:
        return f'{self.AUTENTICADOR_ENDPOINT}/{self._id}{self.ATUALIZAR_PERFIL_ENDPOINT}'

    def get_request(self) -> dict:
        return {
            'form_params': {
                'usuario_sigla': self._usuario_sigla,
                'usuario_descricao': self._usuario_descricao,
            }
        }
