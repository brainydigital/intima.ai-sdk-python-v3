# Recurso: **Consultas**

> Com este recurso você poderá realizar consultas de todos os processos disponíveis em qualquer
> tribunal do Brasil. Bastando apenas informar o `numero do processo` ou o `nome da parte` ou o `nome do
> representante`.
>
> O `Intima.ai` recomenda que antes de realizar qualquer consulta processual, primeiro solicite
> a `pré-analise da consulta`, pois dependendo dos termos utilizados na consulta,
> poderá haver um numero muito alto de registros encontrados, consumindo assim seus créditos.
>
> A `pré-analise de uma consulta` retorna a quantidade de registros encontrados com os
> termos de busca informados.
>
> Ao solicitar uma consulta por perfil, a API faz a pré-análise sozinha. Se houver processos, a
> consulta para em `StatusAcao.AGUARDANDO_CONFIRMACAO` (13) e só segue depois de confirmada
> (veja [Confirmar ou cancelar consulta](acoes.md#confirmar-ou-cancelar-consulta)). Sem
> confirmação em 1 hora, a consulta expira.
>
> A OAB vai como dicionário: `oab={'numero': '123', 'letra': 'A', 'uf': 'RJ'}`.
>
> No EPROC, informe só um parâmetro de busca: número do processo **ou** documento da parte
> **ou** OAB. Nome da parte e nome do representante ainda não são aceitos nesse sistema.

Todas as URIs são relativas a *https://app.intima.ai/api/v3*

## **Busca**

> Obs: Lembre-se que é possível paginar ou aplicar filtros as buscas dos serviços.

### Geral

Exemplo para realizar uma busca geral de todas as consultas do usuário.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.consulta.consulta_busca import ConsultaBusca

try:
    sdk = Intimai('api_token')

    # Se não for inserido nenhum id no serviço busca, ele irá retornar todos os registros daquele serviço
    consultas = ConsultaBusca()

    resultado = sdk.servicos.buscar(consultas)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

### Específica

Exemplo para realizar uma busca específica de uma consulta do usuário.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.consulta.consulta_busca import ConsultaBusca

try:
    sdk = Intimai('api_token')

    id_consulta = 1  # ID da consulta no Intima.ai

    consulta = ConsultaBusca(id_consulta)

    resultado = sdk.servicos.buscar(consulta)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

## **Solicitar**

Exemplo para realizar a solicitação de uma consulta.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.solicitar.consulta.consulta_solicitacao import ConsultaSolicitacao

try:
    sdk = Intimai('api_token')

    id_autenticador = 1                          # ID do autenticador no Intima.ai
    numero_do_processo = '00000000000000000000'  # Número do processo no tribunal
    # OU nome do representante >> nome_representante = 'nome-representante'

    consulta = ConsultaSolicitacao(id_autenticador, numero_do_processo)

    resultado = sdk.servicos.solicitar(consulta)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

## **Resultado**

Exemplo para realizar a busca do resultado de uma consulta.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.resultado.consulta.consulta_resultado import ConsultaResultado

try:
    sdk = Intimai('api_token')

    id_consulta = 1  # ID da consulta no Intima.ai

    consulta = ConsultaResultado(id_consulta)

    resultado = sdk.servicos.resultado(consulta)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

[Voltar ao topo](#recurso-consultas)
[Voltar a lista da API](../../README.md#recursos)
[Voltar para o README](../../README.md#intimaai--sdk-v3-python)
