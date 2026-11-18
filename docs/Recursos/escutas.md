# Recurso: **Escutas**

> Com a escuta você pode saber todas as movimentações que ocorreram em um processo,
> e baixar todos os novos documentos anexados ao processo. Para realizá-la
> é bastante simples, bastando somente informar o numero do processo, tribunal e os dias/horários que
> deseja realizar.

Todas as URIs são relativas a *https://app.intima.ai/api/v3*

## **Busca**

> Obs: Lembre-se que é possível paginar ou aplicar filtros as buscas dos serviços.

### Geral

Exemplo para realizar uma busca geral de todas as escutas cadastradas do usuário.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.escuta.escuta_busca import EscutaBusca

try:
    sdk = Intimai('api_token')

    # Se não for inserido nenhum id no serviço busca, ele irá retornar todos os registros daquele serviço
    escutas = EscutaBusca()

    resultado = sdk.servicos.buscar(escutas)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

### Específica

Exemplo para realizar uma busca específica de uma escuta.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.escuta.escuta_busca import EscutaBusca

try:
    sdk = Intimai('api_token')

    id_escuta = 1  # ID da escuta no Intima.ai

    escuta = EscutaBusca(id_escuta)

    resultado = sdk.servicos.buscar(escuta)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

## **Cadastrar**

Exemplo para realizar o cadastro de uma escuta.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.cadastrar.escuta.escuta_cadastro import EscutaCadastro
from intimai.utilidades.dia import Dia
from intimai.utilidades.horario import Horario

try:
    sdk = Intimai('api_token')

    # ID do autenticador no Intima.ai
    id_autenticador = 1

    # Número do processo no tribunal
    numero_do_processo = '00000000000000000000'

    # Dias no qual a captura será realizada
    dias_de_captura = [
        Dia.SEGUNDA_FEIRA,
        Dia.SEXTA_FEIRA
    ]

    # Horários no qual a captura será realizada (no máximo 3)
    horarios_de_captura = [
        Horario.DEZ_HORAS,
        Horario.DEZOITO_HORAS
    ]

    escuta = EscutaCadastro(
        id_autenticador,
        numero_do_processo,
        dias_de_captura,
        horarios_de_captura
    )

    resultado = sdk.servicos.cadastrar(escuta)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

## **Atualizar**

Exemplo para realizar a atualização de uma escuta.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.atualizar.escuta.escuta_atualizacao import EscutaAtualizacao
from intimai.utilidades.dia import Dia
from intimai.utilidades.horario import Horario

try:
    sdk = Intimai('api_token')

    id_escuta = 1  # ID da escuta no Intima.ai

    # Dias no qual a captura será realizada
    dias_de_captura = [
        Dia.SEGUNDA_FEIRA,
        Dia.SEXTA_FEIRA
    ]

    # Horários no qual a captura será realizada (no máximo 3)
    horarios_de_captura = [
        Horario.DEZ_HORAS,
        Horario.DEZOITO_HORAS
    ]

    escuta = EscutaAtualizacao(id_escuta, dias_de_captura, horarios_de_captura)

    resultado = sdk.servicos.atualizar(escuta)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

## **Excluir**

Exemplo para realizar a exclusão de uma escuta.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.excluir.escuta.escuta_exclusao import EscutaExclusao

try:
    sdk = Intimai('api_token')

    id_escuta = 1  # ID da escuta no Intima.ai

    escuta = EscutaExclusao(id_escuta)

    resultado = sdk.servicos.excluir(escuta)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

[Voltar ao topo](#recurso-escutas)
[Voltar a lista da API](../../README.md#recursos)
[Voltar para o README](../../README.md#intimaai--sdk-v3-python)
