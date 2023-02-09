# generator demo

def mynum(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j % 7 == 0:
            yield j

x = mynum(100)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


# or

for i in mynum(50):
    print(i)



