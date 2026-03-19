# Recurso: **Cópias**

> Neste recurso você poderá visualizar e manter todas as suas cópias processuais.
> Bastando somente informar o tribunal e numero do processo.

Todas as URIs são relativas a *https://app.intima.ai/api/v3*

## Exemplos

Para solicitar serviços referentes as cópias, você deve instanciar o tipo de serviço antes e inserir nas funções padrões dos serviços. Veja os serviços disponíveis para as cópias nos exemplos abaixo.

## **Busca**

> Obs: Lembre-se que é possível paginar ou aplicar filtros as buscas dos serviços.

### Geral

Exemplo para realizar uma busca geral de todas as cópias do usuário.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.copia.copia_busca import CopiaBusca

try:
    sdk = Intimai('api_token')

    # Se não for inserido nenhum id no serviço busca, ele irá retornar todos os registros daquele serviço
    copias = CopiaBusca()

    resultado = sdk.servicos.buscar(copias)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

### Específica

Exemplo para realizar uma busca específica de uma cópia do usuário.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.copia.copia_busca import CopiaBusca

try:
    sdk = Intimai('api_token')

    id_copia = 1  # ID da cópia no Intima.ai

    copia = CopiaBusca(id_copia)

    resultado = sdk.servicos.buscar(copia)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

## **Solicitação**

Exemplo para realizar a solicitação de uma cópia.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.solicitar.copia.copia_solicitacao import CopiaSolicitacao

try:
    sdk = Intimai('api_token')

    id_autenticador = 1                          # ID do autenticador no Intima.ai
    numero_do_processo = '00000000000000000000'  # Número do processo no tribunal

    copia = CopiaSolicitacao(id_autenticador, numero_do_processo)

    resultado = sdk.servicos.solicitar(copia)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

[Voltar ao topo](#recurso-cópias)
[Voltar a lista da API](../../README.md#recursos)
[Voltar para o README](../../README.md#intimaai---sdk-v3-python)
