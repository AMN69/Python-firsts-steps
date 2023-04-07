def square(num):
    return num**2

my_nums = [1,2,3,4,5]

for item in map(square, my_nums): # print squares
    print(item)

print(list(map(square, my_nums))) # creates a list of squares

def check_even(num):
    return num%2 == 0

mynums = [1,2,3,4,5,6]

for n in filter(check_even,mynums):
    print(n)

# Lamba expression (are anonymous functions)
square = lambda num: num ** 2
print(square(10))

print(list(map(lambda num:num**2,mynums)))

print(list(filter(lambda num:num%2 == 0,mynums)))
