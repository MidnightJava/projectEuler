'''
Created on Dec 15, 2015

@author: Mark
'''
from collections import defaultdict
import timeit

#brute force: keep trying the next multiple of the highest number in the range,
#checking if it's divisible by all the other numbers in the range
def lcm1(n):
    def divisibleByRange(num, r):
        for i in r:
            if num % i != 0:
                return False
        return True
    r = xrange(n, 0, -1)
    m = n
    while not divisibleByRange(n, r):
        n += m
    return n

#Much faster solution. Find all the prime factors of each number in the range.
#Multiply each factor the greatest number of times in occurs in any number.
def lcm2(n):
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
    
    factors = defaultdict(int)
    for i in xrange(n, 0, -1):
        tempdict = defaultdict(int)
        for num, count in primeFactors(i).items():
            tempdict[num] += count
        for num, count in tempdict.items():
            if count > factors[num]:
                factors[num] = count
        tempdict.clear()
    res = 1
    for num, count in factors.items():
        res *= (num**count)
    return res
#     return reduce(lambda x,y: x*y, map(lambda t: t[0]**t[1], factors.items()))

start = timeit.default_timer()
print "LCM of all numbers from 1 to 20 is ", lcm1(20)
stop = timeit.default_timer()
print "Time:", stop - start

start = timeit.default_timer()
print "LCM of all numbers from 1 to 20 is ", lcm2(20)
stop = timeit.default_timer()
print "Time:", stop - start
