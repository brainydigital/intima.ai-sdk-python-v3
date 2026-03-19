# Recurso: **Ações**

> Todas as ações realizadas dentro do `Intima.ai`, ficam registradas neste recurso. Você pode
> buscar (todas ou uma ação específica), buscar o resultado ou tentar novamente.

Todas as URIs são relativas a *https://app.intima.ai/api/v3*

## **Busca**

> Obs: Lembre-se que é possível paginar ou aplicar filtros as buscas dos serviços.

### Geral

Exemplo para realizar uma busca geral de todas as ações do usuário.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.acao.acao_busca import AcaoBusca

try:
    sdk = Intimai('api_token')

    # Se não for inserido nenhum id no serviço busca, ele irá retornar todos os registros daquele serviço
    acoes = AcaoBusca()

    resultado = sdk.servicos.buscar(acoes)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

### Específica

Exemplo para realizar uma busca específica de uma ação do usuário.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.acao.acao_busca import AcaoBusca

try:
    sdk = Intimai('api_token')

    id_acao = 1  # ID da ação no Intima.ai

    acao = AcaoBusca(id_acao)

    resultado = sdk.servicos.buscar(acao)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

## **Resultado**

Exemplo para realizar a busca do resultado de uma ação.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.resultado.acao.acao_resultado import AcaoResultado

try:
    sdk = Intimai('api_token')

    id_acao = 1  # ID da ação no Intima.ai

    acao = AcaoResultado(id_acao)

    resultado = sdk.servicos.resultado(acao)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

## **Tentar Novamente**

Exemplo para tentar novamente uma ação que tenha falhado.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.tentar_novamente.acao.acao_tenta_novamente import AcaoTentaNovamente

try:
    sdk = Intimai('api_token')

    id_acao = 1  # ID da ação no Intima.ai

    acao = AcaoTentaNovamente(id_acao)

    resultado = sdk.servicos.tentar_novamente(acao)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

[Voltar ao topo](#recurso-ações)
[Voltar a lista da API](../../README.md#recursos)
[Voltar para o README](../../README.md#intimaai---sdk-v3-python)
