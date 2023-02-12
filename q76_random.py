import random

print(random.choice([x for x in range(0,1000) if x%5==0 and x%7==0]))


print(random.sample(range(100),5))


print(random.sample([x for x in range(100,200) if x%2==0],5))