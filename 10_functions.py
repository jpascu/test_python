def my_function ():
    print("Esto es una función")


my_function()
my_function()
my_function()

def sum_two_values (first_number, second_number): 
    print (first_number + second_number)

sum_two_values(8,9)
sum_two_values("5","7")
sum_two_values(1.4,2)

def sum_two_values_with_return (first_number, second_number): 
    return first_number + second_number

my_result = sum_two_values_with_return(10,5)
print(my_result)

my_nombre = "Luis"

def print_name(name, surname):
    print(f"{name} {surname}")
    my_nombre = name

print_name(my_nombre,"Ortiz")
print_name(surname="Ortiz", name="Jose")
print(my_nombre)


def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Jose", "Ortiz", "jportiz")
print_name_with_default("Jose", "Ortiz")

def print_texts(*texts):
    for text in texts:
        print(text)

print_texts("Hola", "Jose", "Java")