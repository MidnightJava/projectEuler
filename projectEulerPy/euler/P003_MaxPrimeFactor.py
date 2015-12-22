'''
Created on Dec 12, 2015

@author: Mark
'''
import timeit

def factors(n):
    def prime(n):
        for m in xrange(2, n/2, 2):
            if n % m == 0:
                return False
        return True
    fList = []
    found = False
    for m in xrange(2, n/2):
        if n % m == 0:
            fList += factors(n/m)
            found = True
            break
    if not found:
        fList.append(n)
    return [f for f in fList if prime(f)]

def factors2(n):
    m = 2
    f = n
    while (m < n/m):
        if n % m == 0:
            f = n / m
            n /= m
            m = 2
        m += 1
    return f

def factors3(n):
    def maxFactor(n):
        for m in xrange(2, n/2):
            if n % m == 0:
                return n / m
        return -1
    
    a = f = maxFactor(n)
    while f > 0:
        a = n = f
        f = maxFactor(n)
    return a
    
start = timeit.default_timer()
print "#1 Max prime factor of 600851475143 is", max(factors(600851475143))
stop = timeit.default_timer()
print "Time:", stop - start

start = timeit.default_timer()
print "#2: Max prime factor of 600851475143 is", factors2(600851475143)
stop = timeit.default_timer()
print "Time:", stop - start

start = timeit.default_timer()
print "#3: Max prime factor of 600851475143 is", factors3(600851475143)
stop = timeit.default_timer()
print "Time:", stop - start


#factors() and factors3() failed to complete when run with a much larger numbe,
#but factors2() seems to work for all numbers

#Time: 0.00138902664185
#2: Max prime factor of 600851475143 is 6857
#Time: 0.000735998153687
#3: Max prime factor of 600851475143 is 6857
#Time: 0.000617980957031
        