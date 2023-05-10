import json
import modules.modules as m
import modules.Text as textey
import os
import modules.Log as log

def updateSkillsTraitsStats(sk, tr, st):
	sk.update({
		"crit": round(sk["agi"]*0.02, 2),
		"meleeacu": round(sk["agi"]*0.15+sk["str"]*0.37)/10,
		"rangeacu": round(sk["agi"]*0.37+sk["str"]*0.1)/10,
		"spellacu": round(sk["int"]*0.52)/10
	})
	tr.update({
		"collector": round(sk["agi"]*0.3),
		"oratory": round(sk["int"]*0.5)+1,
		"meelemast": round(sk["meleeacu"]*15), 
		"rangemast": round(sk["rangeacu"]*15),
		"luck": round(sk["agi"]*0.015, 2)
	})
	st.update({
		"hp": sk["str"]*10,
		"mp": sk["int"]*20
	})

class Saves():

	def __init__(self, loc):
		self.loc = loc
		self.text = textey.Text(self.loc)
		log.log("Info  [ Succesfully initialised saves module.")

	@log.log_on_error
	def newGame(self, loc):

		skills = {
			"resist": 0,
			"dodge": 0,
			"str": 2,
			"int": 2,
			"agi": 2,
			"crit": 0,
			"meleeacu": 0,
			"rangeacu": 0,
			"spellacu": 0
		}
		traits = {
			"collector": round(skills["agi"]*0.3),
			"oratory": round(skills["int"]*0.5)+1,
			"meelemast": round(skills["meleeacu"]*15), 
			"rangemast": round(skills["rangeacu"]*15),
			"luck": round(skills["agi"]*0.04, 2)
		}
		stats = {
			"hp": skills["str"]*10,
			"mp": skills["int"]*20,
			"lvl": 1,
			"xp": 0,
			"xptoup": 500,
			"traitpoints": 0,
			"money": 20
		}


		self.text.printTi(self.text.local(self.loc+"dialogues.xml", "system/newgame/cname"), 0.01)
		cname = input()
		self.text.printTi(self.text.local(self.loc+"dialogues.xml", "system/newgame/race"), 0.01)
		crace=input()
		self.text.printTi(self.text.local(self.loc+"dialogues.xml", "system/newgame/gender"), 0.01)
		gender=input()
		self.text.printTi(self.text.local(self.loc+"dialogues.xml", "system/newgame/parents"), 0.01)
		parents=input()
		self.text.printTi(self.text.local(self.loc+"dialogues.xml", "system/newgame/tage"), 0.01)
		tage=input()
		self.text.printTi(self.text.local(self.loc+"dialogues.xml", "system/newgame/youtha"), 0.01)
		youtha=input()

		#^ - Гімно щоби зрозуміти що ставити в стати

		match crace:
			case "1": 
				charrace="ragul"
				skills.update({
					"str": skills["str"]+2,
					"agi": skills["agi"]+2,
					"int": skills["int"]-1
				})
			case "2":
				charrace="cossack"
				skills.update({
					"str": skills["str"]+3,
					"agi": skills["agi"]+1
				})
			case "3":
				charrace="orc"
				skills.update({
					"str": skills["str"]+3,
					"agi": skills["agi"]+2,
					"int": skills["int"]-1,
					"resist": skills["resist"]-2
				})
			case "4":
				charrace="anon"
				skills.update({
					"str": skills["str"]+1,
					"agi": skills["agi"]+1,
					"int": skills["int"]+1
				})
			case _:
				self.text.printTi("Нема такої раси, підорасе!", 0.01)
				self.newGame(loc)
		match gender:
			case "1":
				gender = "male"
				skills.update({
					"str": skills["str"]+2
				})
			case "2":
				gender = "female"
				skills.update({
					"agi": skills["agi"]+2
				})
			case _:
				self.text.printTi("Нема такої статті, підорасе!", 0.01)
				self.newGame(loc)
		match parents:
			case "1":
				skills.update({
					"int": skills["int"]+1
				})
				stats.update({
					"money": stats["money"]+30
				})
			case "2":
				skills.update({
					"str": skills["str"]+1,
					"agi": skills["agi"]+1
				})
			case "3":
				skills.update({
					"int": skills["int"]+2
				})
		match tage:
			case "1":
				skills.update({
					"agi": skills["agi"]+2
				})
			case "2":
				skills.update({
					"str": skills["str"]+1,
					"agi": skills["agi"]+1
				})
			case "3":
				skills.update({
					"int": skills["int"]+2			
				})
		match youtha:
			case "1":
				skills.update({
					"str": skills["str"]+2,
					"agi": skills["agi"]+1
				})
			case "2":
				skills.update({
					"str": skills["str"]+3
				})
			case "3":
				skills.update({
					"agi": skills["agi"]+2,
					"int": skills["int"]+1
				})
			case "4":
				skills.update({
					"str": skills["str"]+1,
					"agi": skills["agi"]+2
				})

		updateSkillsTraitsStats(skills, traits, stats)

		character = {
			"name": cname,
			"race": charrace,
			"gender": gender,
			"stats": stats,
			"skills": skills,
			"traits": traits
		}

		saveGame(character)

	@log.log_on_error
	def saveGame(self, char):

		filename=char["name"]+".json" 
		with open(f"saves/{filename}", "w") as f: #Створюємо файл з сейвом
			json.dump(char, f) 
		f.close()

	@log.log_on_error
	def loadGame(self):
		self.text.printTi(self.text.local("dialogues.xml", "system/load/choose"), 0.01)
		self.text.printTi(str(os.listdir("saves")).replace(".json", "").replace("[", "").replace("]", ""), 0.01) #Виводимо всі файли з сейвами
		toload = input()
		try:
			with open(f"saves/{toload}.json") as f:
				character = json.load(f)
				return character
			f.close()
		except:
			self.text.printTi("Нема такого сейву, рагуле!", 0.01)
			self.loadGame() #якщо юзер даун перезапускаємо функцію