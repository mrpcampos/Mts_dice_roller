# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class FramePrincipal
###########################################################################

class FramePrincipal ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1024,576 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		main_sizer = wx.BoxSizer( wx.VERTICAL )

		self.titulo_lbl = wx.StaticText( self, wx.ID_ANY, u"Mts's Dice Roller", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titulo_lbl.Wrap( -1 )

		self.titulo_lbl.SetFont( wx.Font( 24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.titulo_lbl.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )

		main_sizer.Add( self.titulo_lbl, 0, wx.ALL, 10 )

		adicioar_ou_remover_diceset_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.remover_diceset_btn = wx.Button( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( 24,25 ), 0 )
		self.remover_diceset_btn.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
		self.remover_diceset_btn.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		adicioar_ou_remover_diceset_sizer.Add( self.remover_diceset_btn, 0, wx.ALL, 1 )

		self.novo_diceset_btn = wx.Button( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 24,25 ), 0 )
		self.novo_diceset_btn.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
		self.novo_diceset_btn.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		adicioar_ou_remover_diceset_sizer.Add( self.novo_diceset_btn, 0, wx.ALL, 1 )


		main_sizer.Add( adicioar_ou_remover_diceset_sizer, 0, wx.EXPAND, 5 )

		self.dice_set_listbook = wx.Listbook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT )
		self.dice_set_listbook.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		self.dice_set_listbook.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )


		main_sizer.Add( self.dice_set_listbook, 1, wx.EXPAND, 1 )


		self.SetSizer( main_sizer )
		self.Layout()
		self.menubar = wx.MenuBar( 0 )
		self.arquivo_menu = wx.Menu()
		self.salvar_menuitem = wx.MenuItem( self.arquivo_menu, wx.ID_ANY, u"Salvar"+ u"\t" + u"CTRL + S", wx.EmptyString, wx.ITEM_NORMAL )
		self.arquivo_menu.Append( self.salvar_menuitem )

		self.abrir_menuitem = wx.MenuItem( self.arquivo_menu, wx.ID_ANY, u"Abrir"+ u"\t" + u"CTRL + A", wx.EmptyString, wx.ITEM_NORMAL )
		self.arquivo_menu.Append( self.abrir_menuitem )

		self.menubar.Append( self.arquivo_menu, u"Arquivo" )

		self.config_menu = wx.Menu()
		self.config_tamanho_janela_menuitem = wx.MenuItem( self.config_menu, wx.ID_ANY, u"Tamanho da Tela", wx.EmptyString, wx.ITEM_NORMAL )
		self.config_menu.Append( self.config_tamanho_janela_menuitem )

		self.menubar.Append( self.config_menu, u"Configurações" )

		self.SetMenuBar( self.menubar )


		self.Centre( wx.BOTH )

		# Connect Events
		self.remover_diceset_btn.Bind( wx.EVT_BUTTON, self.remover_diceset_event )
		self.novo_diceset_btn.Bind( wx.EVT_BUTTON, self.adicionar_diceset_event )
		self.dice_set_listbook.Bind( wx.EVT_LISTBOOK_PAGE_CHANGED, self.selecao_diceset_event )
		self.Bind( wx.EVT_MENU, self.salvar_menu_action, id = self.salvar_menuitem.GetId() )
		self.Bind( wx.EVT_MENU, self.abrir_menu_action, id = self.abrir_menuitem.GetId() )
		self.Bind( wx.EVT_MENU, self.config_tamanho_janela_event, id = self.config_tamanho_janela_menuitem.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def remover_diceset_event( self, event ):
		event.Skip()

	def adicionar_diceset_event( self, event ):
		event.Skip()

	def selecao_diceset_event( self, event ):
		event.Skip()

	def salvar_menu_action( self, event ):
		event.Skip()

	def abrir_menu_action( self, event ):
		event.Skip()

	def config_tamanho_janela_event( self, event ):
		event.Skip()


###########################################################################
## Class DiceSetPanel
###########################################################################

class DiceSetPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.BORDER_SUNKEN|wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.SetBackgroundColour( wx.Colour( 143, 143, 143 ) )

		dice_set_main_sizer = wx.BoxSizer( wx.VERTICAL )

		dice_set_config_e_rolagem_sizer = wx.BoxSizer( wx.HORIZONTAL )

		dice_set_config_sizer = wx.BoxSizer( wx.VERTICAL )

		novo_dado_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.adicionar_dado_lbl = wx.StaticText( self, wx.ID_ANY, u"Adicionar: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.adicionar_dado_lbl.Wrap( -1 )

		novo_dado_sizer.Add( self.adicionar_dado_lbl, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.LEFT|wx.TOP, 5 )

		adicionar_dado_comboboxChoices = [ u"d4", u"d6", u"d8", u"d10", u"d12", u"d20", u"d100" ]
		self.adicionar_dado_combobox = wx.ComboBox( self, wx.ID_ANY, u"d8", wx.DefaultPosition, wx.DefaultSize, adicionar_dado_comboboxChoices, wx.CB_DROPDOWN|wx.CB_READONLY )
		self.adicionar_dado_combobox.SetSelection( 2 )
		novo_dado_sizer.Add( self.adicionar_dado_combobox, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )

		self.adicionar_dado_btn = wx.Button( self, wx.ID_ANY, u"↓", wx.DefaultPosition, wx.Size( 24,25 ), 0 )
		self.adicionar_dado_btn.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.adicionar_dado_btn.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		novo_dado_sizer.Add( self.adicionar_dado_btn, 0, wx.FIXED_MINSIZE|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )

		self.ghost_label2 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ghost_label2.Wrap( -1 )

		self.ghost_label2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		novo_dado_sizer.Add( self.ghost_label2, 0, wx.ALL, 5 )


		dice_set_config_sizer.Add( novo_dado_sizer, 0, 0, 5 )

		self.dados_escolhidos_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )
		self.dados_escolhidos_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )

		dados_escolhidos_outer_sizer = wx.BoxSizer( wx.VERTICAL )


		dados_escolhidos_outer_sizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		dados_escolhidos_inner_sizer = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )


		dados_escolhidos_outer_sizer.Add( dados_escolhidos_inner_sizer, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 5 )


		dados_escolhidos_outer_sizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.dados_escolhidos_panel.SetSizer( dados_escolhidos_outer_sizer )
		self.dados_escolhidos_panel.Layout()
		dados_escolhidos_outer_sizer.Fit( self.dados_escolhidos_panel )
		dice_set_config_sizer.Add( self.dados_escolhidos_panel, 1, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

		self.ghost_label = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ghost_label.Wrap( -1 )

		self.ghost_label.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		dice_set_config_sizer.Add( self.ghost_label, 0, wx.ALL, 5 )


		dice_set_config_e_rolagem_sizer.Add( dice_set_config_sizer, 1, wx.RIGHT|wx.EXPAND, 5 )

		btn_rolar_sizer = wx.BoxSizer( wx.VERTICAL )


		btn_rolar_sizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.rolar_btn = wx.Button( self, wx.ID_ANY, u"Rolar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rolar_btn.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.rolar_btn.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		btn_rolar_sizer.Add( self.rolar_btn, 0, wx.ALIGN_CENTER, 5 )


		btn_rolar_sizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		dice_set_config_e_rolagem_sizer.Add( btn_rolar_sizer, 0, wx.EXPAND, 5 )

		resultado_rolagem_unica_sizer = wx.BoxSizer( wx.VERTICAL )

		self.ghost_label1 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ghost_label1.Wrap( -1 )

		self.ghost_label1.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		resultado_rolagem_unica_sizer.Add( self.ghost_label1, 0, wx.ALL, 5 )

		self.dados_rolados_scrollable_panel = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE|wx.VSCROLL )
		self.dados_rolados_scrollable_panel.SetScrollRate( 5, 5 )
		self.dados_rolados_scrollable_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )

		resultados_individuais_outter_sizer = wx.BoxSizer( wx.VERTICAL )


		resultados_individuais_outter_sizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		resutados_individuais_inner_sizer = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )


		resultados_individuais_outter_sizer.Add( resutados_individuais_inner_sizer, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 5 )


		resultados_individuais_outter_sizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.dados_rolados_scrollable_panel.SetSizer( resultados_individuais_outter_sizer )
		self.dados_rolados_scrollable_panel.Layout()
		resultados_individuais_outter_sizer.Fit( self.dados_rolados_scrollable_panel )
		resultado_rolagem_unica_sizer.Add( self.dados_rolados_scrollable_panel, 2, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )

		valor_total_rolagem_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.identificador_valor_total_lbl = wx.StaticText( self, wx.ID_ANY, u"Total = ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.identificador_valor_total_lbl.Wrap( -1 )

		self.identificador_valor_total_lbl.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		valor_total_rolagem_sizer.Add( self.identificador_valor_total_lbl, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.LEFT|wx.TOP, 5 )

		self.valor_total_lbl = wx.StaticText( self, wx.ID_ANY, u"??", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valor_total_lbl.Wrap( -1 )

		self.valor_total_lbl.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		valor_total_rolagem_sizer.Add( self.valor_total_lbl, 0, wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER_VERTICAL, 5 )


		resultado_rolagem_unica_sizer.Add( valor_total_rolagem_sizer, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		dice_set_config_e_rolagem_sizer.Add( resultado_rolagem_unica_sizer, 1, wx.EXPAND|wx.LEFT, 5 )


		dice_set_main_sizer.Add( dice_set_config_e_rolagem_sizer, 1, wx.EXPAND, 5 )

		self.statistic_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )
		statistic_painel_main_sizer = wx.BoxSizer( wx.VERTICAL )

		self.statistic_config_panel = wx.Panel( self.statistic_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		statistic_config_main_sizer = wx.BoxSizer( wx.HORIZONTAL )

		statistic_choices_sizer = wx.StaticBoxSizer( wx.StaticBox( self.statistic_config_panel, wx.ID_ANY, u"Calcular Probabilidades" ), wx.HORIZONTAL )

		self.amostragem_choice_lbl = wx.StaticText( statistic_choices_sizer.GetStaticBox(), wx.ID_ANY, u"Amostragem: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.amostragem_choice_lbl.Wrap( -1 )

		statistic_choices_sizer.Add( self.amostragem_choice_lbl, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.LEFT|wx.TOP, 5 )

		self.amostragem_spinCtrl = wx.SpinCtrl( statistic_choices_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS|wx.SP_WRAP, 10, 100000, 10000 )
		self.amostragem_spinCtrl.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.amostragem_spinCtrl.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		statistic_choices_sizer.Add( self.amostragem_spinCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		statistic_config_main_sizer.Add( statistic_choices_sizer, 1, wx.EXPAND, 5 )

		self.statistic_calcular_resultados_btn = wx.Button( self.statistic_config_panel, wx.ID_ANY, u"Calcular", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.statistic_calcular_resultados_btn.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		statistic_config_main_sizer.Add( self.statistic_calcular_resultados_btn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10 )

		self.statistics_loader_indicator_animation_ctrl = wx.adv.AnimationCtrl( self.statistic_config_panel, wx.ID_ANY, wx.adv.NullAnimation, wx.DefaultPosition, wx.DefaultSize, wx.adv.AC_DEFAULT_STYLE )
		self.statistics_loader_indicator_animation_ctrl.LoadFile( u"C:\\Projetos\\DiceRoller\\resources\\LoadingIndicator.gif" )

		self.statistics_loader_indicator_animation_ctrl.Play()
		self.statistics_loader_indicator_animation_ctrl.SetBackgroundColour( wx.Colour( 143, 143, 143 ) )
		self.statistics_loader_indicator_animation_ctrl.Hide()

		statistic_config_main_sizer.Add( self.statistics_loader_indicator_animation_ctrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT|wx.TOP, 5 )


		self.statistic_config_panel.SetSizer( statistic_config_main_sizer )
		self.statistic_config_panel.Layout()
		statistic_config_main_sizer.Fit( self.statistic_config_panel )
		statistic_painel_main_sizer.Add( self.statistic_config_panel, 0, wx.EXPAND |wx.ALL, 5 )

		statistc_results_sizer = wx.GridSizer( 0, 3, 0, 0 )

		self.m_scrolledWindow2 = wx.ScrolledWindow( self.statistic_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE|wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		self.m_scrolledWindow2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )

		informacoes_estatisticas_sizer = wx.BoxSizer( wx.VERTICAL )

		info_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.name_amostragem_lbl = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Amostragem: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.name_amostragem_lbl.Wrap( -1 )

		info_sizer.Add( self.name_amostragem_lbl, 0, wx.ALL, 5 )

		self.valor_amostragem_lbl = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"??", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valor_amostragem_lbl.Wrap( -1 )

		info_sizer.Add( self.valor_amostragem_lbl, 0, wx.ALL, 5 )


		informacoes_estatisticas_sizer.Add( info_sizer, 0, wx.ALL|wx.EXPAND, 5 )

		media_simulacao_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.media_simulacao_lbl = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Média: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.media_simulacao_lbl.Wrap( -1 )

		media_simulacao_sizer.Add( self.media_simulacao_lbl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.valor_media_simulacao_lbl = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"??", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valor_media_simulacao_lbl.Wrap( -1 )

		media_simulacao_sizer.Add( self.valor_media_simulacao_lbl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		informacoes_estatisticas_sizer.Add( media_simulacao_sizer, 0, wx.ALL|wx.EXPAND, 5 )

		sem_nome1 = wx.BoxSizer( wx.HORIZONTAL )

		self.desvio_padrao_lbl = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Desvio Padrão: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.desvio_padrao_lbl.Wrap( -1 )

		sem_nome1.Add( self.desvio_padrao_lbl, 0, wx.ALL, 5 )

		self.valor_desvio_padrao_lbl = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"??", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valor_desvio_padrao_lbl.Wrap( -1 )

		sem_nome1.Add( self.valor_desvio_padrao_lbl, 0, wx.ALL, 5 )


		informacoes_estatisticas_sizer.Add( sem_nome1, 0, wx.ALL|wx.EXPAND, 5 )

		sem_nome2 = wx.BoxSizer( wx.HORIZONTAL )

		self.menor_valor_encontrado_lbl = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Menor valor: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.menor_valor_encontrado_lbl.Wrap( -1 )

		sem_nome2.Add( self.menor_valor_encontrado_lbl, 0, wx.ALL, 5 )

		self.valor_menor_valor_lbl = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"??", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valor_menor_valor_lbl.Wrap( -1 )

		sem_nome2.Add( self.valor_menor_valor_lbl, 0, wx.ALL, 5 )


		informacoes_estatisticas_sizer.Add( sem_nome2, 0, wx.ALL|wx.EXPAND, 5 )

		sem_nome3 = wx.BoxSizer( wx.HORIZONTAL )

		self.maior_valor_lbl = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Maior valor: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.maior_valor_lbl.Wrap( -1 )

		sem_nome3.Add( self.maior_valor_lbl, 0, wx.ALL, 5 )

		self.valor_maior_valor_lbl = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"??", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valor_maior_valor_lbl.Wrap( -1 )

		sem_nome3.Add( self.valor_maior_valor_lbl, 0, wx.ALL, 5 )


		informacoes_estatisticas_sizer.Add( sem_nome3, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_scrolledWindow2.SetSizer( informacoes_estatisticas_sizer )
		self.m_scrolledWindow2.Layout()
		informacoes_estatisticas_sizer.Fit( self.m_scrolledWindow2 )
		statistc_results_sizer.Add( self.m_scrolledWindow2, 1, wx.EXPAND |wx.ALL, 5 )

		self.statistic_grafico_painel_1 = wx.Panel( self.statistic_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )
		self.statistic_grafico_painel_1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )

		statistc_grafico_sizer_11 = wx.GridSizer( 0, 1, 0, 0 )

		self.aviso_feature_futura_lbl_11 = wx.StaticText( self.statistic_grafico_painel_1, wx.ID_ANY, u"Algum dia quem sabe um gráfico aqui", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL|wx.ST_ELLIPSIZE_END )
		self.aviso_feature_futura_lbl_11.Wrap( 120 )

		self.aviso_feature_futura_lbl_11.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		statistc_grafico_sizer_11.Add( self.aviso_feature_futura_lbl_11, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.statistic_grafico_painel_1.SetSizer( statistc_grafico_sizer_11 )
		self.statistic_grafico_painel_1.Layout()
		statistc_grafico_sizer_11.Fit( self.statistic_grafico_painel_1 )
		statistc_results_sizer.Add( self.statistic_grafico_painel_1, 1, wx.ALL|wx.EXPAND, 5 )

		self.statistic_grafico_panel_2 = wx.Panel( self.statistic_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )
		self.statistic_grafico_panel_2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.statistic_grafico_panel_2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )

		statistc_grafico_sizer_1 = wx.GridSizer( 0, 1, 0, 0 )

		self.aviso_feature_futura_lbl_1 = wx.StaticText( self.statistic_grafico_panel_2, wx.ID_ANY, u"Algum dia quem sabe um gráfico aqui", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL|wx.ST_ELLIPSIZE_END )
		self.aviso_feature_futura_lbl_1.Wrap( 120 )

		self.aviso_feature_futura_lbl_1.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		statistc_grafico_sizer_1.Add( self.aviso_feature_futura_lbl_1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.statistic_grafico_panel_2.SetSizer( statistc_grafico_sizer_1 )
		self.statistic_grafico_panel_2.Layout()
		statistc_grafico_sizer_1.Fit( self.statistic_grafico_panel_2 )
		statistc_results_sizer.Add( self.statistic_grafico_panel_2, 1, wx.EXPAND |wx.ALL, 5 )


		statistic_painel_main_sizer.Add( statistc_results_sizer, 3, wx.EXPAND, 5 )


		self.statistic_panel.SetSizer( statistic_painel_main_sizer )
		self.statistic_panel.Layout()
		statistic_painel_main_sizer.Fit( self.statistic_panel )
		dice_set_main_sizer.Add( self.statistic_panel, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( dice_set_main_sizer )
		self.Layout()
		dice_set_main_sizer.Fit( self )

		# Connect Events
		self.adicionar_dado_btn.Bind( wx.EVT_BUTTON, self.adicionar_dado_event )
		self.rolar_btn.Bind( wx.EVT_BUTTON, self.rolar_dados_event )
		self.amostragem_spinCtrl.Bind( wx.EVT_SPINCTRL, self.definir_valor_amostragem_spinctrl )
		self.amostragem_spinCtrl.Bind( wx.EVT_TEXT, self.definir_valor_amostragem_spinctrl )
		self.amostragem_spinCtrl.Bind( wx.EVT_TEXT_ENTER, self.definir_valor_amostragem_spinctrl )
		self.statistic_calcular_resultados_btn.Bind( wx.EVT_BUTTON, self.calcular_event )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def adicionar_dado_event( self, event ):
		event.Skip()

	def rolar_dados_event( self, event ):
		event.Skip()

	def definir_valor_amostragem_spinctrl( self, event ):
		event.Skip()



	def calcular_event( self, event ):
		event.Skip()


###########################################################################
## Class XdyPanel
###########################################################################

class XdyPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.BORDER_SIMPLE, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		xdy_sizer = wx.BoxSizer( wx.VERTICAL )

		self.identificador_tipo_dado_lbl = wx.StaticText( self, wx.ID_ANY, u"d12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.identificador_tipo_dado_lbl.Wrap( -1 )

		self.identificador_tipo_dado_lbl.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		xdy_sizer.Add( self.identificador_tipo_dado_lbl, 0, wx.TOP|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.tipo_multiplicador_separador_staticline = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.tipo_multiplicador_separador_staticline.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.tipo_multiplicador_separador_staticline.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		xdy_sizer.Add( self.tipo_multiplicador_separador_staticline, 0, wx.EXPAND, 0 )

		multiplicador_xd_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.indicador_multiplicacao_xd_lbl = wx.StaticText( self, wx.ID_ANY, u"x", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.indicador_multiplicacao_xd_lbl.Wrap( -1 )

		self.indicador_multiplicacao_xd_lbl.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		multiplicador_xd_sizer.Add( self.indicador_multiplicacao_xd_lbl, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.LEFT|wx.TOP, 5 )

		self.numero_x_dados_spinctrl = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 200, 1 )
		self.numero_x_dados_spinctrl.SetMinSize( wx.Size( 45,-1 ) )

		multiplicador_xd_sizer.Add( self.numero_x_dados_spinctrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.BOTTOM|wx.RIGHT|wx.TOP, 2 )


		xdy_sizer.Add( multiplicador_xd_sizer, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( xdy_sizer )
		self.Layout()
		xdy_sizer.Fit( self )

		# Connect Events
		self.numero_x_dados_spinctrl.Bind( wx.EVT_SPINCTRL, self.definir_valor_spin_ctrl )
		self.numero_x_dados_spinctrl.Bind( wx.EVT_TEXT, self.definir_valor_spin_ctrl )
		self.numero_x_dados_spinctrl.Bind( wx.EVT_TEXT_ENTER, self.definir_valor_spin_ctrl )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def definir_valor_spin_ctrl( self, event ):
		event.Skip()




###########################################################################
## Class DadoRoladoPanel
###########################################################################

class DadoRoladoPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		resultado_dy_sizer = wx.BoxSizer( wx.VERTICAL )

		self.resultado_dy_lbl = wx.StaticText( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resultado_dy_lbl.Wrap( -1 )

		self.resultado_dy_lbl.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		resultado_dy_sizer.Add( self.resultado_dy_lbl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.resultado_tipodado_divider_staticline = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		resultado_dy_sizer.Add( self.resultado_tipodado_divider_staticline, 0, wx.EXPAND |wx.ALL, 0 )

		self.tipo_dado_lbl = wx.StaticText( self, wx.ID_ANY, u"d12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tipo_dado_lbl.Wrap( -1 )

		self.tipo_dado_lbl.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		resultado_dy_sizer.Add( self.tipo_dado_lbl, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.RIGHT|wx.LEFT, 5 )


		self.SetSizer( resultado_dy_sizer )
		self.Layout()
		resultado_dy_sizer.Fit( self )

	def __del__( self ):
		pass


