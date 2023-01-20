

def toh(n,source,destination ,auxillary):
    if n==1:
        print("Move disk 1 from ",source," to destination ",destination)
        return 

    toh(n-1, source, auxillary,destination)
    print("Move disk",n,"from ",source," to destination ",destination)
    toh(n-1,auxillary,destination,source)


n=100
toh(n,"A","B","C")

