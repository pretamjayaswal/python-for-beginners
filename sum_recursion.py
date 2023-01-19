

def sumnum(n):
    n = int(n)
    if n == 0: 
        return 0
    else:
        return n % 10 + sumnum(n//10)
    
print(sumnum(12340))

