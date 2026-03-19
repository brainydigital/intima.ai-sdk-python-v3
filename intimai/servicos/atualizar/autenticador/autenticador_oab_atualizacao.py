from intimai.servicos.atualizar.servico_atualizacao import ServicoAtualizacao
from intimai.servicos.endpoint import EndpointMixin


class AutenticadorOabAtualizacao(ServicoAtualizacao, EndpointMixin):
    def __init__(self, id: int | str, oab: dict):
        self._id = id
        self._oab = oab

    def get_endpoint(self) -> str:
        return f'{self.AUTENTICADOR_ENDPOINT}/{self._id}/atualizar-oab'

    def get_request(self) -> dict:
        form_params = {
            'oab_numero': self._oab.get('numero'),
            'oab_uf': self._oab.get('uf'),
        }
        if self._oab.get('letra'):
            form_params['oab_letra'] = self._oab['letra']
        return {'form_params': form_params}
