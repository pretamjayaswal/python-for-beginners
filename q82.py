import gzip

string = b"JHjs jshjhsjh sjs jhsjh sjhs jhs"
t = gzip.compress(string)

print(t)

y = gzip.decompress(t)
print(y)
