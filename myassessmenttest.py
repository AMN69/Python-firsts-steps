theEquation = 100.25 * 10
print(theEquation)
theEquation = theEquation / 10
print(theEquation)
theEquation = theEquation ** 2
print(theEquation)
theEquation = theEquation + 0.9375
print(theEquation)
theEquation = theEquation - theEquation
print(theEquation)
print(4 * (6 + 5))
print(4 * 6 + 5)
print(4 + 6 * 5)
checkType = 3 + 1.5 + 4
print (type(checkType))
import math
print(math.sqrt(9))
print(9 ** 2)
x = 'hello'
print (x[1:2])
print(x[::-1])
print(x[4:5])
print(x[4:3:-1])
list = [0,0,0]
print(list)
list2 = []
list2.append(0)
list2.append(0)
list2.append(0)
print(list2)
list3 = [1,2,[3,4,'hello']]
list3[2].pop()
print(list3)
list3[2].append('goodbye')
print(list3)
list4 = [5,3,4,6,1]
list4.sort()
print(list4)
d = {'simple_key':'hello'}
print(d['simple_key'])
d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])
d4 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d4['k1'][2]['k2'][1]['tough'][2][0])
theTuple = ('1', '2')
print(theTuple)
list5 = [1,2,2,33,4,4,11,22,3,3,2]
mySet = {1,2,2,33,4,4,11,22,3,3,2}
print(mySet)
print(3.0 == 3)
print(4**0.5 !=2)
# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
print(l_one[2][0] >= l_two[2]['k1'])