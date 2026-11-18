# Recurso: **Capturas Agendadas**

> Cada horário agendado de captura de intimações ou de escuta processual vira uma linha neste recurso.
> Assim você acompanha o que rodou, o que deu erro e o que não chegou a ser executado (com o motivo).

Todas as URIs são relativas a *https://app.intima.ai/api/v3*

| Método | Rota                                              |
| ------ | ------------------------------------------------- |
| GET    | `/captura-agendada/buscar`                        |
| GET    | `/captura-agendada/{captura_agendada_id}/buscar`  |

## **Busca**

### Geral

Filtros aceitos (todos opcionais; os de lista aceitam `'1,2,3'`):

| Filtro               | Valores                                                                 |
| -------------------- | ----------------------------------------------------------------------- |
| `data_inicial`       | data inicial do horário previsto                                        |
| `data_final`         | data final do horário previsto                                          |
| `autenticadores_ids` | IDs de autenticadores                                                   |
| `escutas_ids`        | IDs de escutas processuais                                              |
| `tipos`              | `TipoCapturaAgendada.INTIMACAO`, `TipoCapturaAgendada.ESCUTA`           |
| `situacoes`          | `SituacaoCapturaAgendada.EM_ANDAMENTO`, `FINALIZADA`, `NAO_EXECUTADA`, `ERRO` |
| `motivos`            | motivo de não execução                                                  |

```python
from intimai import Intimai, ExcecaoRequisicaoAPI, SituacaoCapturaAgendada, TipoCapturaAgendada
from intimai.servicos.buscar.captura_agendada.captura_agendada_busca import CapturaAgendadaBusca

try:
    sdk = Intimai('api_token')

    filtros = {
        'tipos': TipoCapturaAgendada.INTIMACAO,
        'situacoes': f'{SituacaoCapturaAgendada.NAO_EXECUTADA},{SituacaoCapturaAgendada.ERRO}',
        'autenticadores_ids': '1,2',
    }

    resultado = sdk.servicos.buscar(CapturaAgendadaBusca(), 1, filtros)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
```

### Específica

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.captura_agendada.captura_agendada_busca import CapturaAgendadaBusca

try:
    sdk = Intimai('api_token')

    id_captura_agendada = 1  # ID da captura agendada no Intima.ai

    resultado = sdk.servicos.buscar(CapturaAgendadaBusca(id_captura_agendada))

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
```

[Voltar ao topo](#recurso-capturas-agendadas)
[Voltar para o README](../../README.md#intimaai--sdk-v3-python)
