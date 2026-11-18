# Utilidade: **Nova Tentativa**

Constantes para o campo `situacao` do bloco `nova_tentativa` das [ações com erro](../Recursos/acoes.md#nova-tentativa-automática).

```python
from intimai import SituacaoNovaTentativa
```

Constante | Valor | Quando
------------ | ------------- | -------------
SituacaoNovaTentativa.AGENDADA | agendada | A plataforma vai repetir a ação; `prevista_para` traz o horário
SituacaoNovaTentativa.AGUARDANDO_CONDICAO | aguardando_condicao | Vai repetir quando houver saldo (612) ou quando o ciclo do plano virar (627)
SituacaoNovaTentativa.ENCERRADA | encerrada | As novas tentativas acabaram
SituacaoNovaTentativa.SEM_NOVA_TENTATIVA | sem_nova_tentativa | O erro não tem nova tentativa automática

[Voltar para o README](../../README.md#intimaai--sdk-v3-python)
