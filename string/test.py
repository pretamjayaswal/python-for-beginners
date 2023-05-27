


list = [
{"name": "Nandini",
 "age": 20},
 {"name": "Manjeet",
   "age": 28},
  {"name": "Nikhil", 
   "age": 19}]

list.sort(key = lambda x: x['age'])
print(list)