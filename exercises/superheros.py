# Write your solutions for 1.5 here!
class superhero:
	def __init__(self,name,superpower,strength):
		self.name = name
		self.superpower=superpower
		self.strength=strength
	def name_strength(self):
		print(self.name)
		print(self.strength)
	def save_civilian(self,work):
		self.strength = self.strength - work
		if work>self.strength:
			print("Superhero is not strong enough! :(")
			

asaf = superhero("asaf","super_strong", 10000)
asaf.name_strength()
asaf.save_civilian(15)
print(asaf.strength)
			