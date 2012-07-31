# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="dean"
__date__ ="$31-Jul-2012 23:54:11$"

def add(a,b):
    return a + b

if __name__ == "__main__":
    c = 1   #   n (current number)
    b = 0   #   n - 1
    a = 0   #   n - 2
    
    print(0)
    print(1)
    
    for a in range(100):
        a = b
        b = c
        c = add(a,b)
        print(c),