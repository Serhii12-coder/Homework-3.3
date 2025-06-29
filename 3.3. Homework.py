my_list = [1,2,3,4,5,6,7,8,9]
length = len(my_list)
a1 = int(length/2)
if length % 2 == 0:
    list1 = my_list[:a1]
    list2 = my_list[a1:]
else:
    a2 = a1 + 1
list1 = my_list[:a2]
list2 = my_list[a2:length]
print(list1)
print(list2)
#1