from intimai.servicos.buscar.servico_busca import ServicoBusca
from intimai.servicos.endpoint import EndpointMixin


class CodigoAjudaBusca(ServicoBusca, EndpointMixin):
    def get_endpoint(self) -> str:
        return f'{self.CODIGO_AJUDA_ENDPOINT}{self.BUSCAR_ENDPOINT}'
