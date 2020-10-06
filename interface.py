import wx
import wx.xrc
import wx.adv
import tentativa_separando_classes
import dice_roller

dados_permitidos = [2, 4, 6, 8, 10, 12, 20, 100]
# Traduzido para como o wxFormBuilder escreve
# dados_permitidos = [u"d4", u"d6", u"d8", u"d10", u"d12", u"d20", u"d100"]

# Removido porque a interface ficou responsiva sem querer
tamanhos = [(1024, 576), (1280, 720), (1600, 900)]


# _tamanho_escolhido = tamanhos[0]

class FramePrincipal(tentativa_separando_classes.FramePrincipal):

    def __init__(self, parent, title: str, size: wx.Size, mesa=None):
        super().__init__(parent)
        self.SetTitle(title)
        self.SetSize(size)

        # Variáveis de controle
        self.diceset_por_nome_dict = {}

        if not mesa:
            self.adicionar_dice_set("Novo DiceSet")

    def selecao_diceset_event(self, event):
        event.Skip()

    def salvar_menu_action(self, event):
        event.Skip()

    def abrir_menu_action(self, event):
        event.Skip()

    def config_tamanho_janela_event(self, event):
        event.Skip()

    def adicionar_diceset_event(self, event):
        dialog_nome = wx.TextEntryDialog(self, message="Escolha um nome para seu DiceSet:", caption="Novo DiceSet")
        dialog_nome.ShowModal()
        resposta_dialog_nome = dialog_nome.GetValue()
        if resposta_dialog_nome and resposta_dialog_nome in self.diceset_por_nome_dict:
            resposta_deve_sobrescrever = wx.MessageDialog(self,
                                                          "Já existe um DiceSet com esse nome, deseja sobrescreve-lo?",
                                                          "Sobrescrever DiceSet",
                                                          style=wx.YES_NO).ShowModal()
            resposta_deve_sobrescrever = True if resposta_deve_sobrescrever == wx.ID_YES else False
            if resposta_deve_sobrescrever:
                self.remover_diceset(self.diceset_por_nome_dict[resposta_dialog_nome])
            else:
                resposta_dialog_nome = ''
        if resposta_dialog_nome:
            self.adicionar_dice_set(resposta_dialog_nome)

    def adicionar_dice_set(self, dice_set: (str, dice_roller.DiceSet)):
        """
            Adiciona um novo DiceSet a lista de DiceSets, tenha em mente que esse metodo irá sobrescrever um
            DiceSet antigo com o mesmo nome.
        :param dice_set: String com um nome para um novo diceset, ou um diceset ja criado que será adicionado a tela
        """

        if isinstance(dice_set, str):
            diceset_nome = dice_set
            dice_set = dice_roller.DiceSet(diceset_nome)
        elif isinstance(dice_set, dice_roller.DiceSet):
            diceset_nome = dice_set.nome
        else:
            raise ValueError(
                "Para adicionar um diceset a tela deve-se ou passar um nome para ele, ou passar um DiceSet ja "
                "existente.")
        # Criando o Panel
        novo_diceset_panel = DiceSetPanel(self.dice_set_listbook, dice_set)

        # Definindo variável de controle
        self.diceset_por_nome_dict[diceset_nome] = dice_set

        # Adicionando na lista de escolhas
        self.dice_set_listbook.AddPage(novo_diceset_panel, diceset_nome, True)

    def remover_diceset_event(self, event):
        dice_set = self.dice_set_listbook.CurrentPage.dice_set
        confirmar_delete = wx.MessageDialog(self,
                                            "Tem certeza que deseja remover o DiceSet '{}'?\n"
                                            "Isso não poderá ser desfeito!".format(dice_set.nome), "Deletar DiceSet",
                                            style=wx.YES_NO).ShowModal()
        if confirmar_delete == wx.ID_YES:
            self.remover_diceset(dice_set)

    def remover_diceset(self, dice_set):
        # Removendo da Variável de controle
        self.diceset_por_nome_dict.pop(dice_set.nome)

        # Removendo da Tela
        pagina_para_deletar = self.dice_set_listbook.GetSelection()
        self.dice_set_listbook.DeletePage(pagina_para_deletar)


class DiceSetPanel(tentativa_separando_classes.DiceSetPanel):

    def __init__(self, parent, dice_set: dice_roller.DiceSet):
        super().__init__(parent)

        self.statistics_loader_indicator_animation_ctrl.Hide()

        # Variáveis de controle
        self.dice_set = dice_set
        self.xdypanel_por_tipodado_dict = {}

    def adicionar_dado_event(self, event):
        tipo_dado = self.adicionar_dado_combobox.GetStringSelection()
        self.adicionar_dado(tipo_dado)

    def adicionar_dado(self, tipo_dado):
        if not isinstance(tipo_dado, str):
            raise ValueError("Não foi possível adicionar o tipo de dado, tipo_dado deve ser do tipo string.")
        if tipo_dado not in self.xdypanel_por_tipodado_dict:
            # Criando Panel do tipo de dado
            xdy_panel = XdyPanel(self.dados_escolhidos_panel, tipo_dado)

            # Atualizando variavel de controle
            self.xdypanel_por_tipodado_dict[tipo_dado] = xdy_panel

            # Atualizando tela
            # (Como no wxFormBuilder os sizers não são adicionados como variavel de classe, só local,
            # tive que fazer isso para pegar o sizer onde o novo panel deve ser adicionado)
            sizer_dados_escolhidos = self.dados_escolhidos_panel.GetSizer().Children[1].GetSizer()
            sizer_dados_escolhidos.Add(xdy_panel, 0, wx.ALL, 5)

            self.dados_escolhidos_panel.Layout()
        else:
            # Atualizando FrontEnd
            spin_crtl = self.xdypanel_por_tipodado_dict[tipo_dado].numero_x_dados_spinctrl
            spin_crtl.Value += 1

    def sincronizar_quantidade_dados(self):
        """
            Esse método iguala a quantidade de dados na tela com a quantidade de dados no backend, deve ser chamado
            antes de todos os métodos que interajam com o conjunto de dados.
        """
        for tipo_dado, panel_dados in self.xdypanel_por_tipodado_dict.items():
            self.dice_set.definir_quantidade_tipo_dado(panel_dados.quantidade_dados(), int(tipo_dado.replace("d", "")))

    def rolar_dados_event(self, event):
        self.sincronizar_quantidade_dados()
        self.rolar_dados()

    def rolar_dados(self):
        dice_set = self.dice_set
        dados_rolados_panel = self.dados_rolados_scrollable_panel
        # (Como no wxFormBuilder os sizers não são adicionados como variavel de classe, só local,
        # tive que fazer isso para pegar o sizer onde o novo panel deve ser adicionado)
        dados_rolados_sizer = dados_rolados_panel.GetSizer().Children[1].GetSizer()

        # Impedindo que a janela seja redesenhada até que todos os elementos sejam criados e adicionados a ela
        dados_rolados_panel.Freeze()

        # Limpando os elementos antigos
        dados_rolados_sizer.Clear(True)

        # Rolando os dados novamente e definindo o valor total
        self.valor_total_lbl.SetLabelText(str(dice_set.rolar_dados_individualmente()))

        panel_list = []
        for t_dado, list_results in dice_set.valores_ultima_rolagem_por_dado_dict.items():
            for resultado in list_results:
                resultado_panel = DadoRoladoPanel(dados_rolados_panel, 'd' + str(t_dado), str(resultado))
                panel_list.append((resultado_panel, 0, wx.ALL, 5))

        dados_rolados_sizer.AddMany(panel_list)
        self.Layout()

        # Voltando a atualizar a janela
        dados_rolados_panel.Thaw()

    def definir_valor_amostragem_spinctrl(self, event):
        atualizar_valor_spin_ctrl(self.amostragem_spinCtrl)

    def syncronizar_amostragem(self):
        self.dice_set.simulador_estatistico.amostragem = self.amostragem_spinCtrl.Value

    def calcular_event(self, event):
        self.sincronizar_quantidade_dados()
        self.syncronizar_amostragem()

        self.calcular_simulacao()

    def calcular_simulacao(self):
        # self.statistics_loader_indicator_animation_ctrl.Show(True)
        valores_simulacao = self.dice_set.simulador_estatistico.simular_estatisticas(self.dice_set)
        # self.statistics_loader_indicator_animation_ctrl.Hide()

        self.valor_amostragem_lbl.SetLabelText(str(valores_simulacao["amostragem"]))
        self.valor_menor_valor_lbl.SetLabelText(str(valores_simulacao["valor_minimo"]))
        self.valor_maior_valor_lbl.SetLabelText(str(valores_simulacao["valor_maximo"]))
        self.valor_media_simulacao_lbl.SetLabelText(str(valores_simulacao["media"]))


class XdyPanel(tentativa_separando_classes.XdyPanel):
    def __init__(self, parent, tipo_dado):
        super().__init__(parent)
        self.identificador_tipo_dado_lbl.SetLabelText(tipo_dado)

    def definir_valor_spin_ctrl(self, event):
        """"""
        sc = self.numero_x_dados_spinctrl
        atualizar_valor_spin_ctrl(sc)

    def quantidade_dados(self):
        return self.numero_x_dados_spinctrl.Value


class DadoRoladoPanel(tentativa_separando_classes.DadoRoladoPanel):
    def __init__(self, parent, tipo_dado, quant_dado):
        super().__init__(parent)
        self.tipo_dado_lbl.SetLabelText(tipo_dado)
        self.resultado_dy_lbl.SetLabelText(quant_dado)


class DiceRollerApp(wx.App):
    def __init__(self):
        super().__init__(useBestVisual=True)
        self.main_frame = FramePrincipal(None, "Mts's Dice Roller", wx.Size(tamanhos[1]))
        self.main_frame.Show(True)


def atualizar_valor_spin_ctrl(spin_ctrl):
    valor_atual = spin_ctrl.Value
    maximo_permitido = spin_ctrl.GetMax()
    minimo_permitido = spin_ctrl.GetMin()

    if valor_atual < minimo_permitido:
        valor_atual = minimo_permitido
    elif valor_atual > maximo_permitido:
        valor_atual = maximo_permitido

    spin_ctrl.Value = valor_atual


if __name__ == "__main__":
    DiceRollerApp().MainLoop()
