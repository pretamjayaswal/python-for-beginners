# sum_range 
def sumn(n):
    if n <= 1:
        return n
    else:
        return n + sumn(n-1)


print(sumn(0))