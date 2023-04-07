import math
def vol(rad):
    return (((rad * rad * rad) * 4) / 3) * math.pi
print('Sphere volume is: ', vol(2))

def ran_bool(num,low,high):
    if num >= low and num <= high:
        return True
    else:
        return False
print('Is the number 5 between 3 and 10?: ',ran_bool(5,3,10))

import string
def up_low(s):
    alphabet = string.ascii_letters
    low = 0
    up = 0
    for letter in s:
        if letter not in (alphabet):
            continue
        if letter.isupper():
            up = up + 1
        else:
            low = low + 1
    return (low,up)
print('The number of letters low and up are: ', up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))

sample_list = [1,1,1,1,2,2,3,3,3,3,4,5]
def unique_list(list):
    unique_list = set(list)
    return unique_list
print('The unique list is: ', unique_list(sample_list))

sample_list_to_multiply = [1,2,3,-4]
def multiply(list):
    total = 1
    for number in list:
        total = total * number
    return total
print('The total of the list is: ', multiply(sample_list_to_multiply))

def palindrome(s):
    s = s.replace(' ','')
    reversed_string = s[::-1]
    return s == reversed_string

print('Is this word a palindrome?: ', palindrome('pep ep'))

def ispangram(strl, alphabet=string.ascii_lowercase):
    strl_without_spaces = strl.replace(" ", "")
    unique_letters = set(strl_without_spaces)
    if len(unique_letters) >= len(alphabet):
        return True
    else:
        return False

print('Is it a pangram?: ', ispangram('The quick brown fox jumps over the lazy dog'))
