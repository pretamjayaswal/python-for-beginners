
def gcd(a,b):
    max,min = (a,b) if a>b else (b,a)
    print(max,min)

    gcd = 'None'

    for num in range(2,min):
        if a % num == 0 and b % num == 0:
            print('==============',num,'===============')
            gcd = num
    
    return gcd



print(gcd(25,45))