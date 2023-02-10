

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # result.append()
        return fibo(n-1) + fibo(n-2)


n = int(input())   

res  = [fibo(x) for x in range(0,n+1) ]

print(res)