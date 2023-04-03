# person: module(file) name, Person:class name
from viewing_party.person import Person

my_person = Person("Auberon", 28) # need to match parameter in __init__ function in Person class
baby = Person("Jazz")# if there is defaul assigned in __init__, there is no need to pass a age in here
nancy = Person("Nancy")

print(my_person.name)
print(my_person.age)
print(my_person.friends)
# print(baby.name)
# print(baby.age)
my_person.add_friend(baby)
print(my_person.friends[0].name)
print(nancy.friends)# will print out an empty list as well