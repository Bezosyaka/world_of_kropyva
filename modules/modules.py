import modules.Text as text, modules.Saves as saves
import arrow
import os

class KropyvaException(BaseException):
	pass

class Modules():

	def __init__(self, gname:str, ver:str, aut:str, loc:str):
		self.name=gname
		self.version=ver
		self.author=aut
		self.loc = loc
		self.Saves = saves.Saves(self.loc)
		self.Text = text.Text(self.loc)