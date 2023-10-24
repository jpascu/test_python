#### Classess ####


class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        self.__name = name # Propiedad privada
        self.__surname= surname
        self.full_name = f"{name} {surname} {alias}" # Propiedad publica
    
    def get_name(self):
        return self.__name
    
    def walk(self):
        print(f"{self.full_name} está caminando" )

my_person = Person("Jose", "Ortiz")

print(f"{my_person.full_name}")
my_person.walk()

my_other_person = Person("Gael", "Ortiz", "Gamer")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Gael El Loco"

print(f"{my_other_person.full_name}")

#print(my_other_person.__name) # Error
print(my_other_person.get_name())