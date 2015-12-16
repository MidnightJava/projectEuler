'''
Created on Dec 16, 2015

@author: maleone
'''

print sum(xrange(1, 101)) ** 2 - sum(map(lambda x: x**2, xrange(1, 101)))
