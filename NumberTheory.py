import math

# Optimize this to increment by 6 instead of 2
# Make more pythonic
def eratosthenes(n):
	if n < 2:
		return []
	numList = range(0, n+1)
	i = 1
	while i**2 < n:
		i += 1
		if numList[i] == 0:
			continue
		if i > 2:
			step = 2 * i
		else:
			step = i
		for j in range(i**2, n+1, step):
			numList[j] = 0
	numList[1] = 0
	return [i for i in numList if i != 0]

def gcd(a, b):
	return a if b == 0 else gcd(b, a%b)

def coprime(a, b):
	return gcd(a, b) == 1

def rel_prime(a, b):
	return coprime(a, b)

def fib(n):
	p = (1+math.sqrt(5))/2
	q = (1-math.sqrt(5))/2
	return int((p**n - q**n)/math.sqrt(5))

def comb(n, r):
	return float(math.factorial(n)/(math.factorial(n-r)*math.factorial(r)))

def factors(n):
	return [i for i in range(1,n+1) if n%i == 0]

def prime_factors(n):
	return list(set(factors(n)) & set(eratosthenes(n)))

def prime_factorization(n):
	i = 0
	count = 0
	result = []
	pf = prime_factors(n)
	for factor in pf:
		while n%pf[i] == 0:
			n /= pf[i]
			count += 1
		result.append((factor, count))
		count = 0
		i += 1
	return result

def totient(n):
	pf = prime_factors(n)
	x = 1
	for factor in pf:
		x *= (1.0 - 1.0/factor)
	return int(n*x)

def isPrime(n):
	if (n%2 == 0 and n != 2) or n <= 2:
		return False
	i = 3
	while i**2 < n:
		if n%i == 0:
			return False
		i += 2
	return True
