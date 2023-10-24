### Tuples ####

my_tuple = tuple()
my_other_tuple = ()



my_tuple = (42, 1.78, "Jose", "Ortiz")
my_other_tuple = (15, 30, 45, 60)


print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])


print(my_tuple.count("Jose"))
print(my_tuple.index("Jose"))

#my_tuple[1] = 1.80 Error es inmutable
print(my_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[3] = "Accenture"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

del my_tuple
print(my_tuple)
