# Ractangle w=10 and h=4res
result = []

def maxsq(width, height):

    side = height
  
    while  height >= 0 and width >= 0 and side > 0:
        dimension = (width,height)
        height = min(dimension)
        width = max(dimension)
        side = height
      
        if side > 0:
            result.append(f'{side} x {side}')

        width = width - side
    
    return result


print(maxsq(4,4))

