# -*- coding: cp1252 -*-
from Tkinter import *
from utilities import savePhoto, renderPhoto, createVarByTextWidget

from os import path

class TabInfoApp:
	def __init__(self, master, eventWhenChangeValue):
		"""
		master: Frame que contem a aba InfoApp
		eventWhenChangeValue: Evento que será chamado quando o valor da variável de controle mudar
		"""
		self.master = master
		self.eventWhenChangeValue = eventWhenChangeValue

		self.defineVars()
		self.defineFonts()
	
	def defineVars(self):
		self.nameFormVar = StringVar()
		self.pathImageFormVar = StringVar()
		self.nameFormVar.trace("w", self.eventWhenChangeValue)
		self.pathImageFormVar.trace("w", self.eventWhenChangeValue)
	
	def defineFonts(self):
		"Variaveis de fonte globais para estética padrão da aplicação"
		self.font = ("Arial", 13)
		self.fontMin = ("Arial", 10)
		self.fontMax = ("Arial", 15)
	
	def createAba(self):
		"Cria a aba InfoApp"
		frame = Frame(self.master)
		Label(frame, text="Crie seu App aqui", font=self.font)\
		.grid(row=0, column=0, columnspan=5)

		Label(frame, text="Nome", font=self.fontMin).grid(row=1, column=0)
		inputName = Entry(frame, font=self.fontMin, textvariable=self.nameFormVar)
		inputName.grid(row=1, column=1, pady=10, sticky=W+E+N+S)
		#inputName.bind("<KeyPress>", self.checkAbaInfoAppCompleted)

		Label(frame, text="Descrição", font=self.fontMin).grid(row=2, column=0)
		textWidget = Text(frame, pady=10, font=self.fontMin, width=50, height=3)
		textWidget.grid(row=2, column=1, sticky=W+E+N+S)
		self.descriptionFormVar = createVarByTextWidget(textWidget)

		self.imageWidget = Label(frame, padx=10, pady=10, background="lightcyan", anchor=N)
		self.imageWidget.grid(row=1, column=2, rowspan=2, sticky=W+E+N+S, padx=10, pady=10)

		Label(frame, padx=10, pady=10, background="lightcyan", font=self.fontMin, textvariable=self.pathImageFormVar)\
		.grid(row=3, column=1, sticky=W+E+N+S)
		Button(frame, font=self.fontMin, text="Procurar Imagem", command=self.actionChoiseImageInfoApp)\
		.grid(row=3, column=2, padx=10, pady=10)

		self.buttonNext = Button(frame, state="disabled", font=self.fontMin, text="Prosseguir")
		self.buttonNext.grid(row=4, column=1, padx=20, pady=15)
		return frame

	def setPersonValuesWidgets(self):
		"FUNCAO DESENVOLVEDOR: Preenche com valores personalizados"
		self.nameFormVar.set("Eventos Mensais")
		self.descriptionFormVar.set("Eventos e palestrar de tecnologia que estão perto de ocorrer no ano de 2018.")
		self.actionChoiseImageInfoApp("images/iconsApps/video.png")#Define a imagem que representara o app
		#self.cleanAbaInfoApp()

	def setDefaultValuesWidgets(self):
		"Preeche com valores padroes da aplicacao"
		self.pathImageFormVar.set("link da imagem")

	def checkAbaCompleted(self):
		if self.nameFormVar.get() and self.pathImageFormVar.get() != "link da imagem":
			return True
		else: return False

	def renderInputElement(self, master, widget_tkinter):
		"Renderiza os inputs dos elementos na tela para input do usuario"
		inputElementVar = None
		if widget_tkinter == "entry":
			inputElementVar = StringVar()
			inputElement = Entry(master, width=40, textvariable=inputElementVar, font=self.font)
		
		elif widget_tkinter == "entry-date":
			inputElementVar = StringVar()
			inputElement = Entry(master, width=10, textvariable=inputElementVar, font=self.font)
			inputElement.config(validate="key", validatecommand=(self.validadeDateReg, '%i','%P', '%S', '%s'))

		elif widget_tkinter == "entry-phone":
			inputElementVar = StringVar()
			inputElement = Entry(master, width=15, textvariable=inputElementVar, font=self.font)
			inputElement.config(validate="key", validatecommand=(self.validadePhoneReg, '%i','%P', '%S', '%s'))

                elif widget_tkinter == "spinbox":
			inputElementVar = StringVar()
			inputElement = Spinbox(master, width=5, textvariable=inputElementVar, font=self.font)
		
		elif widget_tkinter == "text":
			inputElement = Text(master, width=40, height=4, font=self.font)
			inputElementVar = createVarByTextWidget(inputElement)

		elif widget_tkinter == "option-box":
			pass			

		inputElement.pack(side=LEFT, padx=10, pady=10)

		return (inputElement, inputElementVar)

	def actionChoiseImageInfoApp(self, path_origin=None):
		"Escolhe imagem atravez de acao ou atraves de chamada call"
		if path_origin == "": #Limpa todas as informacoes referentes a imagem e apaga
			self.imageWidget["image"] = None
			self.imageWidget["background"] = "grey"
			self.pathImageFormVar.set("")
		#Escolhe a imagem em determinado diretorio
		elif path_origin == None: path_origin = tkFileDialog.askopenfilename(initialdir = "/",title = "Selecione o Arquivo", filetypes = (("Arquivos jpeg", "*.jpg"), ("Arquivos png", "*.png"),("Todos arquivos", "*.*")))
		
		if path_origin:
			file_name = path.basename(path_origin)
			self.pathImageFormVar.set("images/iconsApps/"+file_name)

			path_origin = path_origin.encode("latin-1")
			path_destiny = ("images/iconsApps/"+file_name).encode("latin-1")
			
			print(path_origin, path_destiny, type(savePhoto))

			savePhoto(path_origin, path_destiny, (100, 100))
			image = renderPhoto(path_destiny, (100, 100))
			self.imageWidget["image"] = image
			self.imageWidget["background"] = "SystemButtonFace"

	def cleanAbaInfoApp(self):
		"Limpa todas as informacoes da aba InfoApp"
		self.nameFormVar.set("")
		self.descriptionFormVar.set("")
		self.actionChoiseImageInfoApp("")