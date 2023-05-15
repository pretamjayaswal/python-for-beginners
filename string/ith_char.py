'''
Different approaches for ith char removal
'''
str1 = "thegoodway"

def remove_pos1(str:str, pos:int)->str:
    return str[:pos]+str[pos+1:]

def remove_pos2(str:str, pos:int) -> str:
    result = ''
    for i,chr in enumerate(str):
        if i == pos:
            continue
        result += chr
    
    return result

def remove_pos3(str:str, pos:int) -> str:
    return str.replace(str[pos],'',1)

def remove_pos4(str:str, pos:int)->str:
    result = ''.join([str[i] for i in range(len(str)) if i != pos])
    return result


def remove_pos5(mystr:str, pos:int) -> str:
    tbl = str.maketrans(mystr[pos],'_')
    return mystr.translate(tbl)

# using recursion
def remove_ith(mystr:str, pos:int) -> str:
    if pos == 0 :
        return mystr[1:]
    
    return mystr[0] + remove_ith(mystr[1:],pos-1)





print(remove_pos1(str1,2))
print(remove_pos2(str1,2))
print(remove_pos3(str1,2))
print(remove_pos4(str1,2))
print(remove_pos5(str1,2))
print(remove_ith(str1,2))
