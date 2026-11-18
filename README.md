<br />
<div align="center">
  <a href="#">
    <img src="https://raw.githubusercontent.com/brainydigital/intima.ai-sdk-php/master/docs/images/logo.png" alt="Logo" width="120" height="120">
  </a>

[![PyPI version](https://img.shields.io/pypi/v/intima-ai-sdk.svg?style=flat&color=blue)](https://pypi.org/project/intima-ai-sdk/)
[![PyPI downloads](https://img.shields.io/pypi/dm/intima-ai-sdk.svg?style=flat&color=97ca00)](https://pypi.org/project/intima-ai-sdk/)
[![Contributors](https://img.shields.io/github/contributors/brainydigital/intima.ai-sdk-python.svg?style=flat&color=yellow)](https://github.com/brainydigital/intima.ai-sdk-python/graphs/contributors)
[![MIT license](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
</div>

# Intima.ai — SDK V3 Python

Implementação da API V3 do [Intima.ai](https://app.intima.ai) em forma de SDK Client para Python. Cobre todas as ações disponíveis na plataforma e as expõe como métodos prontos para integração, bastando um `api_token` válido.

- **Versão da API:** 3
- **Versão da SDK:** 1.1.0
- **Referência completa:** [Postman Docs](https://documenter.getpostman.com/view/11707205/2sAYBaAVnT)

## Requisitos

- Python >= 3.10
- requests >= 2.31.0

## Instalação

### Via pip

```bash
pip install intima-ai-sdk
```

### Manual

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/brainydigital/intima.ai-sdk-python
cd intima.ai-sdk-python
pip install requests
```

## Início Rápido

Antes de executar qualquer ação, você precisa:

1. **Importar um Certificado A1** na sua conta (emitido por qualquer certificadora autorizada), _ou_ cadastrar um autenticador com usuário/senha, caso o tribunal suporte;
2. **Criar uma Autenticação** para cada tribunal onde deseja operar;
3. **Solicitar ações** usando os serviços correspondentes.

### Exemplo: Solicitar cópia processual

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.solicitar.copia.copia_solicitacao import CopiaSolicitacao

try:
    sdk = Intimai('seu_api_token')

    id_autenticador = 1                           # ID do autenticador no Intima.ai
    numero_do_processo = '00000000000000000000'   # Número do processo no tribunal

    copia = CopiaSolicitacao(id_autenticador, numero_do_processo)

    resultado = sdk.servicos.solicitar(copia)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

## Paginação e Filtros

Os serviços de busca suportam paginação e filtros opcionais:

```python
from intimai import Intimai, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.copia.copia_busca import CopiaBusca

try:
    sdk = Intimai('seu_api_token')

    copias  = CopiaBusca()
    pagina  = 5
    filtros = {'status': '1,3', 'per_page': 50}  # Filtros com vários valores aceitam '1,2,3'

    resultado = sdk.servicos.buscar(copias, pagina, filtros)

    print(resultado)
except ExcecaoRequisicaoAPI as e:
    print(e.para_dict())
except Exception as e:
    print(str(e))
```

O tamanho da página é 15 por padrão. `per_page` muda esse valor nas buscas de ações e de consultas.

## Autenticação em dois fatores (2FA)

Se a conta tiver 2FA ativo, toda request precisa do código de 6 dígitos do app autenticador. A SDK envia o código no header `X-Codigo-2FA`, igual à collection da API V3. O `api_token` continua na query.

```python
from intimai import Intimai

# Código fixo (vale enquanto o app autenticador mostrar o mesmo código)
sdk = Intimai('seu_api_token', {'codigo_2fa': '482913'})

# Ou uma função chamada a cada request, para sempre mandar o código atual
sdk = Intimai('seu_api_token', {'codigo_2fa': lambda: '482913'})

# Também dá para trocar depois
sdk.definir_codigo_2fa('123456')
```

Sem 2FA na conta, não informe nada: o header não é enviado.

## Limites e erros

Quando a API responde com erro, a SDK lança `ExcecaoRequisicaoAPI` com o status e o corpo da resposta:

```python
import time

from intimai import Intimai, ExcecaoDoisFatores, ExcecaoLimiteDeRequisicoes, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.acao.acao_busca import AcaoBusca

sdk = Intimai('seu_api_token')

try:
    resultado = sdk.servicos.buscar(AcaoBusca())
except ExcecaoDoisFatores as e:
    print('401: código 2FA ausente, inválido ou cadastro de 2FA pendente no painel')
except ExcecaoLimiteDeRequisicoes as e:
    time.sleep(e.get_retry_after() or 60)
except ExcecaoRequisicaoAPI as e:
    print(e.get_status())    # código HTTP
    print(e.get_mensagem())  # mensagem da API
    print(e.get_erros())     # erros de validação por campo (422)
    print(e.get_corpo())     # corpo completo da resposta
```

| HTTP | Quando |
| ---- | ------ |
| 401  | `api_token` inválido ou problema no 2FA (`ExcecaoDoisFatores`) |
| 403  | Usuário inativo |
| 422  | Erro de validação (`get_erros()`), dados fiscais incompletos, autenticador indisponível ou certificado duplicado |
| 429  | Mais de 1000 requests por minuto, ou mais de 10 códigos 2FA errados por minuto (`ExcecaoLimiteDeRequisicoes`) |
| 457  | Cota de solicitações por hora do plano esgotada |
| 458  | Certificado inválido ou ausente |
| 459  | Saldo insuficiente, ou serviço indisponível no tribunal |

O tamanho máximo dos PDFs e a quantidade de arquivos por protocolo são definidos pela API; se passar do limite, a resposta é 422.

## Serviços Disponíveis

| Serviço               | Recursos disponíveis                                                                                                                                                                                  |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Atualizar             | Autenticador, Escuta, Intimação, Notificação                                                                                                                                                          |
| Buscar                | Ação, Andamento, Autenticador, Captura Agendada, Certificado, Código de Ajuda, Consulta, Consulta pré-análise, Cópia, Crédito, Escuta, Informação, Intimação, Notificação, Protocolo, Protocolo Habilitação, Transação, Tribunal, Usuário |
| Cadastrar             | Andamento, Autenticador, Autenticador 2FA, Escuta, Notificação                                                                                                                                        |
| Excluir               | Andamento, Escuta, Notificação                                                                                                                                                                        |
| Resultado             | Ação, Andamento, Consulta, Escuta                                                                                                                                                                     |
| Solicitar             | Ação (confirmar/cancelar consulta), Andamento, Autenticador (capturar intimações), Consulta, Consulta pré-análise, Cópia, Escuta, Informação, Protocolo, Protocolo Habilitação                         |
| Solicitar Atualização | Certificado                                                                                                                                                                                           |
| Solicitar Cadastro    | Certificado                                                                                                                                                                                           |
| Solicitar Exclusão    | Certificado                                                                                                                                                                                           |
| Tentar Novamente      | Ação                                                                                                                                                                                                  |

## Recursos

| Recurso                                                                                                              | Descrição                                                                       |
| -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [**Ações**](docs/Recursos/acoes.md#recurso-ações)                                                                    | Endpoints para ações realizadas no Intima.ai                                    |
| [**Andamentos**](docs/Recursos/andamentos.md#recurso-andamentos)                                                     | Endpoints para andamentos processuais                                           |
| [**Autenticações**](docs/Recursos/autenticacoes.md#recurso-autenticações)                                            | Endpoints para autenticações                                                    |
| [**Capturas Agendadas**](docs/Recursos/capturasAgendadas.md#recurso-capturas-agendadas)                              | Histórico dos horários agendados de captura de intimações e escutas            |
| [**Certificados**](docs/Recursos/certificados.md#recurso-certificados)                                               | Endpoints para certificados                                                     |
| [**Códigos de Ajuda**](docs/Recursos/codigosAjuda.md#recurso-códigos-de-ajuda)                                       | Catálogo de códigos de erro, cobrança e nova tentativa automática               |
| [**Consultas**](docs/Recursos/consultas.md#recurso-consultas)                                                        | Endpoints para consultas processuais e pré-análises                             |
| [**Cópias**](docs/Recursos/copias.md#recurso-cópias)                                                                 | Endpoints para cópias processuais                                               |
| [**Créditos**](docs/Recursos/creditos.md#recurso-créditos)                                                           | Endpoints para créditos no Intima.ai                                            |
| [**Escutas**](docs/Recursos/escutas.md#recurso-escutas)                                                              | Endpoints para escutas processuais                                              |
| [**Informações**](docs/Recursos/informacoes.md#recurso-informações)                                                  | Endpoints para informações processuais                                          |
| [**Intimações**](docs/Recursos/intimacoes.md#recurso-intimações)                                                     | Endpoints para intimações capturadas                                            |
| [**Notificações**](docs/Recursos/notificacoes.md#recurso-notificações)                                               | Endpoints para notificações do usuário                                          |
| [**Protocolos**](docs/Recursos/protocolos.md#recurso-protocolos)                                                     | Endpoints para protocolos                                                       |
| [**Protocolos de Habilitação**](docs/Recursos/protocolosDeHabilitacao.md#recurso-protocolos-de-habilitação)          | Endpoints para protocolos de habilitação                                        |
| [**Transações**](docs/Recursos/transacoes.md#recurso-transações)                                                     | Endpoints para transações no Intima.ai                                          |
| [**Tribunais**](docs/Recursos/tribunais.md#recurso-tribunais)                                                        | Endpoints para tribunais                                                        |
| [**Usuários**](docs/Recursos/usuarios.md#recurso-usuários)                                                           | Endpoints para o usuário                                                        |

## Modelos

| Modelo                                                                            | Descrição                                                                                              |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| [**Certificado**](docs/Modelos/certificado.md#modelo-certificado)                 | Instanciação do certificado A1 (necessário para cadastro e atualização de certificado no Intima.ai)    |
| [**Documento**](docs/Modelos/documento.md#modelo-documento)                       | Instanciação de documento (necessário para protocolos em alguns tribunais)                             |
| [**Parte Vinculada**](docs/Modelos/parteVinculada.md#modelo-parte-vinculada)      | Instanciação de parte vinculada (necessário para protocolos em alguns tribunais)                       |
| [**Petição**](docs/Modelos/peticao.md#modelo-petição)                             | Instanciação de petição (necessário para protocolos em alguns tribunais)                               |

## Utilidades

| Utilidade                                                                                  | Descrição                                                |
| ------------------------------------------------------------------------------------------ | -------------------------------------------------------- |
| [**Ação**](docs/Utilidades/acao.md#utilidade-ação)                                         | Constantes para tipos de ação                            |
| [**Captura Agendada**](docs/Utilidades/capturaAgendada.md#utilidade-captura-agendada)      | Constantes para tipos e situações de captura agendada    |
| [**Dia**](docs/Utilidades/dia.md#utilidade-dia)                                            | Constantes para dias da semana                           |
| [**Horário**](docs/Utilidades/horario.md#utilidade-horário)                                | Constantes para horários                                 |
| [**Nova Tentativa**](docs/Utilidades/novaTentativa.md#utilidade-nova-tentativa)            | Constantes para a situação da nova tentativa automática  |
| [**Polo**](docs/Utilidades/polo.md#utilidade-polo)                                         | Constantes para polo processual (ativo/passivo)          |
| [**Status da Ação**](docs/Utilidades/statusAcao.md#utilidade-status-da-ação)               | Constantes para o status das ações                       |
| [**Tipo Declaração**](docs/Utilidades/tipoDeclaracao.md#utilidade-tipo-declaração)         | Constantes para tipos de declaração                      |
| [**Tipo Solicitação**](docs/Utilidades/tipoSolicitacao.md#utilidade-tipo-solicitação)      | Constantes para tipos de solicitação                     |

## Autenticação

| Campo       | Valor            |
| ----------- | ---------------- |
| Tipo        | API Key          |
| Parâmetro   | `api_token`      |
| Localização | URL query string |

Com 2FA ativo na conta, o código vai no header `X-Codigo-2FA` (veja [Autenticação em dois fatores](#autenticação-em-dois-fatores-2fa)).

## Testes

```bash
python -m venv .venv
.venv/bin/pip install -e .
.venv/bin/python -m unittest discover -s tests -t .
```

## Autores

- **BrainyDigital** — [Intima.ai](https://intima.ai)
