class Peticao:
    def __init__(self, caminho: str, tipo: int | str = '', descricao: str = ''):
        self._caminho = caminho
        self._tipo = tipo
        self._descricao = descricao

    def get_caminho(self) -> str:
        return self._caminho

    def get_tipo(self) -> int | str:
        return self._tipo

    def get_descricao(self) -> str:
        return self._descricao

    def get_arquivo(self):
        try:
            return open(self._caminho, 'rb')
        except OSError:
            raise Exception('O caminho do arquivo informado é inválido!')

    def em_array(self) -> dict:
        return {
            'peticao[arquivo]': self.get_arquivo(),
            'peticao[tipo_documento]': self._tipo,
            'peticao[descricao_documento]': self._descricao,
        }
