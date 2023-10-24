## Strings

my_string = "Hola"
my_other_string = "Adios"

print(len(my_string))
print(len(my_other_string))

my_new_line_string = "Hola con \n salto de línea y \t tabulacion "
print(my_new_line_string)


my_scape_string = "Hola con \\n escapado "
print(my_scape_string)

name, surname, age = "Jose", "Ortiz", 18

print("Nombre es {} {} y mi edad es {}".format(name,surname,age))
print("Nombre es %s %s y mi edad es %d" %(name,surname,age))
print(f"Nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres

language = "python"
a,b,c,d,e,f = language
print(a,c,e)

#División

language_slice = language[1:3]
print(language_slice)


language_slice = language[1]
print(language_slice)

language_slice = language[-2]
print(language_slice)


language_slice = language[1:2:4]
print(language_slice)

#Reverse
reversed_language = language[::-1]
print(reversed_language)

#Funciones 

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.capitalize())
print(language.isnumeric())
print("2".isnumeric())
print(language.upper().isupper())