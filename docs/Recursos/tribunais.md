# Recurso: **Tribunais**

> Os tribunais correspondem a todos os sistemas jurídicos disponíveis no `Intima.ai`
> (PJE, ESAJ, PROJUDI, EPROC e etc).
>
> Para cada tribunal, você pode definir se deseja realizar as capturas de intimações
> (definir dias e horários do seu agrado) e associar uma `Autenticação`.
>
> A `Autenticação` pode ser um certificado A1 ou usuário/senha, mas sempre deve-se
> ficar atento as funcionalidades suportadas por cada tribunal.

Todas as URIs são relativas a *https://app.intima.ai/api/v3*

## Exemplos

Para solicitar serviços referentes aos tribunais, você deve instanciar o tipo de serviço antes e inserir nas funções padrões dos serviços. Veja os serviços disponíveis para o tribunal nos exemplos abaixo.

### **Busca**

> Obs: Lembre-se que é possível paginar ou aplicar filtros as buscas dos serviços.

#### Geral

Exemplo para realizar a busca geral de todos os tribunais disponíveis no `Intima.ai`.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.tribunal.tribunal_busca import TribunalBusca

try:
    sdk = Intimai('api_token')

    # Se não for inserido nenhum id no serviço busca, ele irá retornar todos os registros daquele serviço
    tribunais = TribunalBusca()

    resultado = sdk.servicos.buscar(tribunais)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

#### Específica

Exemplo para realizar a busca específica de um tribunal.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.tribunal.tribunal_busca import TribunalBusca

try:
    sdk = Intimai('api_token')

    id_tribunal = 1  # ID do tribunal no Intima.ai
    tribunal = TribunalBusca(id_tribunal)

    resultado = sdk.servicos.buscar(tribunal)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

[Voltar ao topo](#recurso-tribunais)
[Voltar a lista da API](../../README.md#recursos)
[Voltar para o README](../../README.md#intimaai---sdk-v3-python)
