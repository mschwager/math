import math

def comb(n, r):
	return float(math.factorial(n)/(math.factorial(n-r)*math.factorial(r)))

def catalan(n):
	return (1.0 / (n+1)) * comb(2*n, n)

def stirling1(n, k):
	if n == 0 and k == 0:
		return 1
	if k == 0 and n >= 1:
		return 0
	if k > n:
		return 0
	return stirling1(n-1, k-1) - (n - 1) * stirling1(n-1, k)

def stirling2(n, k):
	if k <= 1 or k == n: 
		return 1
	if k > n or n <= 0: 
		return 0
	return stirling2(n-1, k-1) + k * stirling2(n-1, k)

def derangements(n):
	if n == 1:
		return 0
	d = -1
	dn = 0
	for i in range(2, n+1):
		dnm1 = dn
		d = -d
		dn = i * dnm1 + d
	return dn
