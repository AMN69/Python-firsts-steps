row1 = [' ', ' ', ' ']
row2 = [' ', 'X', ' ']
row3 = [' ', ' ', ' ']
def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

display(row1, row2, row3)

result = int(input("Please, enter a value: "))
print(result)
print(type(result))

def user_choice():
    choice = 'WRONG'
    acceptable_values = range(0,10)
    within_range = False
    while choice.isdigit() == False or within_range == False:
        choice = input("Please, enter a number (0-10): ")
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")
        else: 
            if int(choice) in acceptable_values:
                within_range = True
            else:
                print("The number must be between 0 and 10!")
    return int(choice)
print(user_choice())