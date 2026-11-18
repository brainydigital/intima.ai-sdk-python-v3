from intimai.servicos.cadastrar.servico_cadastro import ServicoCadastro
from intimai.servicos.endpoint import EndpointMixin


class AutenticadorCertificadoCadastro(ServicoCadastro, EndpointMixin):
    def __init__(
        self,
        id_tribunal: int | str | list,
        oab: dict,
        id_certificado: int | str,
        usuario_sigla: str = None,
        usuario_descricao: str = None,
        secret: str = None,
    ):
        self._id_tribunal = id_tribunal
        self._oab = oab
        self._id_certificado = id_certificado
        self._usuario_sigla = usuario_sigla
        self._usuario_descricao = usuario_descricao
        self._secret = secret

    def get_endpoint(self) -> str:
        return f'{self.AUTENTICADOR_ENDPOINT}{self.CERTIFICADO_ENDPOINT}{self.CADASTRAR_ENDPOINT}'

    def get_request(self) -> dict:
        form_params = {
            'tribunal_id': self._id_tribunal,
            'oab_numero': self._oab.get('numero'),
            'oab_uf': self._oab.get('uf'),
            'certificado_id': self._id_certificado,
        }
        if self._oab.get('letra'):
            form_params['oab_letra'] = self._oab['letra']
        form_params['usuario_sigla'] = self._usuario_sigla
        form_params['usuario_descricao'] = self._usuario_descricao
        form_params['secret'] = self._secret
        return {'form_params': form_params}
