# Recurso: **Protocolos**

> Você pode realizar protocolos em quase todos os tribunais disponíveis no Brasil. De
> forma rápida e segura, sem se preocupar com tamanho dos arquivos em PDF (nos ajustamos e
> recortamos automaticamente, de acordo com tribunal selecionado).
>
> Para os `protocolos no PJE ou PROJUDI`, tudo é realizado em apenas uma `única etapa`, já para os `protocolos no
> ESAJ, EPROC e TJRJ`, são necessárias `duas etapas` para conclusão do mesmo.

Todas as URIs são relativas a *https://app.intima.ai/api/v3*

## Exemplos

Para solicitar serviços referentes aos protocolos, você deve instanciar o tipo de serviço antes e inserir nas funções padrões dos serviços. Veja os serviços disponíveis para os protocolos nos exemplos abaixo.

## **Busca**

> Obs: Lembre-se que é possível paginar ou aplicar filtros as buscas dos serviços.

### Geral

Exemplo para realizar uma busca geral de todos os protocolos do usuário.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.protocolo.protocolo_busca import ProtocoloBusca

try:
    sdk = Intimai('api_token')

    # Se não for inserido nenhum id no serviço busca, ele irá retornar todos os registros daquele serviço
    protocolos = ProtocoloBusca()

    resultado = sdk.servicos.buscar(protocolos)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

### Específica

Exemplo para realizar uma busca específica de um protocolo.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.protocolo.protocolo_busca import ProtocoloBusca

try:
    sdk = Intimai('api_token')

    id_protocolo = 1  # ID do protocolo no Intima.ai

    protocolo = ProtocoloBusca(id_protocolo)

    resultado = sdk.servicos.buscar(protocolo)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

## **Solicitação**

### PJE

Protocolos no sistema PJE são realizados em uma única etapa.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.modelos.peticao import Peticao
from intimai.modelos.documento import Documento
from intimai.servicos.solicitar.protocolo.pje.protocolo_pje_solicitacao import ProtocoloPjeSolicitacao

try:
    sdk = Intimai('api_token')

    id_autenticador = 1                          # ID do autenticador no Intima.ai
    numero_do_processo = '00000000000000000000'  # Número do processo no tribunal

    # Estes tipos estão disponíveis no tribunal em questão, você pode buscar o tribunal e verificar os valores disponíveis.
    tipo_documento_mensagem_geral = 1

    # A petição é obrigatória nos tribunais da Justiça do Trabalho (TRT) e proibida nos demais: fora do TRT, passe None e envie tudo em documentos.
    peticao = Peticao('caminho/da/peticao', 12, 'descricao-peticao')

    documentos = [
        Documento('caminho/do/documento', 1, 21, 'descricao-doc')
    ]

    # Obs: fora do TRT, use None no lugar de peticao
    protocolo = ProtocoloPjeSolicitacao(
        id_autenticador,
        numero_do_processo,
        tipo_documento_mensagem_geral,
        peticao,
        documentos,
    )

    resultado = sdk.servicos.solicitar(protocolo)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

### PROJUDI

Protocolos no sistema PROJUDI são realizados em uma única etapa.

Antes de protocolar, busque os tipos de documento mensagem geral disponíveis para o autenticador. A API responde 422 se o autenticador não for do PROJUDI e 404 se o tribunal não tiver nenhum tipo.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.protocolo.tipo_documento_mensagem_geral.tipo_documento_mensagem_geral_projudi_busca import TipoDocumentoMensagemGeralProjudiBusca

try:
    sdk = Intimai('api_token')

    id_autenticador = 1  # ID do autenticador no Intima.ai

    resultado = sdk.servicos.buscar(TipoDocumentoMensagemGeralProjudiBusca(id_autenticador))

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.get_status(), e.get_mensagem())
```

Depois, solicite o protocolo:

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.modelos.documento import Documento
from intimai.servicos.solicitar.protocolo.projudi.protocolo_projudi_solicitacao import ProtocoloProjudiSolicitacao

try:
    sdk = Intimai('api_token')

    id_autenticador = 1                          # ID do autenticador no Intima.ai
    numero_do_processo = '00000000000000000000'  # Número do processo no tribunal

    # Um dos tipos devolvidos por TipoDocumentoMensagemGeralProjudiBusca
    tipo_documento_mensagem_geral = 1

    documentos = [
        Documento('caminho/do/documento', 1, 21, 'descricao-doc')
    ]

    protocolo = ProtocoloProjudiSolicitacao(
        id_autenticador,
        numero_do_processo,
        tipo_documento_mensagem_geral,
        documentos,
    )

    resultado = sdk.servicos.solicitar(protocolo)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

### ESAJ

Protocolos no sistema ESAJ são realizados em duas etapas.

#### Primeira Etapa

Para realizar a primeira etapa do protocolo no sistema ESAJ, basta informar o número do processo e
o id do autenticador (contendo o tribunal referente ao número do processo).

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.solicitar.protocolo.esaj.protocolo_esaj_primeiro_passo_solicitacao import ProtocoloEsajPrimeiroPassoSolicitacao

try:
    sdk = Intimai('api_token')

    id_autenticador = 1                          # ID do autenticador no Intima.ai
    numero_do_processo = '00000000000000000000'  # Número do processo no tribunal

    primeira_etapa = ProtocoloEsajPrimeiroPassoSolicitacao(id_autenticador, numero_do_processo)

    resultado = sdk.servicos.solicitar(primeira_etapa)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

#### Segunda Etapa

Após a finalização da primeira etapa, você terá que informar todas as informações principais do protocolo.

Após a finalização da segunda etapa, a ação do protocolo estará finalizada e você poderá ver a certidão do protocolo que contém todas as informações do protocolo e serve como comprovante de protocolo.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.modelos.parte_vinculada import ParteVinculada
from intimai.modelos.peticao import Peticao
from intimai.modelos.documento import Documento
from intimai.servicos.solicitar.protocolo.esaj.protocolo_esaj_segundo_passo_solicitacao import ProtocoloEsajSegundoPassoSolicitacao

try:
    sdk = Intimai('api_token')

    id_protocolo = 1  # ID do protocolo no Intima.ai

    # O id da classe pode ser obtido verificando as classes disponíveis ao buscar todas as classes
    id_classe = 1

    # O id da categoria pode ser obtido verificando as classes e categorias disponíveis ao buscar todas as classes
    id_categoria = 1

    # Array com as partes. Obs: a parte pode ter participação, verifique no tribunal
    partes_vinculadas = [
        ParteVinculada('nome-parte')
    ]

    peticao = Peticao('caminho/da/peticao', 12, 'descricao-peticao')

    documentos = [
        Documento('caminho/do/documento', 1, 21, 'descricao-doc')
    ]

    segunda_etapa = ProtocoloEsajSegundoPassoSolicitacao(
        id_protocolo,
        id_classe,
        id_categoria,
        partes_vinculadas,
        peticao,
        documentos
    )

    resultado = sdk.servicos.solicitar(segunda_etapa)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

### EPROC

Protocolos no sistema EPROC são realizados em duas etapas.

#### Primeira Etapa

Para realizar a primeira etapa do protocolo no sistema EPROC, basta informar o número do processo e
o id do autenticador (contendo o tribunal referente ao número do processo).

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.solicitar.protocolo.eproc.protocolo_eproc_primeiro_passo_solicitacao import ProtocoloEprocPrimeiroPassoSolicitacao

try:
    sdk = Intimai('api_token')

    id_autenticador = 1                          # ID do autenticador no Intima.ai
    numero_do_processo = '00000000000000000000'  # Número do processo no tribunal

    primeira_etapa = ProtocoloEprocPrimeiroPassoSolicitacao(id_autenticador, numero_do_processo)

    resultado = sdk.servicos.solicitar(primeira_etapa)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

#### Segunda Etapa

Após a finalização da primeira etapa, você terá que informar todas as informações principais do protocolo.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.modelos.parte_vinculada import ParteVinculada
from intimai.modelos.documento import Documento
from intimai.servicos.solicitar.protocolo.eproc.protocolo_eproc_segundo_passo_solicitacao import ProtocoloEprocSegundoPassoSolicitacao

try:
    sdk = Intimai('api_token')

    id_protocolo = 1  # ID do protocolo no Intima.ai

    # Estes tipos estão disponíveis no protocolo, você pode buscar o protocolo e verificar os valores disponíveis.
    tipo_documento_mensagem_geral = 1

    # Array com as partes. Obs: a parte pode ter participação, verifique no tribunal
    partes_vinculadas = [
        ParteVinculada('nome-parte')
    ]

    documentos = [
        Documento('caminho/do/documento', 1, 21, 'descricao-doc')
    ]

    segunda_etapa = ProtocoloEprocSegundoPassoSolicitacao(
        id_protocolo,
        tipo_documento_mensagem_geral,
        partes_vinculadas,
        documentos
    )

    resultado = sdk.servicos.solicitar(segunda_etapa)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

### TJRJ

Protocolos no sistema TJRJ são realizados em duas etapas.

#### Primeira Etapa

Para realizar a primeira etapa do protocolo no sistema TJRJ, basta informar o número do processo e
o id do autenticador (contendo o tribunal referente ao número do processo).

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.solicitar.protocolo.tjrj.protocolo_tjrj_primeiro_passo_solicitacao import ProtocoloTjrjPrimeiroPassoSolicitacao

try:
    sdk = Intimai('api_token')

    id_autenticador = 1                          # ID do autenticador no Intima.ai
    numero_do_processo = '00000000000000000000'  # Número do processo no tribunal

    primeira_etapa = ProtocoloTjrjPrimeiroPassoSolicitacao(id_autenticador, numero_do_processo)

    resultado = sdk.servicos.solicitar(primeira_etapa)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

#### Segunda Etapa

Após a finalização da primeira etapa, você terá que informar todas as informações principais do protocolo.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.modelos.parte_vinculada import ParteVinculada
from intimai.modelos.peticao import Peticao
from intimai.modelos.documento import Documento
from intimai.servicos.solicitar.protocolo.tjrj.protocolo_tjrj_segundo_passo_solicitacao import ProtocoloTjrjSegundoPassoSolicitacao

try:
    sdk = Intimai('api_token')

    id_protocolo = 1  # ID do protocolo no Intima.ai

    # O id da classe pode ser obtido verificando as classes disponíveis ao buscar todas as classes
    id_classe = 1

    # Array com as partes. Obs: a parte pode ter participação, verifique no tribunal
    partes_vinculadas = [
        ParteVinculada('nome-parte')
    ]

    peticao = Peticao('caminho/da/peticao', 12, 'descricao-peticao')

    documentos = [
        Documento('caminho/do/documento', 1, 21, 'descricao-doc')
    ]

    # Obrigatório quando a classe escolhida tem categorias (veja as classes do protocolo)
    id_categoria = None

    segunda_etapa = ProtocoloTjrjSegundoPassoSolicitacao(
        id_protocolo,
        id_classe,
        partes_vinculadas,
        peticao,
        documentos,
        id_categoria
    )

    resultado = sdk.servicos.solicitar(segunda_etapa)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

[Voltar ao topo](#recurso-protocolos)
[Voltar a lista da API](../../README.md#recursos)
[Voltar para o README](../../README.md#intimaai--sdk-v3-python)
