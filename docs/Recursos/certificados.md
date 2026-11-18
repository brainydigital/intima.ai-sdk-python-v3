# Recurso: **Certificados**

> Certas ações como protocolar, por exemplo, exigem que possua um `Tribunal` com o tipo de autenticação
> `Certificado A1`.
>
> Após associar um `Certificado A1` a sua conta, você deverá esperar até que o mesmo seja aprovado e
> liberado por nossa equipe.

Todas as URIs são relativas a *https://app.intima.ai/api/v3*

## Exemplos

Para solicitar serviços referentes ao certificado, você deve instanciar o tipo de serviço antes e inserir nas funções padrões dos serviços. Veja os serviços disponíveis para o certificado nos exemplos abaixo.

### **Busca**

> Obs: Lembre-se que é possível paginar ou aplicar filtros as buscas dos serviços.

#### Geral

Exemplo para realizar uma busca geral de todos os certificados do usuário.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.certificado.certificado_busca import CertificadoBusca

try:
    sdk = Intimai('api_token')

    # Se não for inserido nenhum id no serviço busca, ele irá retornar todos os registros daquele serviço
    certificados = CertificadoBusca()

    resultado = sdk.servicos.buscar(certificados)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

#### Específica

Exemplo para realizar uma busca específica de um certificado do usuário.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.certificado.certificado_busca import CertificadoBusca

try:
    sdk = Intimai('api_token')

    id_certificado = 1  # ID do certificado no Intima.ai
    certificado = CertificadoBusca(id_certificado)

    resultado = sdk.servicos.buscar(certificado)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

### **Solicitações**

Exemplos dos serviços disponíveis para solicitação do cadastro, atualização ou exclusão do certificado.

#### Cadastro

Exemplo para solicitar o cadastro de um certificado.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.modelos.certificado import Certificado
from intimai.servicos.solicitar_cadastro.certificado.certificado_solicitacao_cadastro import CertificadoSolicitacaoCadastro

try:
    sdk = Intimai('api_token')

    model_certificado = Certificado('/caminho/certificado', 'senha')

    certificado = CertificadoSolicitacaoCadastro(model_certificado)

    resultado = sdk.servicos.solicitar_cadastro(certificado)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

#### Atualização

Exemplo para solicitar a atualização de um certificado.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.modelos.certificado import Certificado
from intimai.servicos.solicitar_atualizacao.certificado.certificado_solicita_atualizacao import CertificadoSolicitaAtualizacao

try:
    sdk = Intimai('api_token')

    id_certificado = 1  # ID do certificado no Intima.ai
    model_certificado = Certificado('/caminho/certificado', 'senha')

    certificado = CertificadoSolicitaAtualizacao(id_certificado, model_certificado)

    resultado = sdk.servicos.solicitar_atualizacao(certificado)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

#### Exclusão

Exemplo para solicitar a exclusão de um certificado.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.solicitar_exclusao.certificado.certificado_solicitacao_exclusao import CertificadoSolicitacaoExclusao

try:
    sdk = Intimai('api_token')

    id_certificado = 1  # ID do certificado no Intima.ai

    certificado = CertificadoSolicitacaoExclusao(id_certificado)

    resultado = sdk.servicos.solicitar_exclusao(certificado)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

[Voltar ao topo](#recurso-certificados)
[Voltar a lista da API](../../README.md#recursos)
[Voltar para o README](../../README.md#intimaai--sdk-v3-python)
