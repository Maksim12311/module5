import random

class Varrior:

	def __init__(self, name):
		self.name = name
		self.health = 100
		self.tired = 100
		self.armoar = 100

class Player1(Varrior):

	def attack(self, opponent):
		opponent.health -=random.randint(10,30) 
		self.health -= random.randint(10,30)
		self.tired -= 10
		if self.health <=0:
			print("Player1 is die")

	def defend(self):
		if self.armoar > 0:
			self.armoar -=random.randint(0,10)
			self.health -=random.randint(0,20)
		else:
			self.health -=random.randint(10,30)
		if self.health <=0:
			print("Player1 is die")
		
	def relax(self):
		if self.tired < 90:
			self.tired +=10
		else:
			self.tired = 100


class Player2(Varrior):

	def attack(self, opponent):
		opponent.health -=random.randint(10,30)
		self.health -= random.randint(10,30) 
		self.tired -=10
		if self.health <=0:
			print("Player2 is die")

	def defend(self):
		if self.armoar > 0:
			self.armoar -=random.randint(0,10)
			self.health -=random.randint(0,20)
		else:
			self.health -=random.randint(10,30)
		if self.health <=0:
			print("Player2 is die")

	def relax(self):
		if self.tired < 90:
			self.tired +=10
		else:
			self.tired = 100

p1 = Player1('Player1')
p2 = Player2('Player2')

for i in range(3):
	p1.attack(p2)
	p2.attack(p1)

print(p1.health, p2.health)