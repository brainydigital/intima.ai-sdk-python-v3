# Recurso: **Créditos**

Todas as URIs são relativas a *https://app.intima.ai/api/v3*

## **Busca**

> Obs: Lembre-se que é possível paginar ou aplicar filtros as buscas dos serviços.

### Cotação

Exemplo para realizar a busca da cotação de créditos por ação.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.credito.credito_cotacao_busca import CreditoCotacaoBusca

try:
    sdk = Intimai('api_token')

    cotacao = CreditoCotacaoBusca()

    resultado = sdk.servicos.buscar(cotacao)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

### Histórico

Exemplo para realizar a busca do histórico de créditos do usuário.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.credito.credito_historico_busca import CreditoHistoricoBusca

try:
    sdk = Intimai('api_token')

    historico = CreditoHistoricoBusca()

    resultado = sdk.servicos.buscar(historico)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

### Saldo

Exemplo para realizar a busca do saldo de créditos do usuário.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.credito.credito_saldo_busca import CreditoSaldoBusca

try:
    sdk = Intimai('api_token')

    saldo = CreditoSaldoBusca()

    resultado = sdk.servicos.buscar(saldo)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

### Consumo mensal

Exemplo para buscar o consumo de créditos de um mês, agrupado por tipo de ação. O filtro `date` usa o formato `YYYY-MM`; sem ele, a API usa o mês atual.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.credito.credito_consumo_mensal_busca import CreditoConsumoMensalBusca

try:
    sdk = Intimai('api_token')

    resultado = sdk.servicos.buscar(CreditoConsumoMensalBusca(), 1, {'date': '2026-10'})

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.get_status(), e.get_mensagem())
```

[Voltar ao topo](#recurso-créditos)
[Voltar a lista da API](../../README.md#recursos)
[Voltar para o README](../../README.md#intimaai--sdk-v3-python)
