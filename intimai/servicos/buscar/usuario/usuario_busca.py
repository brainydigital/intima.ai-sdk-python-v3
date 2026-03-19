from intimai.servicos.buscar.servico_busca import ServicoBusca
from intimai.servicos.endpoint import EndpointMixin


class UsuarioBusca(ServicoBusca, EndpointMixin):
    def get_endpoint(self) -> str:
        return f'{self.USUARIO_ENDPOINT}{self.BUSCAR_ENDPOINT}'
