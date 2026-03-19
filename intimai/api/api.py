import requests
from intimai.excecoes.excecao_requisicao_api import ExcecaoRequisicaoAPI


class API:
    URL_BASE = 'https://app.intima.ai/api/v3'

    def __init__(self, api_token: str, opcoes: dict = None):
        self._api_token = api_token
        self._opcoes_api = opcoes or {}

    def _get_opcoes(self, pagina: int = 1, filtros: dict = None, request: dict = None) -> dict:
        filtros = filtros or {}
        request = request or {}

        opcoes_padrao = {
            'headers': {
                'Accept': 'application/json',
                'User-Agent': 'Intimai_SDK/3.0.0',
            },
            'params': {
                'api_token': self._api_token,
                'page': pagina,
            }
        }

        opcoes = {**opcoes_padrao, **self._opcoes_api}

        # Apply filters to params
        if filtros.get('filtros'):
            for chave, valor in filtros['filtros'].items():
                opcoes['params'][chave] = valor

        # Merge request options
        for key, value in request.items():
            if key == 'headers' and 'headers' in opcoes:
                opcoes['headers'].update(value)
            elif key == 'params' and 'params' in opcoes:
                opcoes['params'].update(value)
            else:
                opcoes[key] = value

        return opcoes

    def post(self, endpoint: str, request: dict = None) -> dict:
        try:
            opcoes = self._get_opcoes(request=request or {})
            url = self.URL_BASE + endpoint

            headers = opcoes.pop('headers', {})
            params = opcoes.pop('params', {})

            # Handle form_params (data)
            data = opcoes.pop('form_params', None)
            # Handle multipart
            files = None
            multipart = opcoes.pop('multipart', None)
            if multipart:
                files = {}
                data = {}
                for item in multipart:
                    name = item['name']
                    contents = item['contents']
                    filename = item.get('filename')
                    if hasattr(contents, 'read') or filename:
                        files[name] = (filename, contents) if filename else contents
                    else:
                        data[name] = contents
                if not files:
                    files = None
                # When sending multipart, don't set Content-Type (requests handles it)
                headers.pop('Content-Type', None)

            response = requests.post(url, headers=headers, params=params, data=data, files=files)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as e:
            raise ExcecaoRequisicaoAPI(str(e), e.response.status_code if e.response else 0) from e

    def get(self, endpoint: str, pagina: int = 1, filtros: dict = None, request: dict = None) -> dict:
        try:
            opcoes = self._get_opcoes(pagina, filtros or {}, request or {})
            url = self.URL_BASE + endpoint

            headers = opcoes.pop('headers', {})
            params = opcoes.pop('params', {})

            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as e:
            raise ExcecaoRequisicaoAPI(str(e), e.response.status_code if e.response else 0) from e

    def put(self, endpoint: str, request: dict = None) -> dict:
        try:
            opcoes = self._get_opcoes(request=request or {})
            url = self.URL_BASE + endpoint

            headers = opcoes.pop('headers', {})
            params = opcoes.pop('params', {})
            data = opcoes.pop('form_params', None)

            response = requests.put(url, headers=headers, params=params, data=data)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as e:
            raise ExcecaoRequisicaoAPI(str(e), e.response.status_code if e.response else 0) from e

    def delete(self, endpoint: str) -> dict:
        try:
            opcoes = self._get_opcoes()
            url = self.URL_BASE + endpoint

            headers = opcoes.pop('headers', {})
            params = opcoes.pop('params', {})

            response = requests.delete(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as e:
            raise ExcecaoRequisicaoAPI(str(e), e.response.status_code if e.response else 0) from e
