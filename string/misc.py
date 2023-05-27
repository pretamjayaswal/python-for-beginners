str1 = "This is a so fab test string"
str2="justanotherstring"


def print_even_length_words(s:str)->None:
    s = s.split()
    result = []
    for word in s:
        if not len(word) % 2:
            result.append(word)

    print(result)

# print_even_length_words(str1)

def uppercase_half_string(s:str) -> None:
    mid = len(s)//2
    result =  s[:mid].upper()+s[mid:]
    print(result)
# uppercase_half_string(str1)
# uppercase_half_string(str2)

def capitalize_first_and_last_char_string(s:str):
    word_list = s.split()
    result = []
    for word in word_list:
        if len(word) != 1:
            new_word = word[0].upper() + word[1:-1] + word[-1].upper()
        else:
            new_word = word[0].upper()
        
        result.append(new_word)
    print(result)
    
# capitalize_first_and_last_char_string(str1)


# 
def count_matching_chars_in_strings(s1:str, s2:str) -> int:
    set1 = set(s1)
    set2 = set(s2)
    result = set1.intersection(set2)
    print(list(result))
    return len(result)

# print(count_matching_chars_in_strings(str1, str2))

def remove_all_duplicates1(s:str):
    '''
    it kepts order
    '''
    result = ''
    for char in s:
        if char not in result:
            result += char
    print(result)

def remove_all_duplicates2(s:str):
    '''
    it ignores order
    '''
    result = set(s)
    print(''.join(result))

# remove_all_duplicates1("geeksforgeeks")
# remove_all_duplicates2("geeksforgeeks")

def frequency_of_chars(s:str):
    freq = {}
    for char in s:
        freq[char] = freq.get(char,0) + 1
    print(freq)

    print(freq.keys())
    print(freq.values())
    print(freq.items())
    min_item, min_freq = '',0

    for i in freq.items():

        if i[1]<min_freq:
            min_freq = i[1]
            min_item = i
    print(min_item)
    print('----------------------------')
    max_freq = max(freq, key = lambda x : freq[x])
    min_freq = min(freq, key = freq.get)
    print(f'max item is {max_freq}')
    print(f'min item is {min_freq}')
  

# frequency_of_chars(str1)
# frequency_of_chars(str2)









