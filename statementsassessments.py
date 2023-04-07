st = 'Print only the words that start with s in this sentence'
stringlist = st.split(' ')
print(stringlist)
for word in stringlist:
    if (word[0].lower() == 's'):
        print(word)
print('----------------')
evennumbers = list(range(0,11,2))
print(evennumbers)
print('----------------')
print([x for x in range(1,51) if x%3==0])
print('----------------')
st = 'Print every word in this sentence that has an even number of letters'
stringlist = st.split(' ')
print(stringlist)
for word in stringlist:
    if (len(word)%2 == 0):
        print(word)
print('----------------')
for number in range(1,101):
    if(number%3 == 0 and number%5 == 0):
        print('FizzBuzz')
    elif(number%3 == 0):
        print('Fizz')
    elif(number%5 == 0):
        print('Buzz')
    else:
        print(number)
print('----------------')
st = 'Create a list of the first letters of every word in this string'
print([word[0] for word in st.split(' ')])