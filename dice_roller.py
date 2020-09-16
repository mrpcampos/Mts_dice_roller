import random


class Roller:
    @staticmethod
    def dx(x_lados):
        """Rola um dado de x lados e retorna o resultado."""
        return random.randint(1, x_lados)

    @staticmethod
    def xdy(x, y):
        """Rola x dados de y lados e retorna o resultado."""
        return sum(Roller.dx(y) for _ in range(1, x + 1))


class DiceSet:
    def __init__(self):
        self._dict_dados_quantidade = {}
        self.dict_valores_ultima_rolagem = {}

    def novo_dado(self, n_lados):
        if n_lados in self._dict_dados_quantidade:
            self._dict_dados_quantidade[n_lados] += 1
        else:
            self._dict_dados_quantidade[n_lados] = 1

    def remover_tipo_dado(self, n_lados):
        if n_lados in self._dict_dados_quantidade:
            self._dict_dados_quantidade.pop(n_lados)
        else:
            raise ValueError(
                "Não da pra tirar algo que não esta la. aka não tem nenhum dado de '{}' lados para ser removido".format(
                    n_lados))

    def definir_quantidade_tipo_dado(self, n_dados, n_lados):
        self._dict_dados_quantidade[n_lados] = n_dados

    def rolar_dados(self):
        return sum(Roller.xdy(n_dados, n_lados) for n_lados, n_dados in self._dict_dados_quantidade.items())

    def rolar_dados_individualmente(self):
        soma = 0
        self.dict_valores_ultima_rolagem = {}
        for n_lados, n_dados in self._dict_dados_quantidade.items():
            dados = []
            for _ in range(1, n_dados + 1):
                rolada = Roller.dx(n_lados)
                dados.append(rolada)
                soma += rolada
            self.dict_valores_ultima_rolagem[n_lados] = dados
        return soma


class VerificadorEstatistico:
    @staticmethod
    def valor_medio_maximo_e_minimo(dice_set, tamanho_amostragem):
        """Retorna um set contendo o valor médio, máximo e minimo obtido em todas as rolagens."""

        if not isinstance(dice_set, DiceSet) or tamanho_amostragem < 1:
            raise ValueError("Amostragem deve ser maior que zero e um conjunto de dados deve ser definido.")

        rolada_inalgural = dice_set.rolar_dados()
        soma_total = rolada_inalgural
        valor_minimo = rolada_inalgural
        valor_maximo = rolada_inalgural

        for _ in range(1, tamanho_amostragem):
            rolada = dice_set.rolar_dados()
            soma_total += rolada
            if rolada > valor_maximo:
                valor_maximo = rolada
            elif rolada < valor_minimo:
                valor_minimo = rolada

        media = soma_total / tamanho_amostragem
        return media, valor_maximo, valor_minimo
