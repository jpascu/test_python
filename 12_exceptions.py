## Exception Handling ####


numberOne = 5
numberTwo = 1
numberTwo = "1"


try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una exception
    print("Error")


try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Error")
else:
    # Se ejecuta si no se produce exception
    print("La ejecución continua correctamente")
finally:
    print("Ejecución continua")


# Excepciones por tipo
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception  as error:
    print(error)