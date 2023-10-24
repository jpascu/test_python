### Lists

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [1, 1, 2, 3, 5, 8, 4]

print(my_list)
print(len(my_list))

my_other_list = [42, 1.78, "Jose", "Ortiz"]
print(my_other_list)
print(type(my_other_list))
print(my_other_list[1])
print(my_other_list[-1])
# print(my_other_list[5])

print(my_list.count(1))
print(my_other_list.count("Jose"))

name, height, age , surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

print (my_list + my_other_list)

my_other_list.append("Accenture")
print(my_other_list)
my_other_list.insert(1, "Valencia")
print(my_other_list)
my_other_list.remove("Valencia")
print(my_other_list)

my_new_list = my_list.copy()
print(my_new_list)

my_new_list.sort()
print(my_new_list)


'''
my_list.remove(1)
print(my_list)

print(my_list.pop())
print(my_list)

my_list.pop(2)
print(my_list)

del my_list[2]
print(my_list)

my_list.clear()
print(my_list)
'''
