# Recurso: **Andamentos**

> Com os Andamentos, você poderá visualizar todas as movimentações e documentos
> (PDF e HTML) do polo interno de um processo.

Todas as URIs são relativas a *https://app.intima.ai/api/v3*

## **Busca**

> Obs: Lembre-se que é possível paginar ou aplicar filtros as buscas dos serviços.

### Geral

Exemplo para realizar uma busca geral de todos os andamentos cadastrados do usuário.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.andamento.andamento_busca import AndamentoBusca

try:
    sdk = Intimai('api_token')

    # Se não for inserido nenhum id no serviço busca, ele irá retornar todos os registros daquele serviço
    andamentos = AndamentoBusca()

    resultado = sdk.servicos.buscar(andamentos)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

### Específica

Exemplo para realizar uma busca específica de um andamento cadastrado do usuário.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.andamento.andamento_busca import AndamentoBusca

try:
    sdk = Intimai('api_token')

    id_andamento = 1  # ID do andamento no Intima.ai

    andamento = AndamentoBusca(id_andamento)

    resultado = sdk.servicos.buscar(andamento)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

## **Cadastrar**

Exemplo para realizar o cadastro de um andamento.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.cadastrar.andamento.andamento_cadastro import AndamentoCadastro

try:
    sdk = Intimai('api_token')

    id_autenticador = 1                          # ID do autenticador no Intima.ai
    numero_do_processo = '00000000000000000000'  # Número do processo no tribunal

    andamento = AndamentoCadastro(id_autenticador, numero_do_processo)

    resultado = sdk.servicos.cadastrar(andamento)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

## **Solicitar**

Exemplo para realizar a captura de um andamento.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.solicitar.andamento.andamento_solicitacao import AndamentoSolicitacao

try:
    sdk = Intimai('api_token')

    id_andamento = 1  # ID do andamento no Intima.ai

    andamento = AndamentoSolicitacao(id_andamento)

    resultado = sdk.servicos.solicitar(andamento)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

## **Excluir**

Exemplo para realizar a exclusão de um andamento.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.excluir.andamento.andamento_exclusao import AndamentoExclusao

try:
    sdk = Intimai('api_token')

    id_andamento = 1  # ID do andamento no Intima.ai

    andamento = AndamentoExclusao(id_andamento)

    resultado = sdk.servicos.excluir(andamento)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

[Voltar ao topo](#recurso-andamentos)
[Voltar a lista da API](../../README.md#recursos)
[Voltar para o README](../../README.md#intimaai--sdk-v3-python)
