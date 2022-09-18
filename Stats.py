from random import randint

class Attribute():
	'''Represents a generic DnD stat attribute'''
	def __init__(self,name='',value=0):
		self.name = name
		self.value = value

	def __str__(self):
		return f"{self.name}: {self.value}\nModifier: {self.modifier():+}"
	
	def modifier(self):
		'''calculate the modifier for a given value'''
		return int(self.value/2)-5

	@property
	def value(self):
		return self.__value
	@value.setter
	def value(self, new):
		if isinstance(new, int) and new in range(1,31):
			self.__value = new
		else:
			print(f"Expected a whole number between 1 and 30\n\tReceived {type(new)}<value '{new}'>")


class HP():
	'''Represents a generic Dnd entity hit points'''
	def __init__(self,max=1):
		self.__max = max
		self.__hp = max
		self.__temp = 0

	def __str__(self):
		return f"{self.hp+self.temp}/{self.max}\nTemp HP: {self.temp} (included above)"
	
	def __check_hp(self):
		if if self.hp + self.temp <= -self.max:
			print("Instant Death!")
		elif self.hp + self.temp < 1:
			print("HP below 1, Unconscious!")

	@property
	def max(self):
		return self.__max
	def max(self, new):
		if isinstance(new, int)
			if self.hp <= new:
				self.__max = new
			else:
				print("Current hit points dropped to new maximum HP.")
				self.__max = new
				self.__hp = new
		else:
			print(f"Expected a whole number\n\tReceived {type(new)}<value '{new}'>")
	
	@property
	def hp(self):
		return self.__hp
	@hp.setter
	def hp(self, new):
		if isinstance(new, int):
			if new <= self.max:
				self.__hp = new
			else:
				print("Can't have more hit points than your max, overflow hp discarded.")
				self.__hp = self.max
		else:
			print(f"Expected a whole number\n\tReceived {type(new)}<value '{new}'>")
		__check_hp()

	@property
	def temp(self):
		return self.__temp
	@temp.setter
	def temp(self, new):
		if isinstance(new, int):
			self.__temp = new
		else:
			print(f"Expected a whole number\n\tReceived {type(new)}<value '{new}'>")


class Stats():
	'''Represents the base stats of a DnD 5e entity'''
	def __init__(self):
		self.attributes = (
			Attribute('Strength',0),
			Attribute('Dexterity',0),
			Attribute('Constitution',0),
			Attribute('Intelligence',0),
			Attribute('Wisdom',0),
			Attribute('Charisma',0)
		)
		self.HP = HP(1)
		self.__AC = 0
		self.__speed = 0

	@property
	def initiative(self):
		'''return an initiative roll + mod'''
		roll = randint(1,21)
		return roll + self.attributes[2].modifier()

	@property
	def AC(self):
		return self.__AC
	@AC.setter
	def AC(self, new):
		if isinstance(new, int):
			self.__AC = new
		else:
			print(f"Expected a whole number\n\tReceived {type(new)}<value '{new}'>")

	@property
	def speed(self):
		return self.__speed
	@speed.setter
	def speed(self, new):
		if isinstance(new, int):
			self.__speed = new
		else:
			print(f"Expected a whole number\n\tReceived {type(new)}<value '{new}'>")


	