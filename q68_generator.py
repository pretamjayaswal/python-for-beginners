def gen_even(n):
    i = 0
    while i < n:
        if i%2==0:
            yield i
        i += 1

x = gen_even(50)

print(x)
# for i in x:
#     print(i)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
