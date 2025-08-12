#creating empty lis
my_list = []
print(my_list)
#Appending values
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
#replace the second character with 15
my_list[1] = 15
print(my_list)
#delete the last elemet
del my_list[3]
print(my_list)
#sorting in ascending order
my_list.sort(reverse=False)
print(my_list)
#find the index of 30
value = 30
index = my_list.index(value)
print(f"The index of {value} is", index)