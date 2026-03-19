# Recurso: **Usuários**

> Através deste recurso você pode consultar todas as informações do usuário.

Todas as URIs são relativas a *https://app.intima.ai/api/v3*

## Exemplos

Para solicitar serviços referentes ao usuário, você deve instanciar o tipo de serviço antes e inserir nas funções padrões dos serviços. Veja os serviços disponíveis para o usuário nos exemplos abaixo.

### **Busca**

Exemplo para realizar a busca do usuário.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.usuario.usuario_busca import UsuarioBusca

try:
    sdk = Intimai('api_token')

    usuario = UsuarioBusca()

    resultado = sdk.servicos.buscar(usuario)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

[Voltar ao topo](#recurso-usuários)
[Voltar a lista da API](../../README.md#recursos)
[Voltar para o README](../../README.md#intimaai---sdk-v3-python)
