

data = [("pritam",86,6),("Ajay",80,3),("Ajay",96,8),("zubin", 99, 2),("tumpi",98,4)]

x = sorted(data, key = lambda x:x[1], reverse=True)
print(x)