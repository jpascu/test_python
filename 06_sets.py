### Sets ###

my_set = set()
my_other_set = {}

print (type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Jose", "Ortiz", 42}
print(type(my_other_set))

print(len(my_other_set))
print(my_other_set.add("jportiz"))
print(my_other_set.add("jportiz")) # No admite repetidos
print(my_other_set)   #  Un set no es una estructura ordenada

print("Ortiz" in my_other_set)
print("Pascual" in my_other_set)

my_other_set.remove("Ortiz")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
#print(my_other_set)  NameError: name 'my_other_set' is not defined

my_set = {"Jose", "Ortiz", 42}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Java", "Kotlin", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union(my_new_set).union({"Javascript", "C#"}))

print(my_new_set.difference(my_set))