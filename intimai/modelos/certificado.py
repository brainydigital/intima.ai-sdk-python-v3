class Certificado:
    def __init__(self, caminho_do_certificado: str, senha: str):
        self._caminho_do_certificado = caminho_do_certificado
        self._senha = senha

    def get_caminho_do_certificado(self) -> str:
        return self._caminho_do_certificado

    def get_senha(self) -> str:
        return self._senha

    def get_arquivo(self):
        try:
            return open(self._caminho_do_certificado, 'rb')
        except OSError:
            raise Exception('O caminho do arquivo informado é inválido!')

    def em_array(self) -> list:
        return [
            {'name': 'arquivo', 'contents': self.get_arquivo(), 'filename': self._caminho_do_certificado.split('/')[-1]},
            {'name': 'senha', 'contents': self._senha},
            {'name': 'senha_confirmation', 'contents': self._senha},
        ]
