my_list1 = [1,2,3]
my_list2 = ['string',100,23.2]
print(len(my_list1))
print(my_list2[0])
print(my_list1[1:])
print(my_list1 + my_list2)
new_list = my_list1 + my_list2
print(new_list)
new_list[0] = 'zero'
print(new_list)
new_list.append('six')
print(new_list)
new_list.pop()
print(new_list)
popped_item = new_list.pop()
print(new_list)
print(popped_item)
new_list.pop(0)
print(new_list)
new_list = ['a', 'x', 'y', 'b', 'c', 'd']
new_list.sort()
print(new_list)
new_list.reverse()
print(new_list)
