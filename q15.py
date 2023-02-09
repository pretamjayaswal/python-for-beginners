# a + aa +aaa+aaaa for a digit 'a'


a = input("provide a number between 0 to 9 :")
sum = 0
for i in range(1,5):
    num = int(a * i)
    sum += num

print(sum)