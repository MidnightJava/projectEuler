'''
Created on Dec 16, 2015

@author: Mark
'''
from _collections import defaultdict
import timeit
import math

def primeFactors(n):
        primes = defaultdict(int)
        for i in xrange(2, n):
            if n % i == 0:
                tempdict = defaultdict(int)
                for num, count in primeFactors(i).items():
                    tempdict[num] += count
                for num, count in tempdict.items():
                    if count > primes[num]:
                        primes[num] = count
                tempdict.clear()
        if len(primes.keys()) == 0:
            primes[n] += 1
        prod = 1
        for num, count in primes.items():
            prod *= (num**count)
        if n/prod != 1:
            primes[n/prod] += 1 
        return primes
    
# start = timeit.default_timer()
# nPrimes = 0
# f = 2
# while nPrimes < 10001:
#     primes = primeFactors(f)
#     if len(primes) == 1 and primes[f] == 1:
#         nPrimes += 1
#         if nPrimes % 100 == 0:
#             print nPrimes, "th prime is", f
#     f += 1
# print "10001st prime:", f-1
# stop = timeit.default_timer()
# print "Time:", stop - start

def primesInRange(m, n, primes):
    print "get primes in range",m,n-1
    a = dict([(i,1) for i in xrange(m, n) if i % 2 != 0 or i == 2])
    if primes:
        primesCopy = primes[::-1] #reverse list so pop will iterate from smallest to greatest
        p = primesCopy.pop()
        if p == 2: # skip 2, since remaining even numbers are not in the sieve
            p = primesCopy.pop()
        j =  m
        while j % p != 0:
            j += 2
    else:
        primesCopy = None
        p = m
    while p**2 <= n:
        j = p**2
        while j <= n:        
            a[j] = 0
            j += p
        if primesCopy:
            p = primesCopy.pop()
        else:
            p = 3 if p == 2 else p + 2
    return [n for n in a.keys() if a[n] == 1]

def nthPrime(n):
    count = 0
    start = 2
    sieve = 100000
#     sieve = 2 * n * int(math.log(n))
    primes = []
    while count < n:
        primes.extend(primesInRange(start, start + sieve, primes))
        count = len(primes)
        start += sieve
#         print count, "primes found so far"
    if count == n:
        return primes[-1]
    else:
        return primes[-(count - n + 1)]

start = timeit.default_timer()
print nthPrime(10001)
stop = timeit.default_timer()
print "Time:", stop - start

             
    

    
    