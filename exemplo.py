"""
Exemplo de uso do SDK Intima.ai para Python.

Instale as dependencias:
    pip install requests

Execute:
    python exemplo.py
"""

from intimai import (
    Intimai,
    ExcecaoRequisicaoAPI,
    Certificado,
    Documento,
    ParteVinculada,
    Peticao,
    Acao,
    Dia,
    Horario,
    Polo,
    TipoDeclaracao,
    TipoSolicitacao,
    StatusAcao,
    SituacaoCapturaAgendada,
    SituacaoNovaTentativa,
    TipoCapturaAgendada,
)
from intimai.servicos.buscar.captura_agendada.captura_agendada_busca import CapturaAgendadaBusca
from intimai.servicos.buscar.credito.credito_consumo_mensal_busca import CreditoConsumoMensalBusca
from intimai.servicos.solicitar.acao.acao_confirmar_consulta_solicitacao import AcaoConfirmarConsultaSolicitacao

# Servicos de BUSCAR
from intimai.servicos.buscar.acao.acao_busca import AcaoBusca
from intimai.servicos.buscar.andamento.andamento_busca import AndamentoBusca
from intimai.servicos.buscar.autenticador.autenticador_busca import AutenticadorBusca
from intimai.servicos.buscar.certificado.certificado_busca import CertificadoBusca
from intimai.servicos.buscar.codigo_ajuda.codigo_ajuda_busca import CodigoAjudaBusca
from intimai.servicos.buscar.consulta.consulta_busca import ConsultaBusca
from intimai.servicos.buscar.credito.credito_saldo_busca import CreditoSaldoBusca
from intimai.servicos.buscar.tribunal.tribunal_busca import TribunalBusca
from intimai.servicos.buscar.usuario.usuario_busca import UsuarioBusca

# Servicos de CADASTRAR
from intimai.servicos.cadastrar.autenticador.autenticador_regular_cadastro import AutenticadorRegularCadastro
from intimai.servicos.cadastrar.escuta.escuta_cadastro import EscutaCadastro
from intimai.servicos.cadastrar.notificacao.notificacao_webhook_cadastro import NotificacaoWebhookCadastro

# Servicos de ATUALIZAR
from intimai.servicos.atualizar.autenticador.autenticador_regular_atualizacao import AutenticadorRegularAtualizacao
from intimai.servicos.atualizar.escuta.escuta_atualizacao import EscutaAtualizacao

# Servicos de EXCLUIR
from intimai.servicos.excluir.andamento.andamento_exclusao import AndamentoExclusao

# Servicos de SOLICITAR
from intimai.servicos.solicitar.andamento.andamento_solicitacao import AndamentoSolicitacao
from intimai.servicos.solicitar.consulta.consulta_solicitacao import ConsultaSolicitacao
from intimai.servicos.solicitar.copia.copia_solicitacao import CopiaSolicitacao
from intimai.servicos.solicitar.protocolo.pje.protocolo_pje_solicitacao import ProtocoloPjeSolicitacao

# Servicos de RESULTADO
from intimai.servicos.resultado.andamento.andamento_resultado import AndamentoResultado
from intimai.servicos.resultado.consulta.consulta_resultado import ConsultaResultado

# Servicos de SOLICITAR_CADASTRO / SOLICITAR_ATUALIZACAO / SOLICITAR_EXCLUSAO
from intimai.servicos.solicitar_cadastro.certificado.certificado_solicitacao_cadastro import CertificadoSolicitacaoCadastro
from intimai.servicos.solicitar_atualizacao.certificado.certificado_solicita_atualizacao import CertificadoSolicitaAtualizacao
from intimai.servicos.solicitar_exclusao.certificado.certificado_solicitacao_exclusao import CertificadoSolicitacaoExclusao

# Servicos de TENTAR NOVAMENTE
from intimai.servicos.tentar_novamente.acao.acao_tenta_novamente import AcaoTentaNovamente


def main():
    # Inicializar o SDK com sua API token
    api_token = 'SEU_API_TOKEN_AQUI'
    sdk = Intimai(api_token)

    try:
        # ---------------------------------------------------------------
        # BUSCAR exemplos
        # ---------------------------------------------------------------

        # Buscar todos os autenticadores (paginado)
        resultado = sdk.servicos.buscar(AutenticadorBusca(), pagina=1)
        print('Autenticadores:', resultado)

        # Buscar um autenticador especifico pelo ID
        resultado = sdk.servicos.buscar(AutenticadorBusca(id=123))
        print('Autenticador 123:', resultado)

        # Buscar saldo de credito
        resultado = sdk.servicos.buscar(CreditoSaldoBusca())
        print('Saldo:', resultado)

        # Buscar dados do usuario
        resultado = sdk.servicos.buscar(UsuarioBusca())
        print('Usuario:', resultado)

        # Buscar tribunais com filtros
        resultado = sdk.servicos.buscar(
            TribunalBusca(),
            pagina=1,
            filtros={'filtros': {'nome': 'TJSP'}},
        )
        print('Tribunais:', resultado)

        # Buscar um código de ajuda: diz se o erro tem nova tentativa automática
        resultado = sdk.servicos.buscar(CodigoAjudaBusca(), 1, {'codigo': 606})
        print('Código 606:', resultado['data']['grupos'][0]['codigos'][0]['nova_tentativa'])

        # Ação com erro: se a nova tentativa for automática, não crie outra ação
        nova_tentativa = sdk.servicos.buscar(AcaoBusca(id=1))['data']['nova_tentativa']
        if nova_tentativa and nova_tentativa['automatica']:
            print('Nova tentativa automática:', nova_tentativa['mensagem'])
        elif nova_tentativa and nova_tentativa['situacao'] == SituacaoNovaTentativa.SEM_NOVA_TENTATIVA:
            print('Sem nova tentativa: corrija a causa antes de criar outra ação')

        # ---------------------------------------------------------------
        # CADASTRAR exemplos
        # ---------------------------------------------------------------

        # Cadastrar autenticador regular
        resultado = sdk.servicos.cadastrar(
            AutenticadorRegularCadastro(
                id_tribunal=1,
                oab={'numero': '123456', 'uf': 'SP'},
                usuario='meu_usuario',
                senha='minha_senha',
            )
        )
        print('Autenticador criado:', resultado)

        # Cadastrar escuta processual
        resultado = sdk.servicos.cadastrar(
            EscutaCadastro(
                id_autenticador=1,
                numero_do_processo='0000000-00.0000.0.00.0000',
                dias_de_captura=[Dia.SEGUNDA_FEIRA, Dia.QUARTA_FEIRA, Dia.SEXTA_FEIRA],
                horarios_de_captura=[Horario.OITO_HORAS, Horario.QUATORZE_HORAS],
            )
        )
        print('Escuta criada:', resultado)

        # Cadastrar webhook
        resultado = sdk.servicos.cadastrar(
            NotificacaoWebhookCadastro(
                tipo_acao=Acao.TIPO_INTIMACAO,
                verbo_http='POST',
                url='https://meu-sistema.com/webhook',
            )
        )
        print('Webhook criado:', resultado)

        # ---------------------------------------------------------------
        # ATUALIZAR exemplos
        # ---------------------------------------------------------------

        # Atualizar credenciais de autenticador regular
        resultado = sdk.servicos.atualizar(
            AutenticadorRegularAtualizacao(id=1, senha='nova_senha')
        )
        print('Autenticador atualizado:', resultado)

        # Atualizar dias/horarios da escuta
        resultado = sdk.servicos.atualizar(
            EscutaAtualizacao(
                id=1,
                dias_de_captura=[Dia.SEGUNDA_FEIRA, Dia.SEXTA_FEIRA],
                horarios_de_captura=[Horario.NOVE_HORAS],
            )
        )
        print('Escuta atualizada:', resultado)

        # ---------------------------------------------------------------
        # EXCLUIR exemplos
        # ---------------------------------------------------------------

        resultado = sdk.servicos.excluir(AndamentoExclusao(id=1))
        print('Andamento excluido:', resultado)

        # ---------------------------------------------------------------
        # SOLICITAR exemplos
        # ---------------------------------------------------------------

        # Solicitar atualizacao de andamento processual
        resultado = sdk.servicos.solicitar(AndamentoSolicitacao(id=1))
        print('Andamento solicitado:', resultado)

        # Solicitar consulta processual
        resultado = sdk.servicos.solicitar(
            ConsultaSolicitacao(
                id_autenticador=1,
                numero_do_processo='0000000-00.0000.0.00.0000',
            )
        )
        print('Consulta solicitada:', resultado)

        if resultado['data']['status'] == StatusAcao.AGUARDANDO_CONFIRMACAO:
            resultado = sdk.servicos.solicitar(AcaoConfirmarConsultaSolicitacao(resultado['data']['id']))
            print('Consulta confirmada:', resultado)

        resultado = sdk.servicos.buscar(CreditoConsumoMensalBusca(), 1, {'date': '2026-10'})
        print('Consumo mensal:', resultado)

        resultado = sdk.servicos.buscar(
            CapturaAgendadaBusca(),
            1,
            {'tipos': TipoCapturaAgendada.INTIMACAO, 'situacoes': SituacaoCapturaAgendada.NAO_EXECUTADA},
        )
        print('Capturas não executadas:', resultado)

        # Solicitar copia processual
        resultado = sdk.servicos.solicitar(
            CopiaSolicitacao(
                id_autenticador=1,
                numero_do_processo='0000000-00.0000.0.00.0000',
            )
        )
        print('Copia solicitada:', resultado)

        # Solicitar protocolo PJE com peticao e documentos
        peticao = Peticao(
            caminho='/caminho/para/peticao.pdf',
            tipo=1,
            descricao='Peticao inicial',
        )
        documento = Documento(
            caminho='/caminho/para/documento.pdf',
            ordem=1,
            tipo=2,
            descricao='Documento anexo',
        )
        resultado = sdk.servicos.solicitar(
            ProtocoloPjeSolicitacao(
                id_autenticador=1,
                numero_do_processo='0000000-00.0000.0.00.0000',
                tipo_documento_mensagem_geral=1,
                peticao=peticao,
                documentos=[documento],
            )
        )
        print('Protocolo PJE solicitado:', resultado)

        # ---------------------------------------------------------------
        # RESULTADO exemplos
        # ---------------------------------------------------------------

        resultado = sdk.servicos.resultado(AndamentoResultado(id=1))
        print('Resultado do andamento:', resultado)

        resultado = sdk.servicos.resultado(ConsultaResultado(id=1))
        print('Resultado da consulta:', resultado)

        # ---------------------------------------------------------------
        # CERTIFICADO exemplos
        # ---------------------------------------------------------------

        # Solicitar cadastro de certificado digital
        cert = Certificado(
            caminho_do_certificado='/caminho/para/certificado.pfx',
            senha='senha_do_certificado',
        )
        resultado = sdk.servicos.solicitar_cadastro(CertificadoSolicitacaoCadastro(cert))
        print('Certificado enviado para cadastro:', resultado)

        # Solicitar atualizacao de certificado
        resultado = sdk.servicos.solicitar_atualizacao(
            CertificadoSolicitaAtualizacao(id=1, certificado=cert)
        )
        print('Certificado enviado para atualizacao:', resultado)

        # Solicitar exclusao de certificado
        resultado = sdk.servicos.solicitar_exclusao(CertificadoSolicitacaoExclusao(id=1))
        print('Certificado excluido:', resultado)

        # ---------------------------------------------------------------
        # TENTAR NOVAMENTE
        # ---------------------------------------------------------------

        resultado = sdk.servicos.tentar_novamente(AcaoTentaNovamente(id=1))
        print('Acao tentada novamente:', resultado)

    except ExcecaoRequisicaoAPI as e:
        print(f'Erro na API (codigo {e.get_status()}): {e.get_mensagem()}')
        print('Detalhes:', e.para_dict())


if __name__ == '__main__':
    main()
