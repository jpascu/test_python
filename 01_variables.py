my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))


my_bool_variable = False
print(my_bool_variable)


#Concatenacion de variables en un print
print(my_string_variable,my_int_to_str_variable,my_bool_variable)

#Algunas funciones

print(len(my_string_variable))

#Variables en una sola linea

name, surname, alias, age = "Jose", "Ortiz", "jose.ortiz", '42'
print ("Me llano", name, surname, ". Mi edad es:", age, "y mi alias es:", alias)


#Inputs 

'''
name = input('¿Cual es tu nombre?')
age = input ('¿Cuantos años tienes?')

print (name)
print(age)

'''

#Cambiamos su tipo
name = 35
age = "Hola"

print(name , age)

#Forzamos el tipo
address: str = "Madrid"
address: int = 32
print(address)
print(type(address))

skills = ['HTML', 'Java']
print(skills)