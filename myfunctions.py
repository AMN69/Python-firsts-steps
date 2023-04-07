def says_name(name='Default'):
    '''
    says hello + name
    '''
    print(f'Hello {name}')

says_name("Andreu")
says_name()

def add_function(num1,num2):
    return num1+num2

result = add_function(1,2)
print(result)
print(add_function('10','20')) # concatenates

# functions with logic
def even_check(number):
    return number % 2 == 0
print(even_check(20))
print(even_check(21))

def check_even_list(num_list):
    # return all even numbers in a list
    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers
print(check_even_list([2,4,5]))
print(check_even_list([1,3,5]))

# tupples unpacking

stock_prices = [('APPL', 200),('GOOG',400),('MSFT',100)]

work_hours = [('Abby',100),('Billy',4000),('Cassie',800)]
def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''
    
    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass 
    
    # return
    return (employee_of_month,current_max)
print(employee_check(work_hours))

# Interactions between python functions
example = [1,2,3,4,5,6,7]
from random import shuffle
#shuffle(example)

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
#result = shuffle_list(example)
#print(result)
#mylist = [' ', 'O', ' ']
#shuffle_list(mylist)
def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0, 1 o 2: ")
    return int(guess)

#print(player_guess())

def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("Correct!")
    else:
        print("Wrong guess!")
        print(mylist)

mylist = [' ','O',' ']
mixedup_list = shuffle_list(mylist)
guess = player_guess()
check_guess(mixedup_list,guess)
# *args and *kwargs
def myfunc(a,b):
    return (a+b) * 0.05
print(myfunc(40,60))

# If we had an unlimited number of args we can do this (*args is a tuple)
# by convention we use args but could be whatever other word if it starts by *
def myfunc(*args):
    return sum(args) * 0.05
print(myfunc(100,100,100,100,100,100,100))
# by convention kwargs and is a dictionary
def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')
myfunc(fruit='apple',veggie='lettuce')

def myfunc(*args,**kwargs):
    print('I would like {} {}'.format(args[0],kwargs['food']))
myfunc(10,20,30,fruit='banana',food='paella')

def myfunc(theString):
    isUpper = True
    indexCount = 0
    theNewString = ''
    for letter in theString:
        if isUpper:
            isUpper = False
            theNewString = theNewString + theString[indexCount].upper()
        else:
            isUpper = True
            theNewString = theNewString + theString[indexCount]
        indexCount = indexCount + 1
    return theNewString
print(myfunc('pepito'))
print('a'.upper())
