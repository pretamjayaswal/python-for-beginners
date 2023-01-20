# LCM of two numbers

def lcm(a,b):
    greator = a if a>b else b
    
    while True:
        
        if (greator % a == 0 and greator % b == 0):
            lcm = greator
            break
        else:
            greator += 1
    
    return lcm

print(lcm(2,5))