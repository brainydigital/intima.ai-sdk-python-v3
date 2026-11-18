from intimai.modelos.peticao import Peticao


class HelpersMixin:
    def _definir_partes(self, partes: list, parametros: dict) -> None:
        for chave, parte_vinculada in enumerate(partes):
            parametros[f'partes_vinculadas[{chave}][nome]'] = parte_vinculada.get_nome()
            if parte_vinculada.get_participacao():
                parametros[f'partes_vinculadas[{chave}][participacao]'] = parte_vinculada.get_participacao()

    def _definir_peticao(self, peticao: Peticao | None, parametros: dict) -> None:
        if peticao is not None:
            parametros_peticao = peticao.em_array()
            parametros.update(parametros_peticao)

    def _definir_documentos(self, documentos: list, parametros: dict) -> None:
        if documentos:
            for documento in documentos:
                parametros_documento = documento.em_array()
                parametros.update(parametros_documento)

    def _definir_multipart(self, parametros: dict) -> list:
        multipart = []
        for nome, conteudo in parametros.items():
            multipart.append({'name': nome, 'contents': conteudo})
        return multipart
