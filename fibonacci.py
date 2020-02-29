fibonacci.py

# Fibonacci numbers module

#n = int(input('Plese enter a number: '))

def fib(n): #write fibonacci series up to n
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	print()

 


#Go to fibonacci Powerpoint

def fib2(n):	# return Fibonacci series up to n
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a=b
	return result

# a lout kyat pr(important)

# >>> fib #import