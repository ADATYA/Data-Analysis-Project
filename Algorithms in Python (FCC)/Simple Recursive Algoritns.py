## Leasson 01...

# Simple Recursive Algorithms

 
# Factorial-1:

# way 1
def itarative_factorial(n):
    fact = 1
    for i in range (2 , n+1):
        fact*=i
    return fact
print(itarative_factorial(5))

# way 2
def recur_function(n):
    if n == 1:
        return n
    else:
        temp = recur_function(n-1)
        temp = temp *n
    return temp

print(recur_function(5))

# Way 3

def recur_function(n):
    if n==1: return n
    else :return n * recur_function (n-1)
print(recur_function(5))


# Perrmutation -1(Advanced):

def permute (string , pocket=""):
    if len(string) ==0:
        print(pocket)
    else:
        for i in range(len(string)): 
            letter = string[i]
            front =string [0:i]
            back = string[i+1:]
            toghter = front + back
            permute(toghter , letter + pocket)

print(permute("ABCD"))


# 8/N Queens Problem (Mind Breaker)::

