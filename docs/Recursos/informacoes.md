# Recurso: **Informações**

> Com as informações, você poderá obter todas as informações do processo, tais como:
> valor da causa, classe judicial, assuntos, polos e etc.

Todas as URIs são relativas a *https://app.intima.ai/api/v3*

## Exemplos

Para solicitar serviços referentes as informações, você deve instanciar o tipo de serviço antes e inserir nas funções padrões dos serviços. Veja os serviços disponíveis para as informações nos exemplos abaixo.

## **Busca**

> Obs: Lembre-se que é possível paginar ou aplicar filtros as buscas dos serviços.

### Geral

Exemplo para realizar uma busca geral de todas as informações processuais do usuário.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.informacao.informacao_busca import InformacaoBusca

try:
    sdk = Intimai('api_token')

    # Se não for inserido nenhum id no serviço busca, ele irá retornar todos os registros daquele serviço
    informacoes = InformacaoBusca()

    resultado = sdk.servicos.buscar(informacoes)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

### Específica

Exemplo para realizar uma busca específica de uma informação processual.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.informacao.informacao_busca import InformacaoBusca

try:
    sdk = Intimai('api_token')

    id_informacao = 1  # ID da informação no Intima.ai

    informacao = InformacaoBusca(id_informacao)

    resultado = sdk.servicos.buscar(informacao)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

## **Solicitação**

Exemplo para realizar a solicitação de uma informação processual.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.solicitar.informacao.informacao_solicitacao import InformacaoSolicitacao

try:
    sdk = Intimai('api_token')

    id_autenticador = 1                          # ID do autenticador no Intima.ai
    numero_do_processo = '00000000000000000000'  # Número do processo no tribunal

    informacao = InformacaoSolicitacao(id_autenticador, numero_do_processo)

    resultado = sdk.servicos.solicitar(informacao)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

[Voltar ao topo](#recurso-informações)
[Voltar a lista da API](../../README.md#recursos)
[Voltar para o README](../../README.md#intimaai--sdk-v3-python)
