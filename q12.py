#  get all numbers with even digits between start and end range with tracemalloc

import tracemalloc 

tracemalloc.start()

start = 1000
end = 5000

result = list()

snap1 = tracemalloc.take_snapshot()

for num in range(start,end):
    flag = True
    tnum = num
    while num > 0:
        i = num % 10
        if i%2 != 0:
            flag = False
        num = num // 10

    if flag:
        result.append(tnum)
snap2 = tracemalloc.take_snapshot()

stats = snap1.compare_to(snap2, 'lineno')
print("-----------------------TraceMalloc Data --------------------------------------")
for stat in stats:
    print(stat)
print("------------------------------------------------------------")
print(result)
