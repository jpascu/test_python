### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))


my_other_dict = {"Nombre" : "Jose", "Apellidos" : "Ortiz", "Edad": 35, 1 : "Python"}

my_dict = {
    "Nombre" : "Jose", 
    "Apellidos" : "Ortiz", 
    "Edad": 35, 
    "Lenguajes" : {"Python", "Swift", "Kotlin"},
    1:1.78
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Gael"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Empresa"] = "Accenture"
print(my_dict["Empresa"])

del my_dict["Empresa"]
print(my_dict)

print("Jose" in my_dict)
print("Nombre" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)

my_new_dict = dict.fromkeys(("Nombre", 1 , "Piso"))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, ["Jose","Ortiz"])
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, "Jose")
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))