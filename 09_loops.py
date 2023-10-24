### Loops ####


# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition+= 2
else:
    print("Mi condición es mayor  que 10")

print("======================")
while my_condition < 20:
    my_condition+=1
    if my_condition == 15:
        print("Se detiene ejecución")
        break
    print("Mi condición es menor que 20: ", my_condition )



# For

my_list = [1, 1, 2, 3, 5, 8, 4]

for element in my_list:
    print(element)

my_set = {"Jose", "Ortiz", 42}

for element in my_set:
    print(element)

my_dict = {
    "Nombre" : "Jose", 
    "Apellidos" : "Ortiz", 
    "Edad": 35, 
    "Lenguajes" : {"Python", "Swift", "Kotlin"},
    1:1.78
    }
for element in my_dict:
    print(element)
    if  element == "Edad":
        break
    print("Se ejecuta")
else:
    print("Bucle finalizado")
print("La ejecución continua")