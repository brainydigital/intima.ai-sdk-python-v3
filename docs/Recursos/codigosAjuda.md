# Recurso: **Códigos de Ajuda**

> Catálogo dos códigos de erro que uma ação pode retornar: o que cada um significa, se gera cobrança
> e se tem **nova tentativa automática**. É o mesmo conteúdo da página Códigos de Ajuda do painel.

Todas as URIs são relativas a *https://app.intima.ai/api/v3*

| Método | Rota                    |
| ------ | ----------------------- |
| GET    | `/codigo-ajuda/buscar`  |

## **Busca**

| Filtro   | Valores                                                                                   |
| -------- | ----------------------------------------------------------------------------------------- |
| `codigo` | Opcional. Filtra pelo código (ex.: `606`). Sem ele vem o catálogo inteiro. Código fora do catálogo retorna `404`. |

Resposta (`data`):

| Campo                  | Descrição                                                                                                      |
| ---------------------- | -------------------------------------------------------------------------------------------------------------- |
| `faixas`               | Faixas de cobrança (`total`, `parcial`, `isenta`) com a explicação e quantos códigos há em cada uma             |
| `nova_tentativa_aviso` | Regra geral: só os códigos com `nova_tentativa` preenchido são repetidos pela plataforma, em ações do mesmo dia |
| `grupos[].codigos[]`   | `codigo`, `mensagem`, `descricao`, `observacao`, `faixa`, `cobranca` e `nova_tentativa`                         |

`nova_tentativa` de cada código é o texto da regra (quantas vezes e de quanto em quanto tempo) ou `None` quando o código não tem nova tentativa automática.

### Catálogo inteiro

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.codigo_ajuda.codigo_ajuda_busca import CodigoAjudaBusca

try:
    sdk = Intimai('api_token')

    resultado = sdk.servicos.buscar(CodigoAjudaBusca())

    print(resultado['data']['grupos'])
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
```

### Um código

Antes de criar outra ação para um erro, confira se a plataforma já vai repetir a ação sozinha.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.codigo_ajuda.codigo_ajuda_busca import CodigoAjudaBusca

try:
    sdk = Intimai('api_token')

    resultado = sdk.servicos.buscar(CodigoAjudaBusca(), 1, {'codigo': 606})

    codigo = resultado['data']['grupos'][0]['codigos'][0]

    print(codigo['mensagem'], codigo['faixa'], codigo['nova_tentativa'])
except ExcecaoRequisicaoAPI as e:
    if e.get_status() == 404:
        pass  # código fora do catálogo

    print(e.get_mensagem())
```

[Voltar ao topo](#recurso-códigos-de-ajuda)
[Voltar a lista da API](../../README.md#recursos)
[Voltar para o README](../../README.md#intimaai--sdk-v3-python)
