
class favAnimal:

	def __init__(self,arms,legs,eyes,tail,furry):
		self.armLength = float(arms)
		self.legLength = float(legs)
		self.eyes = int(eyes)
		self.tail = bool(tail)
		self.furry = bool(furry)

myCat = favAnimal( 15.0 , 22.0 , 2 , True , True )

print("Arm Length =", myCat.armLength)
print("Leg Length =", myCat.legLength)
print("# of Eyes =", myCat.eyes)
print("Does It Have A Tail?", myCat.tail)
print("Is It Furry?", myCat.furry)