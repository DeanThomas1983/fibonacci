# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="dean"
__date__ ="$31-Jul-2012 23:54:11$"

from array import *

#   create an array of 4 byte long positive integers
fibonacciNumbers = array('l')

def add(a,b):
    #   simply return a sum of two numbers
    return a + b

def buildCache(maximum):
    #   Manually insert the first two numbers
    fibonacciNumbers.append(0)
    fibonacciNumbers.append(1)
    
    for x in range(1,maximum):
        #   Next number will be the sum of the two numbers
        #   currently at the end of the list
        c = add(fibonacciNumbers[x-1],fibonacciNumbers[x])
        fibonacciNumbers.append(c)

def printCache():
    #   Dump contents of cache to console
    for x in range(0,len(fibonacciNumbers)):
        print x, fibonacciNumbers[x]

def startup():
    print "Building cache"
    buildCache(70)
    print "Done"

if __name__ == "__main__":
    startup()
    printCache()