# Recurso: **Protocolos De Habilitação**

> Assim como os protocolos, você pode realizar protocolos de habilitação em quase todos os tribunais
> disponíveis no Brasil. Sem se preocupar com tamanho dos arquivos em PDF (nos ajustamos e
> recortamos automaticamente, de acordo com tribunal selecionado).
>
> O protocolo habilitação é realizado em duas etapas:
>
> - Primeira etapa: Coleta de informações do processo no qual se deseja solicitar habilitação.
> - Segunda etapa: Realização do protocolo, a partir das informações coletadas na etapa anterior.

Todas as URIs são relativas a *https://app.intima.ai/api/v3*

## Exemplos

Para solicitar serviços referentes aos protocolos de habilitação, você deve instanciar o tipo de serviço antes e inserir nas funções padrões dos serviços. Veja os serviços disponíveis para os protocolos de habilitação nos exemplos abaixo.

## **Busca**

> Obs: Lembre-se que é possível paginar ou aplicar filtros as buscas dos serviços.

### Geral

Exemplo para realizar uma busca geral de todos os protocolos de habilitação do usuário.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.protocolo_habilitacao.protocolo_habilitacao_busca import ProtocoloHabilitacaoBusca

try:
    sdk = Intimai('api_token')

    # Se não for inserido nenhum id no serviço busca, ele irá retornar todos os registros daquele serviço
    protocolos_habilitacao = ProtocoloHabilitacaoBusca()

    resultado = sdk.servicos.buscar(protocolos_habilitacao)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

### Específica

Exemplo para realizar uma busca específica de um protocolo de habilitação.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.protocolo_habilitacao.protocolo_habilitacao_busca import ProtocoloHabilitacaoBusca

try:
    sdk = Intimai('api_token')

    id_protocolo_habilitacao = 1  # ID do protocolo habilitação no Intima.ai

    protocolo_habilitacao = ProtocoloHabilitacaoBusca(id_protocolo_habilitacao)

    resultado = sdk.servicos.buscar(protocolo_habilitacao)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

## **Solicitação**

### Primeira etapa

Para realizar a primeira etapa do protocolo de habilitação, basta informar o número do processo e
o id do autenticador (contendo o tribunal referente ao número do processo).

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.solicitar.protocolo_habilitacao.pje.protocolo_habilitacao_pje_primeiro_passo_solicitacao import ProtocoloHabilitacaoPjePrimeiroPassoSolicitacao

try:
    sdk = Intimai('api_token')

    id_autenticador = 1                          # ID do autenticador no Intima.ai
    numero_do_processo = '00000000000000000000'  # Número do processo no tribunal

    primeira_etapa = ProtocoloHabilitacaoPjePrimeiroPassoSolicitacao(id_autenticador, numero_do_processo)

    resultado = sdk.servicos.solicitar(primeira_etapa)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

### Segunda etapa

Após a finalização da primeira etapa, você terá que informar todas as informações principais do protocolo de habilitação.

Após a finalização da segunda etapa, a ação do protocolo de habilitação estará finalizada e você poderá ver a certidão do protocolo que contém todas as informações do protocolo e serve como comprovante de protocolo.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.utilidades.tipo_solicitacao import TipoSolicitacao
from intimai.utilidades.tipo_declaracao import TipoDeclaracao
from intimai.utilidades.polo import Polo
from intimai.modelos.parte_vinculada import ParteVinculada
from intimai.modelos.documento import Documento
from intimai.servicos.solicitar.protocolo_habilitacao.pje.protocolo_habilitacao_pje_segundo_passo_solicitacao import ProtocoloHabilitacaoPjeSegundoPassoSolicitacao

try:
    sdk = Intimai('api_token')

    id_protocolo_habilitacao = 1  # ID do protocolo habilitação no Intima.ai

    # Estes tipos estão disponíveis na classe TipoSolicitacao
    tipo_solicitacao = TipoSolicitacao.HABILITACAO_SIMPLES

    # Estes tipos estão disponíveis na classe TipoDeclaracao
    tipo_declaracao = TipoDeclaracao.DECLARACAO_SOB_PENA_DE_LEI

    # Estes polos estão disponíveis na classe Polo
    polo = Polo.ATIVO

    # Array com as partes. Obs: a parte pode ter participação, verifique no tribunal
    partes_vinculadas = [
        ParteVinculada('nome-parte')
    ]

    # Estes tipos estão disponíveis no protocolo, você pode buscar o protocolo e verificar os valores disponíveis.
    tipo_documento_mensagem_geral = 1

    documentos = [
        Documento('caminho/do/documento', 1, 21, 'descricao-doc')
    ]

    segunda_etapa = ProtocoloHabilitacaoPjeSegundoPassoSolicitacao(
        id_protocolo_habilitacao,
        tipo_solicitacao,
        tipo_declaracao,
        polo,
        partes_vinculadas,
        tipo_documento_mensagem_geral,
        documentos
    )

    resultado = sdk.servicos.solicitar(segunda_etapa)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

[Voltar ao topo](#recurso-protocolos-de-habilitação)
[Voltar a lista da API](../../README.md#recursos)
[Voltar para o README](../../README.md#intimaai---sdk-v3-python)
