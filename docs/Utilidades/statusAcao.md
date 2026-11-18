# Utilidade: **Status da Ação**

Constantes para o campo `status` das ações devolvidas pela API, por exemplo:

```python
from intimai import StatusAcao

if acao['status'] == StatusAcao.AGUARDANDO_CONFIRMACAO:
    print('Confirme ou cancele a consulta')
```

Constante | Valor | Significado
------------ | ------------- | -------------
PENDENTE | 0 | Pendente
FINALIZADO | 1 | Finalizado
PROCESSANDO | 2 | Processando
ERRO | 3 | Ocorreu um erro
NA_FILA | 4 | Em fila
PREPARANDO_DOCUMENTOS | 5 | Preparando documentos
ESPERANDO_ACAO_USUARIO | 6 | Aguardando ação do usuário
TENTANDO_NOVAMENTE | 7 | Tentando executar a ação novamente
ESPERANDO | 8 | Aguardando
ESPERANDO_ARQUIVOS | 9 | Aguardando download dos arquivos
ESPERANDO_2FA | 10 | Aguardando 2FA
USUARIO_SELECIONADO_NAO_ENCONTRADO | 11 | Usuário selecionado não encontrado
AGUARDANDO_DADOS_FISCAIS | 12 | Ação pausada (dados fiscais)
AGUARDANDO_CONFIRMACAO | 13 | Aguardando confirmação da consulta
CANCELADA | 14 | Cancelada

[Voltar para o README](../../README.md#intimaai--sdk-v3-python)
