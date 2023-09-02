for i in ['a','b','c']:
    try:
        print(i**2)
    except:
        print('The array element {} is NOT a number.'.format(i))

x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("The divisor can't be zero")
except:
    print("Other error")
finally:
    print("All done!")

def ask():
    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("You must provide an integer. Try again.")
            continue
        else:
            print("The square of {} is {}".format(result, result * result))
            break
ask()