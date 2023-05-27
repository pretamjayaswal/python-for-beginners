
str1="the golden day"

def getlength1(s: str) -> int:
    return len(s)


def getlength2(s: str) -> int:
    i = 0
    for _ in s:
        i += 1
    return i

def getlength3(s: str) -> int:
    counter = 0
    
    while s[counter:]:
        counter += 1

    return counter

def getlength4(s: str) -> int:
    counter = 0
    if s:
        counter += 1
        return counter + getlength4(s[counter:])
    return counter

def get_length_without_spaces(s:str) -> int:
    counter = 0 
    for x in s:
        if x == ' ':
            continue
        counter += 1
    return counter

def get_length_without_spaces2(s:str) -> int:
    x = [not chr.isspace() for chr in s]
    # print(x)
    return sum(x)




print(getlength1(str1))
print(getlength2(str1))
print(getlength3(str1))
print(getlength4(str1))
print(get_length_without_spaces("hi joe kk"))
print(get_length_without_spaces2("hi joe kk"))