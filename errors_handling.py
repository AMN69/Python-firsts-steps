def add(n1,n2):
    try:
        result = n1 + n2
    except:
        print("Hey it looks like you aren't adding correctly!")
    else:
        print("Add went well!")
        print(result)

add(10,20)
number1 = 10
number2 = input("Please provide a number: ")
add(number1,number2)
try:
    f = open('testfile', 'w')
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print("Hey you have an OS Error")
except:
    print('All other exceptions!')
finally:
    print("I always run") # this is always executed

def ask_for_int():
    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("Whoops! That is not a number")
            continue # meanwhile you don't provide a number are within the while loop
        else:
            print("Yes, thank you")
            break # once you provide a number you leave the while loop
        finally:
            print("End of try/except/finally")
            print("I will always run at the end!")
ask_for_int()
