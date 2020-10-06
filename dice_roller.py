import random


class Roller:
    @staticmethod
    def dy(y):
        """Rola um dado de y lados e retorna o resultado."""
        return random.randint(1, y)

    @staticmethod
    def xdy(x, y):
        """Rola x dados de y lados e retorna o resultado."""
        return sum(Roller.dy(y) for _ in range(1, x + 1))


class DiceSet:
    def __init__(self, nome: str):
        self.nome = nome
        self.dados_quantidade_dict = {}
        self.valores_ultima_rolagem_por_dado_dict = {}
        self.simulador_estatistico = SimuladorEstatistico()

    def novo_dado(self, n_lados: int):
        if not isinstance(n_lados, int):
            raise ValueError(
                "Erro ao adicionar dado no DiceSet {}, o numero de lados deve ser dado em int.".format(self.nome))
        if n_lados in self.dados_quantidade_dict:
            self.dados_quantidade_dict[n_lados] += 1
        else:
            self.dados_quantidade_dict[n_lados] = 1

    def remover_tipo_dado(self, n_lados):
        if n_lados in self.dados_quantidade_dict:
            self.dados_quantidade_dict.pop(n_lados)
        else:
            raise ValueError(
                "Não da pra tirar algo que não esta la. aka não tem nenhum dado de '{}' lados para ser removido".format(
                    n_lados))

    def definir_quantidade_tipo_dado(self, n_dados, n_lados):
        if not isinstance(n_lados, int):
            raise ValueError(
                "Erro ao definir quantidade de dados no DiceSet {}, o numero de lados deve ser dado em int.".format(
                    self.nome))
        self.dados_quantidade_dict[n_lados] = n_dados

    def rolar_dados(self):
        return sum(Roller.xdy(n_dados, n_lados) for n_lados, n_dados in self.dados_quantidade_dict.items())

    def rolar_dados_individualmente(self):
        soma = 0
        self.valores_ultima_rolagem_por_dado_dict = {}
        for n_lados, n_dados in self.dados_quantidade_dict.items():
            dados = []
            for _ in range(n_dados):
                rolada = Roller.dy(n_lados)
                dados.append(rolada)
                soma += rolada
            self.valores_ultima_rolagem_por_dado_dict[n_lados] = dados
        return soma


class SimuladorEstatistico:

    def __init__(self):
        self.amostragem = 10000

        self._ultima_simulacao = None

    def simular_estatisticas(self, dice_set):
        amostragem = self.amostragem

        simulacao = self.valor_medio_minimo_e_maximo(dice_set, tamanho_amostragem=amostragem)

        media = simulacao[0]
        valor_minimo = simulacao[1]
        valor_maximo = simulacao[2]
        # Não adicionado por evidente aumento no tempo de simulação para calcula-lo de [a] para [2a] onde a é o tempo relativo a amostragem
        desvio_padrao = None

        self._ultima_simulacao = {"amostragem": amostragem, "media": media, "valor_minimo": valor_minimo, "valor_maximo": valor_maximo}
        return self._ultima_simulacao

    @property
    def ultima_simulacao(self):
        if self._ultima_simulacao is not None:
            return self._ultima_simulacao
        else:
            raise ValueError(
                "Você deve criar uma simulação com o método 'simular_estatisticas' antes de poder pegar o resultado"
                "da ultima simulação.")

    @staticmethod
    def valor_medio_minimo_e_maximo(dice_set, tamanho_amostragem):
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


class Mesa:
    def __init__(self):
        self._dice_sets = []

    def novo_dice_set(self, ds: DiceSet):
        if isinstance(ds, DiceSet):
            self._dice_sets.append(ds)
        else:
            raise ValueError("Uma mesa pode apenas conter DiceSets.")

    def remover_dice_set(self, ds):
        if isinstance(ds, DiceSet):
            if ds in self._dice_sets:
                self._dice_sets.remove(ds)
            else:
                raise ValueError("Não é possível remover da mesa um diceset que não esta lá.")
        else:
            raise ValueError("Uma mesa pode apenas conter DiceSets.")

    def pegar_dice_sets(self):
        return self._dice_sets
