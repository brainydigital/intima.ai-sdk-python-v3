import os

import requests
from intimai.excecoes.excecao_requisicao_api import ExcecaoRequisicaoAPI


class API:
    URL_BASE = 'https://app.intima.ai/api/v3'
    USER_AGENT = 'Intimai_SDK/3.1.0'
    HEADER_CODIGO_2FA = 'X-Codigo-2FA'

    def __init__(self, api_token: str, opcoes: dict = None):
        opcoes = dict(opcoes or {})
        self._api_token = api_token
        self._codigo_2fa = opcoes.pop('codigo_2fa', None)
        self._opcoes_api = opcoes

    def definir_codigo_2fa(self, codigo) -> None:
        self._codigo_2fa = codigo

    @staticmethod
    def formulario(dados: dict) -> list:
        pares = []

        def adicionar(chave, valor):
            if valor is None:
                return
            if isinstance(valor, (list, tuple)):
                for indice, item in enumerate(valor):
                    adicionar(f'{chave}[{indice}]', item)
            elif isinstance(valor, dict):
                for subchave, item in valor.items():
                    adicionar(f'{chave}[{subchave}]', item)
            elif isinstance(valor, bool):
                pares.append((chave, '1' if valor else '0'))
            else:
                pares.append((chave, str(valor)))

        for chave, valor in dados.items():
            adicionar(chave, valor)

        return pares

    @staticmethod
    def _multipart(campos: list) -> list:
        partes = []

        for campo in campos:
            conteudo = campo['contents']

            if conteudo is None:
                continue

            if hasattr(conteudo, 'read'):
                nome = campo.get('filename') or os.path.basename(getattr(conteudo, 'name', 'arquivo'))
                with conteudo:
                    partes.append((campo['name'], (nome, conteudo.read())))
            else:
                partes.append((campo['name'], (None, str(conteudo))))

        return partes

    def _get_opcoes(self, pagina: int = 1, filtros: dict = None, request: dict = None) -> dict:
        filtros = filtros or {}
        request = request or {}
        opcoes = dict(self._opcoes_api)

        headers = {
            'Accept': 'application/json',
            'User-Agent': self.USER_AGENT,
        }

        codigo = self._codigo_2fa() if callable(self._codigo_2fa) else self._codigo_2fa

        if codigo is not None and codigo != '':
            headers[self.HEADER_CODIGO_2FA] = str(codigo)

        headers.update(opcoes.pop('headers', None) or {})
        headers.update(request.get('headers') or {})

        params = {'api_token': self._api_token, 'page': pagina}
        params.update(opcoes.pop('params', None) or {})
        params.update(request.get('params') or {})
        params.update(filtros['filtros'] if 'filtros' in filtros else filtros)

        return {**opcoes, 'headers': headers, 'params': params}

    def _corpo(self, request: dict) -> dict:
        if request.get('multipart'):
            return {'files': self._multipart(request['multipart'])}

        if request.get('form_params') is not None:
            return {'data': self.formulario(request['form_params'])}

        return {}

    def _requisitar(self, metodo: str, endpoint: str, opcoes: dict, corpo: dict = None) -> dict:
        resposta = requests.request(metodo, self.URL_BASE + endpoint, **opcoes, **(corpo or {}))

        if resposta.status_code >= 400:
            raise ExcecaoRequisicaoAPI.da_resposta(resposta)

        if not resposta.content:
            return {}

        return resposta.json()

    def post(self, endpoint: str, request: dict = None) -> dict:
        request = request or {}
        corpo = self._corpo(request)
        return self._requisitar('POST', endpoint, self._get_opcoes(request=request), corpo)

    def get(self, endpoint: str, pagina: int = 1, filtros: dict = None, request: dict = None) -> dict:
        return self._requisitar('GET', endpoint, self._get_opcoes(pagina, filtros, request))

    def put(self, endpoint: str, request: dict = None) -> dict:
        request = request or {}
        corpo = self._corpo(request)
        return self._requisitar('PUT', endpoint, self._get_opcoes(request=request), corpo)

    def delete(self, endpoint: str) -> dict:
        return self._requisitar('DELETE', endpoint, self._get_opcoes())
