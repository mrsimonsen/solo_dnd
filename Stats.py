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
		try:
			new = int(new)
			if new in range(1,31):
				self.__value = new
			else:
				print("Expected range: 1 - 30")
		except ValueError:
			print("Expected a whole number")


class HP():
	'''Represents a generic Dnd entity hit points'''
	def __init__(self,max=1):
		self.__max = max
		self.__hp = max
		self.__temp = 0

	def __str__(self):
		return f"{self.hp+self.temp}/{self.max}\nTemp HP: {self.temp} (included above)"
	
	def __check_hp(self):
		if self.hp + self.temp <= -self.max:
			print("Instant Death!")
		elif self.hp + self.temp < 1:
			print("HP below 1, Unconscious!")

	@property
	def max(self):
		return self.__max
	def max(self, new):
		try:
			new = int(new)
			if self.hp <= new:
				self.__max = new
			else:
				print("Current hit points dropped to new maximum HP.")
				self.__max = new
				self.__hp = new
		except ValueError:
			print("Expected a whole number")
	
	@property
	def hp(self):
		return self.__hp
	@hp.setter
	def hp(self, new):
		try:
			new = int(new)
			if new <= self.max:
				self.__hp = new
			else:
				print("Can't have more hit points than your max, overflow hp discarded.")
				self.__hp = self.max
			__check_hp()
		except ValueError:
			print("Expected a whole number")

	@property
	def temp(self):
		return self.__temp
	@temp.setter
	def temp(self, new):
		try:
			new = int(new)
			self.__temp = new
		except ValueError:
			print("Expected a whole number")


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
		try:
			new = int(new)
			self.__AC = new
		except ValueError:
			print("Expected a whole number")

	@property
	def speed(self):
		return self.__speed
	@speed.setter
	def speed(self, new):
		try:
			new = int(new)
			self.__speed = new
		except ValueError:
			print("Expected a whole number")

class Item():
	'''Generic DnD item'''
	def __init__(self,name='', weight = 0, quan = 1):
		self.name = name
		self.__weight = weight
		self.__quantity = quan

	def __str__(self):
		return f"{self.quantity}x {self.name} ({self.weight * self.quantity} lbs)"

	@property
	def weight(self):
		return self.__weight
	@weight.setter
	def weight(self, new):
		try:
			new = float(new)
			self.__name = new
		except ValueError:
			print("Expected a number")
	
	@property
	def quantity(self):
		return self.__quantity
	@quantity.setter
	def quantity(self, new):
		try:
			new = int(new)
			self.__quantity = new
		except ValueError:
			print("Expected a whole number")

class Inventory():
	'''PC/NPC inventory'''
	def __init__(self):
		self.inventory = []

	def __str__(self):
		rep  = '--Inventory--\n'
		rep += f'Unique Items: {len(self.inventory)}\n'
		rep += f'Total Weight: {self.weight} lbs\n'
		for i in self.inventory:
			rep += f"{i}\n"
		return rep

	@property
	def weight(self):
		total = 0
		for i in self.inventory:
			total += i.quantity * i.weight
		return total

	def add_item(name=None, weight=None, quantity=None):
		if not name:
			name = input("Enter the Item's name:\n")
		for i in self.inventory:
			if name == i.name:
				print("Item already exists in inventory")
				print("Update Item quantity instead")
				return
		if not weight:
			weight = input("Enter the Item's weight:\n")
		if not quantity:
			quantity = input("Enter the quantity of Item:\n")
		self.inventory.append(Item(name,weight,quantity))

	def update_quantity(name=None,new=None):
		if not name:
			name = input("Enter the Item's name:\n")
		for i in self.inventory:
			if i.name == name:
				if not new:
					new = input(f"What is the new quantity of {i.name}s:\n")
				i.quantity = new
				if i.quantity < 1:
					print(f"Removing {i.name} from your inventory")
					self.inventory.remove(i)
				break
		print(f"{name} not found in inventory, add item instead")
	
	def use(self,name):
		for i in self.inventory:
			if i.name == name:
				i.quantity -= 1
				if i.quantity < 1:
					print(f"Removing {i.name} from your inventory")
					self.inventory.remove(i)
				break
		print(f"{name} not found in inventory")