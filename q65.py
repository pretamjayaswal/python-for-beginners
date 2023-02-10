

def calc(n):
    if n == 0 :
        return 0
    else:
        return calc(n-1) + 100

print(calc(5))


