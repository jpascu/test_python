### Conditionals ###


my_condition = False

if my_condition:
    print("Se ejecuta condicion if")

my_condition = 5 ** 2

if my_condition == 10:
    print("Se ejecuta condicion del segundo if")
elif my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25: 
     print("Es igual a 25")
else:
    print("Es menor o igual a 10 o mayor o igual que 20")

    #print("Es menor o igual a 10 o mayor o igual que 20") # Esta dentro del else


my_string = ""

if not my_string:
    print("Mi cadena de texto es vacia")

if my_string == "Mi cadena de textoooo":
    print("Coinciden")

print("La ejecucion continua")


