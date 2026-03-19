# Recurso: **Notificações**

> Através deste recurso você poderá ter o controle de todos os outros emails em que se deseja
> receber notificações, além do seu email principal.

Todas as URIs são relativas a *https://app.intima.ai/api/v3*

## Exemplos

Para solicitar serviços referentes as notificações, você deve instanciar o tipo de serviço antes e inserir nas funções padrões dos serviços. Veja os serviços disponíveis para as notificações nos exemplos abaixo.

## Notificação por Email

### **Busca**

> Obs: Lembre-se que é possível paginar ou aplicar filtros as buscas dos serviços.

#### Geral

Exemplo para realizar uma busca geral de todas as notificações por email do usuário.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.notificacao.notificacao_email_busca import NotificacaoEmailBusca

try:
    sdk = Intimai('api_token')

    # Se não for inserido nenhum id no serviço busca, ele irá retornar todos os registros daquele serviço
    notificacoes_email = NotificacaoEmailBusca()

    resultado = sdk.servicos.buscar(notificacoes_email)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

#### Específica

Exemplo para realizar uma busca específica de uma notificação por email.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.notificacao.notificacao_email_busca import NotificacaoEmailBusca

try:
    sdk = Intimai('api_token')

    id_notificacao_email = 1  # ID da notificação por email no Intima.ai

    notificacao_email = NotificacaoEmailBusca(id_notificacao_email)

    resultado = sdk.servicos.buscar(notificacao_email)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

### **Cadastro**

Exemplo para realizar o cadastro de uma notificação por email.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.cadastrar.notificacao.notificacao_email_cadastro import NotificacaoEmailCadastro

try:
    sdk = Intimai('api_token')

    email = 'email@exemplo.com'

    notificacao_email = NotificacaoEmailCadastro(email)

    resultado = sdk.servicos.cadastrar(notificacao_email)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

### **Atualização**

Exemplo para realizar a atualização de uma notificação por email.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.atualizar.notificacao.notificacao_email_atualizacao import NotificacaoEmailAtualizacao

try:
    sdk = Intimai('api_token')

    id_notificacao_email = 1           # ID da notificação por email no Intima.ai
    novo_email = 'email-novo@exemplo.com'

    notificacao_email = NotificacaoEmailAtualizacao(id_notificacao_email, novo_email)

    resultado = sdk.servicos.atualizar(notificacao_email)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

### **Exclusão**

Exemplo para realizar a exclusão de uma notificação por email.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.excluir.notificacao.notificacao_email_exclusao import NotificacaoEmailExclusao

try:
    sdk = Intimai('api_token')

    id_notificacao_email = 1  # ID da notificação por email no Intima.ai

    notificacao_email = NotificacaoEmailExclusao(id_notificacao_email)

    resultado = sdk.servicos.excluir(notificacao_email)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

## Notificação por Webhook

### **Busca**

> Obs: Lembre-se que é possível paginar ou aplicar filtros as buscas dos serviços.

#### Geral

Exemplo para realizar uma busca geral de todas as notificações por webhook do usuário.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.notificacao.notificacao_webhook_busca import NotificacaoWebhookBusca

try:
    sdk = Intimai('api_token')

    # Se não for inserido nenhum id no serviço busca, ele irá retornar todos os registros daquele serviço
    notificacoes_webhook = NotificacaoWebhookBusca()

    resultado = sdk.servicos.buscar(notificacoes_webhook)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

#### Específica

Exemplo para realizar uma busca específica de uma notificação por webhook.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.notificacao.notificacao_webhook_busca import NotificacaoWebhookBusca

try:
    sdk = Intimai('api_token')

    id_notificacao_webhook = 1  # ID da notificação por webhook no Intima.ai

    notificacao_webhook = NotificacaoWebhookBusca(id_notificacao_webhook)

    resultado = sdk.servicos.buscar(notificacao_webhook)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

### **Cadastro**

Exemplo para realizar o cadastro de uma notificação por webhook.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.cadastrar.notificacao.notificacao_webhook_cadastro import NotificacaoWebhookCadastro
from intimai.utilidades.acao import Acao

try:
    sdk = Intimai('api_token')

    tipo_acao = Acao.TIPO_COPIA
    verbo_http = 'GET'
    url = 'url-exemplo.com'

    notificacao_webhook = NotificacaoWebhookCadastro(tipo_acao, verbo_http, url)

    resultado = sdk.servicos.cadastrar(notificacao_webhook)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

### **Atualização**

Exemplo para realizar a atualização de uma notificação por webhook.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.atualizar.notificacao.notificacao_webhook_atualizacao import NotificacaoWebhookAtualizacao
from intimai.utilidades.acao import Acao

try:
    sdk = Intimai('api_token')

    id_notificacao_webhook = 1           # ID da notificação por webhook no Intima.ai
    novo_tipo_acao = Acao.TIPO_INFORMACAO
    novo_verbo_http = 'POST'
    nova_url = 'nova-url-exemplo.com'

    notificacao_webhook = NotificacaoWebhookAtualizacao(id_notificacao_webhook, novo_tipo_acao, novo_verbo_http, nova_url)

    resultado = sdk.servicos.atualizar(notificacao_webhook)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

### **Exclusão**

Exemplo para realizar a exclusão de uma notificação por webhook.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.excluir.notificacao.notificacao_webhook_exclusao import NotificacaoWebhookExclusao

try:
    sdk = Intimai('api_token')

    id_notificacao_webhook = 1  # ID da notificação por webhook no Intima.ai

    notificacao_webhook = NotificacaoWebhookExclusao(id_notificacao_webhook)

    resultado = sdk.servicos.excluir(notificacao_webhook)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

[Voltar ao topo](#recurso-notificações)
[Voltar a lista da API](../../README.md#recursos)
[Voltar para o README](../../README.md#intimaai---sdk-v3-python)
