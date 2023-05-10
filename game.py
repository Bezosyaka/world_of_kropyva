import modules.modules as m
import modules.Saves as s 
from modules.Log import *
import sys

def silent_exception_handler(exctype, value, traceback):
	print("FATAL! An error occured during completing code. Logs can be found in \"gamelog.log.\"")

sys.excepthook = silent_exception_handler #Ховаємо ексепшени

# s.newGame("locales/ua/")
# char = s.loadGame("locales/ua/")
# m.Modules.Text.printTi(str(char), 0.01)
#Поки що вимкнув бо нахуй?

localech = input("""Language:
1 - English
2 - Українська
""")
match localech:  #Обираємо локалізацію
	case"1":
		loc = "locales/en/"
	case "2":
		loc = "locales/ua/"
	case _:
		print("Ну ти й підор. Будеш грати українською.")
		loc = "locales/ua/"  

Engine = m.Modules("World Of Kropyva", "0.1", "Bezos", loc)
log("Info  [ Game initialised succesfully")

# Engine.Saves.loadGame()

Engine.Text.printTi(Engine.Text.local("dialogues.xml", "d1/text"), 0.05)
Engine.Text.printTi(Engine.Text.local("dialogues.xml", "d1/desc"), 0.05)
log("Info  [ Programm ended succesfully")