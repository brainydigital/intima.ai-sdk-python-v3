class Documento:
    def __init__(self, caminho: str, ordem: int, tipo: int | str = '', descricao: str = ''):
        self._caminho = caminho
        self._tipo = tipo
        self._descricao = descricao
        self._ordem = ordem

    def get_caminho(self) -> str:
        return self._caminho

    def get_tipo(self) -> int | str:
        return self._tipo

    def get_descricao(self) -> str:
        return self._descricao

    def get_ordem(self) -> int:
        return self._ordem

    def get_arquivo(self):
        try:
            return open(self._caminho, 'rb')
        except OSError:
            raise Exception('O caminho do arquivo informado é inválido!')

    def em_array(self) -> dict:
        index = self._ordem - 1
        return {
            f'documentos[{index}][arquivo]': self.get_arquivo(),
            f'documentos[{index}][tipo_documento]': self._tipo,
            f'documentos[{index}][descricao_documento]': self._descricao,
            f'documentos[{index}][ordem]': self._ordem,
        }
