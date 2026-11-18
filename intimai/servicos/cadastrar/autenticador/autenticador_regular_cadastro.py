from intimai.servicos.cadastrar.servico_cadastro import ServicoCadastro
from intimai.servicos.endpoint import EndpointMixin


class AutenticadorRegularCadastro(ServicoCadastro, EndpointMixin):
    def __init__(
        self,
        id_tribunal: int | str | list,
        oab: dict,
        usuario: str,
        senha: str,
        id_certificado: int | str = None,
        usuario_sigla: str = None,
        usuario_descricao: str = None,
        secret: str = None,
    ):
        self._id_tribunal = id_tribunal
        self._oab = oab
        self._usuario = usuario
        self._senha = senha
        self._id_certificado = id_certificado
        self._usuario_sigla = usuario_sigla
        self._usuario_descricao = usuario_descricao
        self._secret = secret

    def get_endpoint(self) -> str:
        return f'{self.AUTENTICADOR_ENDPOINT}{self.REGULAR_ENDPOINT}{self.CADASTRAR_ENDPOINT}'

    def get_request(self) -> dict:
        form_params = {
            'tribunal_id': self._id_tribunal,
            'oab_numero': self._oab.get('numero'),
            'oab_uf': self._oab.get('uf'),
            'usuario': self._usuario,
            'senha': self._senha,
        }
        if self._oab.get('letra'):
            form_params['oab_letra'] = self._oab['letra']
        form_params['certificado_id'] = self._id_certificado
        form_params['usuario_sigla'] = self._usuario_sigla
        form_params['usuario_descricao'] = self._usuario_descricao
        form_params['secret'] = self._secret
        return {'form_params': form_params}
