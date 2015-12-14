'''
Created on Dec 14, 2015

@author: maleone
'''
#brute force
import timeit

start = timeit.default_timer()
def isPalindrome(num):
    return str(num) == str(num)[::-1]

n1 = n2 = 999
toggle = 0
maxP = 0
while n1 > 0:
    while n2 > 0:
        p = n1 * n2
        maxP = p if p > maxP and isPalindrome(p) else maxP
        n2 -= 1
    n2 = 999
    n1 -= 1
print "Largest palindrome", maxP
stop = timeit.default_timer()
print "Time:", stop - start