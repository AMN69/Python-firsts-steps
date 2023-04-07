# uniques values, added a repeated value doesn't make anything
myset = set()
myset.add(1)
print(myset)
myset.add(2)
print(myset)
mylist = [1,1,1,1,1,1,2,2,2,2,3,3,3,3,3]
print(set(mylist))
print(set([1,1,2,3]))