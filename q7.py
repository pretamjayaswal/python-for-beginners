

x = int(input('X (rows):'))
y = int(input('Y (column):'))

matrix = [[x*y for y in range(y)] for x in range(x)]

print(matrix)

