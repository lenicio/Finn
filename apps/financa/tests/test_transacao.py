from django.test import TestCase
from apps.financa.models.transacao import Transacao
from datetime import datetime


class TestTransacao(TestCase):


    def setUp(self):
        self.receita = Transacao.objects.create(
            descricao = 'Salário',
            valor = 3000,
            tipo_transacao = 'R',
            status_transacao = 'E',
            data_transacao = datetime.strptime('2025-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        )

        self.despesa = Transacao.objects.create(
            descricao = 'Aluguel',
            valor = 1000,
            tipo_transacao = 'D',
            status_transacao = 'E',
            data_transacao = datetime.strptime('2025-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        )


    def test_valida_a_criacao_das_transacoes(self):
        """
        Testa o sucesso da criação/persistência das transações
        """
        self.assertEqual(self.receita.descricao, 'Salário')
        self.assertEqual(self.receita.valor , 3000)
        self.assertEqual(self.receita.tipo_transacao , 'R')
        self.assertEqual(self.receita.status_transacao , 'E')
        self.assertEqual(self.receita.data_transacao , datetime.strptime('2025-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'))

        self.assertEqual(self.despesa.descricao, 'Aluguel')
        self.assertEqual(self.despesa.valor , 1000)
        self.assertEqual(self.despesa.tipo_transacao , 'D')
        self.assertEqual(self.despesa.status_transacao , 'E')
        self.assertEqual(self.despesa.data_transacao , datetime.strptime('2025-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'))
