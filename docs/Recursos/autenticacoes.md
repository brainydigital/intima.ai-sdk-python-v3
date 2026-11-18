# Recurso: **Autenticações**

> Os Autenticadores do `Intima.ai` são utilizados para ter acesso aos tribunais.
> Você pode criar diversas autenticações para diversos tribunais sendo uma autenticação para cada tribunal.
> No cadastro, `id_tribunal` aceita um id, uma lista (`[1, 2]`) ou um texto (`'1,2'`): a API cria uma autenticação para cada tribunal informado.
>
> Alguns tribunais exigem autenticação de dois fatores (2FA) no login. Para eles, informe a `secret` (Base32, mínimo de 16 caracteres) no cadastro ou depois, com [Armazenar 2FA](#armazenar-2fa-do-tribunal).
> Alguns tribunais também exigem um certificado no login por usuário/senha: nesses casos, informe `id_certificado`.

Todas as URIs são relativas a *https://app.intima.ai/api/v3*

## Exemplos

Para solicitar serviços referentes ao autenticador, você deve instanciar o tipo de serviço antes e inserir nas funções padrões dos serviços. Veja os serviços disponíveis para o autenticador nos exemplos abaixo.

### **Busca**

> Obs: Lembre-se que é possível paginar ou aplicar filtros as buscas dos serviços.

#### Geral

Exemplo para realizar uma busca geral de todas as autenticações do usuário.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.autenticador.autenticador_busca import AutenticadorBusca

try:
    sdk = Intimai('api_token')

    # Se não for inserido nenhum id no serviço busca, ele irá retornar todos os registros daquele serviço
    autenticadores = AutenticadorBusca()

    resultado = sdk.servicos.buscar(autenticadores)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

#### Específica

Exemplo para realizar uma busca específica de uma autenticação do usuário.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.autenticador.autenticador_busca import AutenticadorBusca

try:
    sdk = Intimai('api_token')

    id_autenticador = 1  # ID do autenticador no Intima.ai
    autenticador = AutenticadorBusca(id_autenticador)

    resultado = sdk.servicos.buscar(autenticador)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

### **Dados**

Exemplos dos serviços disponíveis para atualização dos dados.

#### Atualizar Dados OAB

Exemplo para realizar a atualização dos dados referentes a OAB do autenticador específico do usuário.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.atualizar.autenticador.autenticador_oab_atualizacao import AutenticadorOabAtualizacao

try:
    sdk = Intimai('api_token')

    id_autenticador = 1  # ID do autenticador no Intima.ai
    oab = {
        'numero': 'numero_valor',  # Número da OAB
        'letra': 'letra_valor',    # Opcional
        'uf': 'uf_valor'           # Ex: RJ, PE, PB...
    }

    autenticador = AutenticadorOabAtualizacao(id_autenticador, oab)

    resultado = sdk.servicos.atualizar(autenticador)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

#### Atualizar Dados Usuário/Senha

Exemplo para realizar a atualização dos dados referentes ao usuário/senha (obrigatório ser do tipo regular) do autenticador específico do usuário.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.atualizar.autenticador.autenticador_regular_atualizacao import AutenticadorRegularAtualizacao

try:
    sdk = Intimai('api_token')

    id_autenticador = 1                    # ID do autenticador no Intima.ai
    usuario = 'usuario-novo-valor'         # Opcional se estiver alterando apenas a senha
    senha = 'senha-nova-valor'             # Opcional se estiver alterando apenas o usuário

    id_certificado = None                  # Opcional; obrigatório nos tribunais que exigem certificado no login regular

    autenticador = AutenticadorRegularAtualizacao(id_autenticador, usuario, senha, id_certificado)

    resultado = sdk.servicos.atualizar(autenticador)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

#### Atualizar Perfil

Exemplo para atualizar a sigla e/ou a descrição do perfil do autenticador. Informe pelo menos um dos dois.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.atualizar.autenticador.autenticador_perfil_atualizacao import AutenticadorPerfilAtualizacao

try:
    sdk = Intimai('api_token')

    id_autenticador = 1  # ID do autenticador no Intima.ai

    resultado = sdk.servicos.atualizar(AutenticadorPerfilAtualizacao(id_autenticador, 'ADV', 'Advogado'))

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.get_status(), e.get_mensagem())
```

### **Situação**

Exemplo para habilitar ou desabilitar um autenticador. Desabilitado, ele não solicita nenhuma ação até ser habilitado de novo. A API responde 422 se o autenticador já estiver na situação pedida.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.atualizar.autenticador.autenticador_habilitar_atualizacao import AutenticadorHabilitarAtualizacao
from intimai.servicos.atualizar.autenticador.autenticador_desabilitar_atualizacao import AutenticadorDesabilitarAtualizacao

try:
    sdk = Intimai('api_token')

    id_autenticador = 1  # ID do autenticador no Intima.ai

    resultado = sdk.servicos.atualizar(AutenticadorHabilitarAtualizacao(id_autenticador))
    # ou: sdk.servicos.atualizar(AutenticadorDesabilitarAtualizacao(id_autenticador))

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.get_status(), e.get_mensagem())
```

### **Armazenar 2FA do tribunal**

Exemplo para armazenar a `secret` do 2FA do tribunal em um ou mais autenticadores. A `secret` é a chave Base32 (letras A–Z e dígitos 2–7, mínimo de 16 caracteres) mostrada pelo tribunal ao configurar o app autenticador.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.cadastrar.autenticador.autenticador_dois_fatores_cadastro import AutenticadorDoisFatoresCadastro

try:
    sdk = Intimai('api_token')

    ids_autenticadores = [1, 2]  # Um ID ou uma lista de IDs de autenticadores

    resultado = sdk.servicos.cadastrar(AutenticadorDoisFatoresCadastro(ids_autenticadores, 'JBSWY3DPEHPK3PXP'))

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.get_status(), e.get_mensagem())
```

### **Tipo**

Exemplos dos serviços disponíveis para criar autenticadores ou alterar o autenticador de Certificado para Regular e vice-versa.

#### Alterar para Usuário/Senha

Exemplo para realizar a alteração do tipo do autenticador para usuário/senha (obrigatório o autenticador ser previamente do tipo Certificado A1).

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.atualizar.autenticador.autenticador_alterar_para_regular_atualizacao import AutenticadorAlterarParaRegularAtualizacao

try:
    sdk = Intimai('api_token')

    id_autenticador = 1              # ID do autenticador no Intima.ai
    usuario = 'usuario-valor'        # Usuário que será utilizado para acesso ao tribunal
    senha = 'senha-valor'            # Senha que será utilizada para acesso ao tribunal

    id_certificado = None            # Opcional; obrigatório nos tribunais que exigem certificado no login regular

    autenticador = AutenticadorAlterarParaRegularAtualizacao(id_autenticador, usuario, senha, id_certificado)

    resultado = sdk.servicos.atualizar(autenticador)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

#### Alterar para Certificado

Exemplo para realizar a alteração do tipo do autenticador para certificado A1 (obrigatório o autenticador ser previamente do tipo usuário/senha).

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.atualizar.autenticador.autenticador_alterar_para_certificado_atualizacao import AutenticadorAlterarParaCertificadoAtualizacao

try:
    sdk = Intimai('api_token')

    id_autenticador = 1  # ID do autenticador no Intima.ai
    id_certificado = 1   # ID do certificado no Intima.ai

    autenticador = AutenticadorAlterarParaCertificadoAtualizacao(id_autenticador, id_certificado)

    resultado = sdk.servicos.atualizar(autenticador)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

#### Criar com Certificado

Exemplo para realizar o cadastro de um autenticador do tipo certificado A1.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.cadastrar.autenticador.autenticador_certificado_cadastro import AutenticadorCertificadoCadastro

try:
    sdk = Intimai('api_token')

    id_tribunal = 1  # ID do tribunal no Intima.ai
    oab = {
        'numero': 'numero_valor',  # Número da OAB
        'letra': 'letra_valor',    # Opcional
        'uf': 'uf_valor'           # Ex: RJ, PE, PB...
    }
    id_certificado = 1

    autenticador = AutenticadorCertificadoCadastro(
        id_tribunal,             # Um ID ou uma lista: [1, 2]
        oab,
        id_certificado,
        usuario_sigla=None,      # Opcional
        usuario_descricao=None,  # Opcional
        secret=None,             # Obrigatória se algum tribunal exigir 2FA
    )

    resultado = sdk.servicos.cadastrar(autenticador)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

#### Criar com Usuário/Senha

Exemplo para realizar o cadastro de um autenticador do tipo regular (usuário/senha).

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.cadastrar.autenticador.autenticador_regular_cadastro import AutenticadorRegularCadastro

try:
    sdk = Intimai('api_token')

    id_tribunal = 1  # ID do tribunal no Intima.ai
    oab = {
        'numero': 'numero_valor',  # Número da OAB
        'letra': 'letra_valor',    # Opcional
        'uf': 'uf_valor'           # Ex: RJ, PE, PB...
    }
    usuario = 'usuario-valor'  # Usuário que será utilizado para acesso ao tribunal
    senha = 'senha-valor'      # Senha que será utilizada para acesso ao tribunal

    autenticador = AutenticadorRegularCadastro(
        id_tribunal,             # Um ID ou uma lista: [1, 2]
        oab,
        usuario,
        senha,
        id_certificado=None,     # Obrigatório nos tribunais que exigem certificado no login regular
        usuario_sigla=None,      # Opcional
        usuario_descricao=None,  # Opcional
        secret=None,             # Obrigatória se algum tribunal exigir 2FA
    )

    resultado = sdk.servicos.cadastrar(autenticador)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

### **Intimação**

Exemplos dos serviços disponíveis para ativar/desativar captura de intimações do autenticador.

#### Ativar Captura

Exemplo para ativar a captura de intimações de um autenticador.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.atualizar.autenticador.autenticador_ativar_captura_intimacao_atualizacao import AutenticadorAtivarCapturaIntimacaoAtualizacao
from intimai.utilidades.dia import Dia
from intimai.utilidades.horario import Horario

try:
    sdk = Intimai('api_token')

    # ID do autenticador no Intima.ai
    id_autenticador = 1

    # Abas disponíveis no tribunal para o qual você está ativando a captura
    abas = ['aba_1', 'aba_2']

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

    # Por padrão, este valor é False, se quiser ativar, basta definir como True
    capturar_procuradorias = True

    autenticador = AutenticadorAtivarCapturaIntimacaoAtualizacao(
        id_autenticador,
        abas,
        dias_de_captura,
        horarios_de_captura,
        capturar_procuradorias
    )

    resultado = sdk.servicos.atualizar(autenticador)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

#### Desativar Captura

Exemplo para desativar a captura de intimações de um autenticador.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.atualizar.autenticador.autenticador_desativar_captura_intimacao_atualizacao import AutenticadorDesativarCapturaIntimacaoAtualizacao

try:
    sdk = Intimai('api_token')

    # ID do autenticador no Intima.ai
    id_autenticador = 1

    autenticador = AutenticadorDesativarCapturaIntimacaoAtualizacao(id_autenticador)

    resultado = sdk.servicos.atualizar(autenticador)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

#### Capturar Agora

Exemplo para pedir uma captura de intimações fora dos horários agendados. A captura do autenticador precisa estar ativa; caso contrário, a API responde 422.

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.solicitar.autenticador.autenticador_capturar_intimacoes_solicitacao import AutenticadorCapturarIntimacoesSolicitacao

try:
    sdk = Intimai('api_token')

    id_autenticador = 1  # ID do autenticador no Intima.ai

    resultado = sdk.servicos.solicitar(AutenticadorCapturarIntimacoesSolicitacao(id_autenticador))

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.get_status(), e.get_mensagem())
```

[Voltar ao topo](#recurso-autenticações)
[Voltar a lista da API](../../README.md#recursos)
[Voltar para o README](../../README.md#intimaai--sdk-v3-python)
