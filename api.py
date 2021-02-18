class MainCharacter:
	name = "name"
	age = 0

	intelligence = 0
	intelligence_per_year = 1
	readed_book = False

	health = 100
	health_per_year = 0
	walk_counter = 0



	def read_a_book(self):
		if self.readed_book == False:
			self.intelligence +=5
			self.intelligence_per_year +=1
			self.readed_book = True
		else:
			print("you already read a book this year")

	def go_walk(self):

		if self.walk_counter <=2:
			self.health +=5
			self.health_per_year +=1
			self.walk_counter +=1

		elif self.walk_counter <=5:
			self.health +=5
			self.walk_counter +=1
		else:
			print ("you already go 5 times for a walk")			


	def birthday(self):
		
		self.age +=1
		self.intelligence += self.intelligence_per_year
		self.readed_book = False
		self.health += self.health_per_year
		self.walk_counter = 0

		print ("{0} has {1} years old".format(self.name, self.age))


		if self.age >= 12:
			self.intelligence_per_year -= 1
			self.health_per_year -= 1

	if self.health >= 100:
		self.health = 100
