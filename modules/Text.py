import time
import xml.etree.ElementTree as ET
import modules.Log as log

class Text():

	def __init__(self, loc):
		self.loc = loc
		log.log("Info  [ Succesfully initialised text module.")

	@log.log_on_error
	def printTi(self,text, timebl:float): #Виводе text з затримкою timebl (приклад: х(затримка)у(затримка)й(затримка))
		sptext=list(text.split()) #Ділимо текст на слова
		for word in sptext:
			for l in word: #Ділимо слово на букви
				print(l, end="", flush=True) #виводить слово
				time.sleep(timebl)
			print(" ", end="", flush=True) #пробел між словами
			time.sleep(timebl*2)
		print("") #нова строка

	@log.log_on_error
	def local(self, dop, tolocal): #tolocal - строка яку будемо локалізувати (писати треба наприклад як "dialog1/textzalupovicha1")
		tree = ET.parse(self.loc+dop)
		x = tree.find(tolocal)
		return x.text