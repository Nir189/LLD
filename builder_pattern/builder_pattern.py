'''
1. Builder and Entity class - Creational design pattern
2. Building complex object by step by step rather in one go
3. At any time, object can be returned by calling build() <even at first step>
4. Existing objects could be givent to builder initialization.
5. Readability of code increases.
'''

class Person:

	def __init__(self):
		self.name = None
		self.age = None
		self.place = None

	def __str__(self):
		return f'A person with name {self.name if self.name else "NA"}' \
				 f'with age{self.age if self.age else "NA"}' \
				 f'lives at {self.place if self.place else "NA"}'
		
class PersonBuilder:

	def __init__(self, person=Person()):
		self.person = person

	def setName(self,name):
		self.person.name = name
		return self

	def setAge(self,age):
		self.person.age = age
		return self  

	def setPlace(self,place):
		self.person.place = place
		return self

	def build(self):
		return self.person 	  

###############################################	   
if __name__ == "__main__":   
  
   pb = PersonBuilder()
   person = pb.build()
   print(person)
###############################################
person = pb.setAge(20).setName("Nirabh").build()
print(person)
###############################################
pb2 = PersonBuilder(person)
person = pb.setPlace("India").build()
print(person)
###############################################
