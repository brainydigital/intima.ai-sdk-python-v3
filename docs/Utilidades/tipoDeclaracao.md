# Utilidade: **Tipo Declaração**

Você pode utilizar a constante de tipo declaração para melhor legibilidade do seu código, por exemplo:

```python
from intimai.utilidades.tipo_declaracao import TipoDeclaracao

tipo_declaracao = TipoDeclaracao.DECLARACAO_SOB_PENA_DE_LEI
```

Abaixo, está a tabela com todos os valores possíveis para a constante de tipo declaração.

Constante | Valor
------------ | -------------
DECLARACAO_SOB_PENA_DE_LEI | 0
DELCARACAO_PELA_APRESENTACAO_OPORTUNA_DO_INSTRUMENTO_DE_MANDATO | 1

Tribunais da Justiça do Trabalho (TRT) usam estes valores:

Constante | Valor
------------ | -------------
TRT_SOB_PENA_DE_LEI_INSTRUMENTO_DE_PROCURACAO | 0
TRT_NA_FORMA_DE_EXCECAO | 1
TRT_SOB_PENA_DE_LEI_SUBSTABELECIMENTO_COM_RESERVA_DE_PODERES | 2
TRT_SOB_PENA_DE_LEI_SUBSTABELECIMENTO_SEM_RESERVA_DE_PODERES | 3
TRT_SOB_PENA_DE_LEI_JA_CONSTAR_PROCURACAO_OU_SUBSTABELECIMENTO_EXISTENTE | 4

[Voltar para o README](../../README.md#intimaai--sdk-v3-python)
