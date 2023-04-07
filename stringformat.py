print('This is an example{}'.format(' INSERTED'))
print('The {} {} {}'.format('fox', 'brown', 'quick'))
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))
result = 104.345
print("The result was {r:1.3f}".format(r=result)) #number of digits for integer and for decimal parts
name = "Jose"
print(f'Hello, his name is {name}')
age = 3
print (f'{name} is {age} years old.')