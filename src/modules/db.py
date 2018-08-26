# -*- coding: Latin-1 -*-

#Autor: Israel Gomes
#Data: 26/08/2018

import sqlite3
"""Classes relacionada ao banco de dados"""
class Database(object):
	"Classe Singleton para conexao com banco de dados Sqlite3"
	def __new__(self):
		if not hasattr(self, "_instance"):
			self._instance = super(Database, self).__new__(self)
			try:
				self.db = sqlite3.connect("..\Forms\src\databases\database.db")
				self.cursor = self.db.cursor()
				self.execute = self.cursor.execute
				self.fetchall = self.cursor.fetchall
				self.fetchone = self.cursor.fetchone
				print("\n\nBanco conectado com sucesso"+ str(id(self._instance)))
			except: 
				print("Não foi possível conectar Banco de dados")

		return self._instance

	def __init__(self):
		print("\nClasse Database inicializada com sucesso"+ str(id(self)))

	def getAllElemments(self):
		self.execute("select id, nome, tipo, multilinha from elementos")
		return self.fetchall()

	def getAllInfoForms(self):
		"""Retorna as informacoes dos formularios existentes no banco"""
		self.execute("select * from formularios")
		return self.fetchall()

	def getInfoFormByName(self, name_form):
		"""Retorna a informacao do formulario informando o nome do formulario"""
		query = "select * from formularios where nome_formulario = '{}'".format(name_form)
		self.execute(query)
		return self.fetchall()

	def getInfoFormById(self, id_form):
		"""Retorna a tabela que representa o id identificador de formulario informado"""
		query = "select * from formularios where id = {}".format(id_form)
		#print(query)
		self.execute(query)
		return self.fetchall()

	def getRecordTableByNameTableAndId(self, name_table, id_record):
		"""Retorna o registro da tabela
		 informado que é igual ao id informado"""

		query = "select * from {} where id_ = {}".format(name_table, id_record)
		#print(query)
		self.execute(query)
		return self.fetchall()

	def getAllDataFormByNameTable(self, name_table):
		"""Retorna todos os registros da tabela informando
		o nome da tabela"""

		query = "select * from {}".format(name_table)
		#print(query)
		self.execute(query)
		return self.fetchall()

	def getAllDataFormByNameForm(self, name_form):
		"""Retorna informacoes do formulario informando
		o nome identificador do formulario"""

		# Retorna id, nome_formulario, descricao, nome_tabela
		info_form = self.getFormByName(name_form)
		table_name = info_form[3]
		data_form = self.getAllDataTableByNameForm(name_form)
		return data_form

	def getAllDataFormByIdForm(self, id_form):
		"""Retorna informacoes do formulario informando
		o id identificador do formulario"""

		# Retorna id, nome_formulario, descricao, nome_tabela
		info_form = self.getFormByName(name_form)
		table_name = info_form[0]
		data_form = self.getAllDataTableByNameForm(name_form)
		return data_form