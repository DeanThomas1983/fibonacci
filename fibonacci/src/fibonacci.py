# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="dean"
__date__ ="$31-Jul-2012 23:54:11$"

from array import *

fibonacciNumbers = array('l')

def add(a,b):
    return a + b

def buildCache(maximum):
    c = 1   #   n (current number)
    b = 0   #   n - 1
    a = 0   #   n - 2
    
    #   Manually insert the first two numbers
    fibonacciNumbers.append(0)
    fibonacciNumbers.append(1)
    
    for x in range(maximum-2):
        a = b
        b = c
        c = add(a,b)
        fibonacciNumbers.append(c)
        #print(c),

def printCache():
    for x in fibonacciNumbers:
        print(x),

if __name__ == "__main__":
    buildCache(50)
    printCache()