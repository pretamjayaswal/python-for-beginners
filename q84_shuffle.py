li = [5,6,77,45,22,12,24]

print([x for (i,x ) in enumerate(li) if i not in (1,4,5)])