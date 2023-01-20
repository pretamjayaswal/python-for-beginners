

def ireverse(string)->str:
    if len(string) == 0:
        return string
    else:
        return ireverse(string[1:]) + string[0]

print(ireverse("stay hungry, stay foolish"))


