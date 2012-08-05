# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="dean"
__date__ ="$31-Jul-2012 23:54:11$"

#   create a list to hold cache
fibonacciNumbers = []

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

def printNumber(index):
    #   Print the number with a specific index in the sequence
    print index, fibonacciNumbers[index]

def printCache():
    #   Dump contents of cache to console
    for x in range(0,len(fibonacciNumbers)):
        printNumber(x)

def startup():
    print "Building cache"
    buildCache(100000)
    print "Done"

if __name__ == "__main__":
    startup()
    printNumber(100000)