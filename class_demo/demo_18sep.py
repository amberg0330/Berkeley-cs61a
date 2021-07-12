# factorial function 

def factorial(n):
    fact = 1 
    i = 1
    while i <= n: 
        fact *= i
        i += 1
    return fact 

# recursion 
# base case: 
# if n == 0
#  n! = 1

# recursive case: 
# if n > 0 
#  n! = n * (n-1)!

def factorial(n):
    if n == 0: 
        return 1 
    elif n > 0: 
        return n * factorial(n-1)


# order of recursive calls 
def casecade(n):
    if n < 10: 
        print(n)
    else: 
        print(n)
        casecade(n//10)
        print(n)

# identical with: 

def casecade2(n):
    print(n)
    if n >= 10: 
        cascade(n // 10)
        print(n)



# def xuxu_cascade(n):
#     if n < 10: 
#         print(n)
#     else: 
#         print(n)
#         xuxu_cascade(n//10)
#         print(n)

# def casecade2(n):
#     print(n)
#     if n >= 10: 
#         casecade2(n // 10)
#         print(n)
    

def reverse_cascade(n):
    
    grow(n//10)
    print(n)
    shrink(n//10)

def grow(n):
    if n >= 10:
        grow(n//10)
        print(n)
    else:
        grow(n)

def shrink(n):
    if n < 10:
        print(n)
    else:
        print(n)
        shrink(n//10)


## counting partitions 

def count_partitions(n, m):
    ##base case: 
    if n == 0: 
        return 1 
    elif n < 0: 
        return 0
    elif m == 0:
        return 0

    else: 
        within_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return within_m + without_m 

    
    
    

   
        


