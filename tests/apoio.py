import json
import os
import re
import tempfile
import unittest
from unittest import mock
from urllib.parse import parse_qsl, urlsplit

import requests

from intimai import Intimai


class Caso(unittest.TestCase):
    def criar(self, respostas=None, opcoes=None) -> Intimai:
        self.requisicoes = []
        self._pendentes = list(respostas or [])

        if not getattr(self, '_envio_simulado', False):
            self._simular_envio()
            self._envio_simulado = True

        return Intimai('token-teste', opcoes)

    def _simular_envio(self) -> None:
        def enviar(sessao, preparada, **kwargs):
            self.requisicoes.append(preparada)
            status, corpo, headers = self._pendentes.pop(0) if self._pendentes else (200, {'data': []}, {})
            resposta = requests.Response()
            resposta.status_code = status
            resposta.reason = 'Erro' if status >= 400 else 'OK'
            if isinstance(corpo, (dict, list)):
                resposta._content = json.dumps(corpo).encode()
            else:
                resposta._content = (corpo or '').encode()
            resposta.headers.update(headers)
            resposta.request = preparada
            resposta.url = preparada.url
            return resposta

        patcher = mock.patch.object(requests.Session, 'send', autospec=True, side_effect=enviar)
        patcher.start()
        self.addCleanup(patcher.stop)

    def requisicao(self, indice: int = -1):
        return self.requisicoes[indice]

    def caminho(self, indice: int = -1) -> str:
        return urlsplit(self.requisicao(indice).url).path

    def query(self, indice: int = -1) -> dict:
        return dict(parse_qsl(urlsplit(self.requisicao(indice).url).query, keep_blank_values=True))

    def corpo(self, indice: int = -1) -> list:
        corpo = self.requisicao(indice).body or ''
        if isinstance(corpo, bytes):
            corpo = corpo.decode()
        return parse_qsl(corpo, keep_blank_values=True)

    def campos(self, indice: int = -1) -> dict:
        corpo = self.requisicao(indice).body.decode()
        partes = re.findall(r'name="([^"]+)"(?:; filename="[^"]*")?\r\n(?:Content-[^\r]+\r\n)*\r\n(.*?)\r\n--', corpo, re.S)
        return dict(partes)

    def arquivo_temporario(self, conteudo: str) -> str:
        pasta = tempfile.mkdtemp()
        caminho = os.path.join(pasta, 'arquivo.pdf')
        with open(caminho, 'w') as arquivo:
            arquivo.write(conteudo)
        self.addCleanup(os.remove, caminho)
        return caminho
