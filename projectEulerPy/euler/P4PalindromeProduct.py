'''
Created on Dec 14, 2015

@author: maleone
'''
import timeit

def isPalindrome(num):
    return str(num) == str(num)[::-1]

#Method 1: Try all 3-digit number combinations for n1, all combinations
#that are multiples of 11 for n2
start = timeit.default_timer()
n1 = 999
n2 = 990
toggle = 0
maxP = 0
f1 = f2 = 0
while n1 > 0:
    while n2 > 0:
        p = n1 * n2
        if p > maxP and isPalindrome(p):
            f1 = str(n1)
            f2 = str(n2)
        maxP = p if p > maxP and isPalindrome(p) else maxP
        n2 -= 11
    n2 = 990
    n1 -= 1
stop = timeit.default_timer()
print "#1 Largest palindrome", maxP
print "Time:", stop - start

#Method 1: Least significant digits constrained to factors of 9, try all combinations for remaining two digits
start = timeit.default_timer()
maxP = 0
factors = [[1, 9], [9, 1], [3, 3]]
for pair in factors:
    for x in xrange(0, 100):
        n1 = x * 10 + pair[0]
        for y in xrange(0, 100):
            n2 = y * 10 + pair[1]
            p = n1 * n2
            maxP = p if p > maxP and isPalindrome(p) else maxP
stop = timeit.default_timer()
print "#2 Largest palindrome", maxP
print "Time:", stop - start