# Recurso: **Transações**

Todas as URIs são relativas a *https://app.intima.ai/api/v3*

## **Busca**

> Obs: Lembre-se que é possível paginar ou aplicar filtros as buscas dos serviços.

### Histórico

Exemplo para realizar a busca do histórico de transações do usuário.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.transacao.transacao_historico_busca import TransacaoHistoricoBusca

try:
    sdk = Intimai('api_token')

    historico = TransacaoHistoricoBusca()

    resultado = sdk.servicos.buscar(historico)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

[Voltar ao topo](#recurso-transações)
[Voltar a lista da API](../../README.md#recursos)
[Voltar para o README](../../README.md#intimaai--sdk-v3-python)
