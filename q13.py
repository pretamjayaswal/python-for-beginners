string = input()

result = {
    'digit':0,
    'alpha':0
}

for char in string:
    if char.isdigit():
        result['digit'] += 1
    else:
        result['alpha'] += 1

print(result)