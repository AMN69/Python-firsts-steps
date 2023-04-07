hungry = True
if hungry:
    print('FEED ME!')
else:
    print('NOT HUNGRY')
loc = 'Bank'
if loc == 'Auto Shop':
    print("Cars all cool!")
elif loc == 'Bank':
    print("Money is cool!")
elif loc == 'Store':
    print("Welcome to the store!")
else:
    print("I do not know much")

name = 'Sammy'

if name == 'Sammy':
    print('Hello Sammy!')
elif name == 'Frankie!':
    print("Hello Frankie!")
else:
    print("What is your name?")

#For loops
my_iterable = [1,2,3,4,5,6,7,8,9,10]
for item_name in my_iterable:
    if item_name % 2 == 0:
        print(item_name)
    else:
        print(f'Odd Number: {item_name}')
list_sum = 0
for num in my_iterable:
    list_sum = list_sum + num

print(list_sum)

my_string = 'Hello World'
for letter in my_string:
    print(letter)

for letter in 'Hello World2':
    print(letter)

for _ in 'Hello': # We don't want to use the variable
    print("cool!")

my_otherlist = [(1,2),(3,5),(5,6),(7,8)]
print(len(my_otherlist))
for item in my_otherlist:
    print(item)

for a,b in my_otherlist: #called tupple and packing
    print(a)
    print(b) # you can print b or not or a yes or not

d = {'k1':1,'k2':2,'k3':3}
for item in d:
    print(item)
for item in d.items():
    print(item)
for key,value in d.items(): #tupple and packing
    print(key)
    print(value)
for value in d.values():
    print(value)

#While loops
x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x = x + 1
else:
    print ("X IS HIGHER THAN 4")
x = [1,2,3]

for item in x:
    pass

mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        #continue
        break
    print(letter)

for num in range(10):
    print(num)
for num in range(0,10,2): # from 0 to 10 (not included) in steps of 2
    print(num)
listofnumbers = list(range(0,10,2))
print(listofnumbers)

index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count +=1

word = 'abcde'
for item in enumerate(word):
    print(item) # I get tupples
for index,letter in enumerate(word):
    print(index)
    print(letter)

mylist1 = [1,2,3]
mylist2 = ['a','b','c','d','e']
for item in zip(mylist1,mylist2): # zips and pair up the items
    print(item)
print('x' in ['x','y','z'])
print(1 in [2,3,4])
print('a' in 'a world')
print('mykey' in {'mykey': 1})
print(min(mylist1))
print(max(mylist1))
from random import randint # build-in method
print(randint(0,100))
#newnumber = input('Enter a number here: ')
""" print(newnumber)
print(type(newnumber))
print(int(newnumber)) """
# List comprehensions
print("List comprehensions")
mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)
mylist = [letter for letter in mystring]
print(mylist)
mylist2 = [x for x in 'word']
print(mylist2)
print([num**2 for num in range(0,11)])
print([x for x in range(0,11) if x%2==0])
celcius = [0,10,20,34.5]
fahrenheit = [( (9/5)*temp + 32) for temp in celcius]
print (fahrenheit)
mylist = []
for x in [2,4,6]:
    for y in [1,10,1000]:
        mylist.append(x*y)
print(mylist)
mylist2 = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(mylist2)