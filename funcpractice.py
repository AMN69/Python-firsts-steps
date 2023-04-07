#WARMUP SECTION:

#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
#lesser_of_two_evens(2,4) --> 2
#lesser_of_two_evens(2,5) --> 5
def lesserOfTwoEvens(a,b):
     if a%2 == 0 and b%2 == 0:
#        if a < b:
#            return a
#        else:
#            return b
        return min(a,b)
     else:
 #       if a < b:
 #           return b
 #       else:
 #           return a
        return max(a,b)
print('The lesser of two evens is: ', lesserOfTwoEvens(2,4))
print('The lesser of two evens is: ', lesserOfTwoEvens(2,5))

#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('Crazy Kangaroo') --> False
def startWithSameLetter(twoWordString):
    twoWordSplitted = twoWordString.lower().split(' ') # or upper() would work the same
#    if twoWordSplitted[0][0] == twoWordSplitted[1][0]:
#        return True
#    else:
#        return False
    return twoWordSplitted[0][0] == twoWordSplitted[1][0]
print('Do two words start with the same letter?: ', startWithSameLetter('Levelheaded Llama'))
print('Do two words start with the same letter?: ', startWithSameLetter('Crazy Kangaroo'))

#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
#makes_twenty(20,10) --> True
#makes_twenty(12,8) --> True
#makes_twenty(2,3) --> False
def makes_twenty(first_number, second_number):
#    if first_number + second_number == 20 or first_number == 20 or second_number == 20:
#        return True
#    else:
#        return False
    return (first_number+second_number) == 20 or first_number == 20 or second_number == 20
print('is the sum 20 or one twenty?: ', makes_twenty(20,10))
print('is the sum 20 or one twenty?: ', makes_twenty(12,8))
print('is the sum 20 or one twenty?: ', makes_twenty(2,3))



#LEVEL 1 PROBLEMS:

#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
#old_macdonald('macdonald') --> MacDonald
def old_macdonald(name):
    new_name = ''
    counter = 0
    for word in name:
        if counter == 0 or counter == 3:
            new_name = new_name + word.upper()
        else:
            new_name = new_name + word
        counter = counter + 1
    return new_name
print('capitalize 1st and 4th letters: ', old_macdonald('macdonald'))
def old_macdonald2(name):
    first_half = name[:3]
    second_half = name[3:]
    return first_half.capitalize() + second_half.capitalize()
print('capitalize 1st and 4th letters: ', old_macdonald('macdonald'))

#MASTER YODA: Given a sentence, return a sentence with the words reversed
#master_yoda('I am home') --> 'home am I'
#master_yoda('We are ready') --> 'ready are We'
def master_yoda(sentence):
    splitted_sentence = sentence.split(' ')
#    new_sentence = ''
#    for word in splitted_sentence:
#        new_sentence = word + ' ' + new_sentence
#    return new_sentence
    reversed_word_list = splitted_sentence[::-1]
    return reversed_word_list
print('reversed words: ', master_yoda('I am home'))
print('reversed words: ', master_yoda('We are ready'))

#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
#almost_there(90) --> True
#almost_there(104) --> True
#almost_there(150) --> False
#almost_there(209) --> True
def almost_there(number):
#    if (number > 89 and number < 111) or (number > 189 and number < 211):
#        return True
#    else:
#        return False
    return (abs(100-number) <= 10) or (abs(200-number) <= 10)
print('Is within 10 of either 100 or 200?: ', almost_there(90))
print('Is within 10 of either 100 or 200?: ', almost_there(104))
print('Is within 10 of either 100 or 200?: ', almost_there(150))
print('Is within 10 of either 100 or 200?: ', almost_there(209))
      
#LEVEL 2 PROBLEMS:

#FIND 33:
#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#has_33([1, 3, 3]) → True
#has_33([1, 3, 1, 3]) → False
#has_33([3, 1, 3]) → False
def has_33(array):
    previous_number = 0
    for number in array:
        if number == 3 and previous_number == 3:
            return True
        previous_number = number
    return False
print('has the array 33?: ', has_33([1, 3, 3]))
print('has the array 33?: ', has_33([1, 3, 1, 3]))
print('has the array 33?: ', has_33([3, 1, 3]))

#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
#paper_doll('Hello') --> 'HHHeeellllllooo'
#paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
def paper_doll(string):
    splitted_string = list(string)
    new_string = ''
    for letter in splitted_string:
        new_string = new_string + letter + letter + letter 
    return new_string
print('3 chars per chart: ', paper_doll('Hello'))
print('3 chars per chart: ', paper_doll('Mississippi'))

#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
#blackjack(5,6,7) --> 18
#blackjack(9,9,9) --> 'BUST'
#blackjack(9,9,11) --> 19
def blackjack(first, second, third):
    if (first + second + third) <= 21:
        return first + second + third
    if (first + second + third) > 21 and (first == 11 or second == 11 or third == 11):
        return first + second + third - 10
    else:
        return 'BUST'
print('blackjack: ', blackjack(5,6,7))
print('blackjack: ', blackjack(9,9,9))
print('blackjack: ', blackjack(9,9,11))

#SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
#summer_69([1, 3, 5]) --> 9
#summer_69([4, 5, 6, 7, 8, 9]) --> 9
#summer_69([2, 1, 6, 9, 11]) --> 14
def summer_69(numbers_array):
    is_six = False
    total_sum = 0
    for number in numbers_array:
        if number == 6 and is_six == False:
            is_six = True
        elif number == 9:
            is_six = False
        elif is_six == False:
            total_sum = total_sum + number
    return total_sum
print('summer 69: ', summer_69([1, 3, 5]))
print('summer 69: ', summer_69([4, 5, 6, 7, 8, 9]))
print('summer 69: ', summer_69([2, 1, 6, 9, 11]))

#CHALLENGING PROBLEMS:

#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False
def spy_game(an_array):
    iszerzeroseven = ''
    for number in an_array:
        if number == 0:
            iszerzeroseven = iszerzeroseven + '0'
        elif number == 7:
            iszerzeroseven = iszerzeroseven + '7'
#    if iszerzeroseven == '007':
#        return True
#    else:
#        return False
    return iszerzeroseven == '007'
print('is 007?: ', spy_game([1,2,4,0,0,7,5]))
print('is 007?: ', spy_game([1,0,2,4,0,5,7]))
print('is 007?: ', spy_game([1,7,2,0,4,5,0]))

#COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
#count_primes(100) --> 25

def count_primes(the_number):
    total_primes = 0
    for number in range(2, the_number+1):
        for number2 in range(2, number+1):
            if number == number2:
                total_primes = total_primes + 1
            elif number % number2 == 0:
                break
    return total_primes
print('total primes: ', count_primes(100))

#Just for fun:
#PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
#print_big('a')

#out:   *  
#      * *
#     *****
#     *   *
#     *   *

the_a = ['  *  ', 
         ' * * ', 
         '*****',
         '*   *',
         '*   *']
the_b = ['**** ',
         '*   *',
         '**** ',
         '*   *',
         '**** ']
the_c = [' ****',
         '*    ',
         '*    ',
         '*    ',
         ' ****']
the_d = ['**** ',
         '*   *',
         '*   *',
         '*   *',
         '**** ']
the_e = ['*****',
         '*    ',
         '*****',
         '*    ',
         '*****']
def print_big(the_letter):
    if the_letter == 'a':
        for row in the_a:
            print(row)
    elif the_letter == 'b':
        for row in the_b:
            print(row)
    elif the_letter == 'c':
        for row in the_c:
            print(row)
    elif the_letter == 'd':
        for row in the_d:
            print(row)
    elif the_letter == 'e':
        for row in the_e:
            print(row)
print_big('a')