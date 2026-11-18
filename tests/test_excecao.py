from intimai import ExcecaoDoisFatores, ExcecaoLimiteDeRequisicoes, ExcecaoRequisicaoAPI
from intimai.servicos.buscar.acao.acao_busca import AcaoBusca
from tests.apoio import Caso


class TestExcecao(Caso):
    def falhar(self, status, corpo, headers=None) -> ExcecaoRequisicaoAPI:
        intimai = self.criar([(status, corpo, headers or {})])

        with self.assertRaises(ExcecaoRequisicaoAPI) as contexto:
            intimai.servicos.buscar(AcaoBusca())

        return contexto.exception

    def test_erro_de_validacao_expoe_status_corpo_e_erros(self):
        corpo = {'autenticacao_id': ['O campo autenticacao id é obrigatório.']}
        erro = self.falhar(422, corpo)

        self.assertIs(type(erro), ExcecaoRequisicaoAPI)
        self.assertEqual(erro.get_status(), 422)
        self.assertEqual(erro.code, 422)
        self.assertEqual(erro.get_corpo(), corpo)
        self.assertEqual(erro.get_erros(), corpo)
        self.assertEqual(erro.para_dict(), {'code': 422, 'error': corpo})

    def test_mensagem_da_excecao_nao_expoe_o_token(self):
        erro = self.falhar(422, {'error': 'x'})

        self.assertNotIn('token-teste', str(erro))

    def test_erro_de_negocio_com_codigo_nao_vira_erro_de_validacao(self):
        erro = self.falhar(422, {'error': 'Complete seus dados fiscais.', 'code': 613})

        self.assertEqual(erro.get_erros(), {})
        self.assertEqual(erro.get_mensagem(), 'Complete seus dados fiscais.')
        self.assertEqual(erro.get_corpo()['code'], 613)

    def test_limites_do_plano_certificado_e_saldo_trazem_a_mensagem_da_api(self):
        self.assertEqual(self.falhar(457, {'error': 'Limite por hora atingido.'}).get_status(), 457)
        self.assertEqual(self.falhar(458, {'error': 'Certificado inválido.'}).get_status(), 458)

        saldo = self.falhar(459, {'error': 'Você não possui saldo suficiente'})
        self.assertEqual(saldo.get_status(), 459)
        self.assertEqual(saldo.get_mensagem(), 'Você não possui saldo suficiente')

    def test_401_de_2fa_vira_excecao_dois_fatores(self):
        for mensagem in ['Código 2FA obrigatório', 'Código 2FA inválido', '2FA ativado: conclua o cadastro no painel']:
            erro = self.falhar(401, {'data': {'error': True, 'message': mensagem}})

            self.assertIsInstance(erro, ExcecaoDoisFatores)
            self.assertEqual(erro.get_status(), 401)
            self.assertEqual(erro.get_mensagem(), mensagem)

    def test_401_de_token_invalido_nao_e_de_2fa(self):
        erro = self.falhar(401, {'data': {'error': True, 'message': 'Unauthenticated'}})

        self.assertIs(type(erro), ExcecaoRequisicaoAPI)
        self.assertEqual(erro.get_mensagem(), 'Unauthenticated')

    def test_429_de_2fa_traz_retry_after(self):
        erro = self.falhar(429, {'data': {'error': True, 'message': 'Muitos códigos 2FA inválidos.'}}, {'Retry-After': '42'})

        self.assertIsInstance(erro, ExcecaoLimiteDeRequisicoes)
        self.assertEqual(erro.get_retry_after(), 42)

    def test_429_do_limite_geral_sem_retry_after(self):
        erro = self.falhar(429, {'message': 'Too Many Attempts.'})

        self.assertIsInstance(erro, ExcecaoLimiteDeRequisicoes)
        self.assertIsNone(erro.get_retry_after())
        self.assertEqual(erro.get_mensagem(), 'Too Many Attempts.')

    def test_corpo_que_nao_e_json_fica_como_texto(self):
        erro = self.falhar(500, 'Erro interno')

        self.assertEqual(erro.get_status(), 500)
        self.assertEqual(erro.get_corpo(), 'Erro interno')
        self.assertEqual(erro.get_erros(), {})
        self.assertEqual(erro.get_mensagem(), str(erro))

    def test_corpo_com_data_em_lista_nao_quebra(self):
        erro = self.falhar(404, {'data': []})

        self.assertEqual(erro.get_mensagem(), str(erro))
