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

## **Nova tentativa automática**

A ação com erro (`StatusAcao.ERRO`) traz o bloco `nova_tentativa`; nos outros status ele vem `None`. Use-o antes de criar outra ação: se `automatica` for `True`, a plataforma repete a ação sozinha e não é preciso criar outra. As regras de cada código estão no recurso [Códigos de Ajuda](codigosAjuda.md#recurso-códigos-de-ajuda).

| Campo            | Descrição                                                                                     |
| ---------------- | --------------------------------------------------------------------------------------------- |
| `automatica`     | `True` quando a plataforma ainda vai repetir a ação                                            |
| `situacao`       | `SituacaoNovaTentativa.AGENDADA`, `AGUARDANDO_CONDICAO`, `ENCERRADA` ou `SEM_NOVA_TENTATIVA`  |
| `tentativa`      | Número da próxima tentativa (quando agendada)                                                  |
| `max_tentativas` | Total de tentativas da regra                                                                   |
| `prevista_para`  | Data e hora previstas da próxima tentativa                                                     |
| `mensagem`       | Texto pronto para mostrar ao usuário                                                           |

```python
from intimai import Intimai, ExcecaoRequisicaoAPI, SituacaoNovaTentativa
from intimai.servicos.buscar.acao.acao_busca import AcaoBusca

try:
    sdk = Intimai('api_token')

    nova_tentativa = sdk.servicos.buscar(AcaoBusca(1))['data']['nova_tentativa']

    if nova_tentativa is None:
        pass  # A ação não está com erro
    elif nova_tentativa['automatica']:
        print(nova_tentativa['mensagem'])  # A plataforma vai repetir sozinha: não crie outra ação
    elif nova_tentativa['situacao'] == SituacaoNovaTentativa.SEM_NOVA_TENTATIVA:
        pass  # Corrija a causa do erro antes de criar outra ação
except ExcecaoRequisicaoAPI as e:
    print(e.get_status(), e.get_mensagem())
```

## **Confirmar ou cancelar consulta**

Toda consulta processual por perfil passa por uma pré-análise. Quando ela encontra processos, a consulta para em `StatusAcao.AGUARDANDO_CONFIRMACAO` (13) e a resposta da ação traz o bloco `confirmacao` (total de processos, custo estimado e `expira_em`). A confirmação vale por 1 hora. Cancelar leva a consulta a `StatusAcao.CANCELADA` (14).

| Método | Rota                                  |
| ------ | ------------------------------------- |
| POST   | `/acao/{acao_id}/confirmar-consulta`  |
| POST   | `/acao/{acao_id}/cancelar-consulta`   |

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai import StatusAcao
from intimai.servicos.buscar.acao.acao_busca import AcaoBusca
from intimai.servicos.solicitar.acao.acao_confirmar_consulta_solicitacao import AcaoConfirmarConsultaSolicitacao
from intimai.servicos.solicitar.acao.acao_cancelar_consulta_solicitacao import AcaoCancelarConsultaSolicitacao

try:
    sdk = Intimai('api_token')

    id_acao = 1  # ID da consulta (ação) no Intima.ai

    consulta = sdk.servicos.buscar(AcaoBusca(id_acao))

    if consulta['data']['status'] == StatusAcao.AGUARDANDO_CONFIRMACAO:
        confirmacao = consulta['data']['confirmacao']  # total, custo_estimado, expira_em...

        sdk.servicos.solicitar(AcaoConfirmarConsultaSolicitacao(id_acao))
        # ou: sdk.servicos.solicitar(AcaoCancelarConsultaSolicitacao(id_acao))
except ExcecaoRequisicaoAPI as e:
    print(e.get_status(), e.get_mensagem())
```

[Voltar ao topo](#recurso-ações)
[Voltar a lista da API](../../README.md#recursos)
[Voltar para o README](../../README.md#intimaai--sdk-v3-python)
