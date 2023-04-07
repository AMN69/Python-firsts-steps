lambda num:num**2 # num is a local variable
name = 'THIS IS A GLOBAL STRING'

def greet():
    name = 'Sammy'

    def hello():
        print('Hello '+name) # we print Hello Sammy because the local variable goes first
    hello()
greet()

name2 = 'THIS IS A GLOBAL STRING'

def greet():
    #name2 = 'Sammy'

    def hello():
        print('Hello '+name) # we print Hello THIS... because the function uses the global variable
    hello()
greet()

# GLOBAL name3
name3 = 'THIS IS A GLOBAL STRING'

def greet():
    # ENCLOSING name 3
    name3 = 'Sammy'

    def hello():
        # LOCAL name3
        name3 = "I'M A LOCAL"
        print('Hello '+name3) # we print Hello THIS... because the function uses the global variable
    hello()
greet()

x = 50 
def func(x):
    print(f'X is {x}') # Here x is 50 because takes the global value
    # LOCAL REASSIGNMENT
    x = 200
    print(f'I JUST LOCALLY CHANGED X TO {x}') # Here x is 200 because I change x locally
func(x)
print(f'The change does not affect outside the function {x}')

x = 50 
def func():
    global x # takes x from the global space
    print(f'X is {x}') # Here x is 50 because takes the global value
    
    # LOCAL REASSIGNMENT ON A GLOBAL VARIABLE!
    x = 2000
    print(f'I JUST LOCALLY CHANGED A GLOBAL X TO {x}') # Here x is 2000 because I change GLOBAL x locally
func()
print(f'The change affects outside the function because I used global x {x}')

# instead of using global we can do the same returning x

x = 50 
def func(x):
    print(f'X is {x}') # Here x is 50 because takes the global value
    
    # LOCAL REASSIGNMENT ON A GLOBAL VARIABLE!
    x = 20000
    print(f'I JUST LOCALLY CHANGED A GLOBAL X TO {x}') # Here x is 20000 because I change x locally
    return x
x = func(x)
print(f'The change affects outside the function because I returned the locally changed x and assigned it globally {x}')


