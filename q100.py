# Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

def soln(numheads, numlegs):
    ns = 'No solution'
    for chicken in range(1,numheads+1):
        rabbit = numheads - chicken
        if 2*chicken + 4*rabbit == numlegs:
            return chicken,rabbit

print(soln(2,6))
