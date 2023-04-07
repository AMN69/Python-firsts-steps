t = (1,2,3)
mylist = [1,2,3]
t = ('one', 2, 'one')
print(t[0])
print(t[-1])
print(t.count('one'))
print(t.index('one'))
t2 = (1,2,[1,2])
print(t2[2])
t2[2][0] = 'New'
print(t2)
t2[2] = 'pepe'