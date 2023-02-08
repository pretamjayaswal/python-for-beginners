import math

def calc_q(d):
    c = 50
    h = 30
    return math.sqrt((2*c*d)/h)


user_input = int(input('Enter value:'))

print(round(calc_q(user_input)))
