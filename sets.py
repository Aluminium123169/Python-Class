#sets

includes a data type for sets.
Curly braces or the set[] function can be used to create sets

basket = {'apple', 'orange', 'apple' 'pear', 'orange', 'banana'}
print(basket)                #show that duplicates have been removed

'orange' in basket            #fast membership testing
'crabgrass' in basket

Demonstrate set operation on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a 									#unique letters in a
a - b								#letters in a but not ijn b
a | b 								#lettrs in a or b or both
a & b 								#letters in both a and b
a ^ b 								#letters in a or b but not both

a = {x for x in 'abracadabra' if x not in 'abc'}
a

-----------

x = set('23802348')
y = set('57839012')
x - y
y - x
x ^ y
y | x
x & y
x

>>>Dictionaries

#Dictionaries

#Another useful data type built into Python is the dictionary

tel = {'jack': 4098, 'scaape': 4139}
tel['scape']
tel['guido'] = 4127
tel

------

del tel['sape']
tel['irv'] = 4137
tel

list(tel) # Change to list

sorted(stuent) #Alphabet Sorting

'MgOo' in student

'MaMa' not in student

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dict(sape=4139, guido=4127, jack=4098)

 for x in 2, 4, 6:
 		print(x,x**2)
2 : 4
4 : 16
6 : 36


 {x: x**3 for X in (1, 2, 3, 4, 5)}

1 : 1
2 : 8
3 : 27
4 : 64
5 : 125

--------------

when looping through Dictionaries
knights = {'gallahad': 'the pure', 'the robin': 'the brave'}
for k, v in knights.items():
		print(k, v)

for x, y in enumerate(['tic', 'tac','toe']):
	print(x, y)