alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
import random
random.seed()
#############################################################
# The following code doesn't need to be edited. It allows
# you to read a text file and store it in a single string, 
# and also to write a single string to a text file. This is
# not an ideal way to work with files, but it will suffice
# for this assignment.
#############################################################

def file_to_string(filename):
    with open(filename, "r") as f:
        x = f.read()
    return x

def string_to_file(filename, s):
    with open(filename, "w") as f:
        f.write(s)



#############################################################
# A working Caesar cipher
#############################################################

def simplify_string(s):
    "your code here"
    word_return = ''
    for char in s:
        if char.isalpha():
            word_return += char
    return word_return.upper()
print(simplify_string("Happy Birthday!"))

def num_to_let(x):
    "your code here"
    lst_of_alpha = []
    while len(lst_of_alpha) < 53:
        for num in range(65, 91):
            lst_of_alpha.append(chr(num))   
    for index in range(len(lst_of_alpha)):
        if index == x:
            return lst_of_alpha[x]
print(num_to_let(25))
    
def let_to_num(a):
    "your code here"
    lst_of_alpha = ''
    for num in range(65, 91):
        lst_of_alpha += chr(num)
    ctr = 0
    for char in lst_of_alpha:
        if char == a:
            return ctr
        ctr += 1
print(let_to_num("D"))

def shift_char(char, shift):
    "your code here"
    call_shift = let_to_num(shift)
    call_char = let_to_num(char)
    total_for_shift = call_shift + call_char
    return num_to_let(total_for_shift)
print(shift_char("Y", "D"))

def caesar_enc(plain, key):
    "your code here"
    caesar_return = ''
    for letter in plain:
        results = shift_char(letter, key)
        caesar_return += results
    return caesar_return
print(caesar_enc('GALAXY', 'D'))

def caesar_dec(cipher, key):
    "your code here"
    caesar_dec_add = ''
    for letter in cipher:
        caesar_dec_add += shift_char(letter, num_to_let(52 - let_to_num(key)))
    return caesar_dec_add
print(caesar_dec('JDODAB', 'D'))

#############################################################
# Breaking the Caesar cipher
#############################################################

def letter_counts(s):
    "your code here"
    lst_of_alpha = ''
    for num in range(65, 91):
        lst_of_alpha += chr(num)
    dict_of_letters = {}
    ctr = 0
    for letter1 in lst_of_alpha:
        dict_of_letters[letter1] = ctr
        for letter2 in s:
            if letter1 == letter2:
                ctr += 1
                dict_of_letters[letter1] = ctr
        ctr = 0
    return dict_of_letters
print(letter_counts('FABIAAN'))
    
def normalize(counts):
    "your code here"
    
    for key, value2 in counts.items():
        ctr = 0 
        for value1 in counts.values():
            ctr += value1
        counts[key] = value2 / ctr
        
    return counts
print(normalize({'A': 3, 'B': 1, 'C': 0, 'D': 0, 'E': 0, 'F': 1, 'G': 0, 'H': 0, 'I': 1, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 1, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}))


# Uncomment the code below once the functions above are complete
english_freqs = letter_counts(simplify_string(file_to_string("twocities_full.txt")))
normalize(english_freqs)

def distance(observed, expected):
    "your code here"

def caesar_break(cipher, frequencies):
    "your code here"



#############################################################
# A working Vigenere cipher
#############################################################

def vigenere_enc(plain, key):
    "your code here"

def vigenere_dec(cipher, key):
    "your code here"


#############################################################
# Breaking the Vigenere cipher
#############################################################

def split_string(s, parts):
    "your code here"

def vig_break_for_length(cipher, klen, frequencies):
    "your code here"

def vig_break(c, maxlen, frequencies):
    "your code here"



#############################################################
# A working substitution cipher
#############################################################

def sub_gen_key():
    "your code here"

def sub_enc(s, k):
    "your code here"

def sub_dec(s, k):
    "your code here"


#############################################################
# Breaking the substitution cipher
#############################################################

def count_trigrams(s):
    "your code here"

# Uncomment the code below once the functions above are complete
# english_trigrams = count_trigrams(simplify_string(file_to_string("twocities_full.txt")))
# normalize(english_trigrams)

def map_log(d):
    "your code here"

# Uncomment the code below once the functions above are complete
# map_log(english_trigrams) 

def trigram_score(s, english_trigrams):
    "your code here"

def sub_break(cipher, english_trigrams):
    "your code here"



