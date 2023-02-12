'''
demo
'''
import time

start = time.time()

for i in range(2000000000):
    x = i*i

end = time.time()

print(end-start, " Seconds")