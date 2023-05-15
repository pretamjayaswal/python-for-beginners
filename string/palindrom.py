s1 = "welcome"
s2 = "baasaab"

def chk_palindrom(string):
    return string == string[::-1]


print(chk_palindrom(s1))
print(chk_palindrom(s2))