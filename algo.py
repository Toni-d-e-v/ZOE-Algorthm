# ZUE Algorithm
# Encrypting algorithm
import random
import json
from random import shuffle 







# reverse dictonary
def reverse_dictonary(dictonary):
    # Reverse dictonary
    # Input: dictonary
    # Output: dictonary
    reverse_dictonary = {}
    for key in dictonary:
        reverse_dictonary[dictonary[key]] = key
    return reverse_dictonary


def split_string_to_array(string):
    # Split string to array
    # Input: string
    # Output: array
    return list(string)



def get_cordinates(string):
    # Get cordinates of letter
    # Input: string
    # Output: json
    cordinates = {}
    for i in range(len(string)):
        if string[i] in cordinates:
            cordinates[string[i]].append(i)
        else:
            cordinates[string[i]] = [i]
    return cordinates


# from string array get string
def get_string_from_array(array):
    # Get string from array
    # Input: string array
    # Output: string
    return ''.join(array)



# from cordinates get an dictonary where H = 0 E = 1 L = 2 L = 3 O = 3
def get_dictonary(cordinates):
    # Get dictonary from cordinates
    # Input: cordinates
    # Output: dictonary
    dictonary = {}
    for key in cordinates:
        for i in cordinates[key]:
            dictonary[i] = key
    return dictonary
# from cordinates get string
def get_string_from_cordinates(cordinates):
    # Get string from cordinates
    # Input: cordinates
    # Output: string
    x = cordinates
    s = ["" for v in x.values() for _ in v]
    for k, v in x.items():
        for i in v:
            s[i] = k
    return s   


# get letter in letter map
def get_letter(letter, letter_map_upper_case, letter_map_lower_case):
    if letter in letter_map_upper_case:
        return letter_map_upper_case[letter]
    elif letter in letter_map_lower_case:
        return letter_map_lower_case[letter]
    else:
        return letter
# get letter in reversed letter map
def get_letter_ref(letter, letter_map_upper_case, letter_map_lower_case):
    letter_map_lower_case = reverse_dictonary(letter_map_lower_case)
    letter_map_upper_case = reverse_dictonary(letter_map_upper_case)
    if letter in letter_map_upper_case:
        return letter_map_upper_case[letter]
    elif letter in letter_map_lower_case:
        return letter_map_lower_case[letter]
    else:
        return letter
def join_array_to_string(array):
    # Join array to string
    # Input: array
    # Output: string
    return ''.join(array)
def encrypt(string, letter_map_upper_case, letter_map_lower_case):
    # Encrypt string
    # Input: string and letter map
    # Output: string
    string_array = split_string_to_array(string)
    cordinates = get_cordinates(string_array)
    dictonary = get_dictonary(cordinates)
    for i in range(len(string_array)):
        if i in dictonary:
            string_array[i] = get_letter(string_array[i], letter_map_upper_case, letter_map_lower_case)
    return get_cordinates(string_array)

# Function that joins the array to a string


def decrypt(string, letter_map_upper_case, letter_map_lower_case):
    # Decrypt string
    # Input: string and letter map
    # Output: string
    string = get_string_from_cordinates(string)
    string_array = split_string_to_array(string)
    cordinates = get_cordinates(string_array)
    dictonary = get_dictonary(cordinates)
    for i in range(len(string_array)):
        if i in dictonary:
            string_array[i] = get_letter_ref(string_array[i], letter_map_upper_case,letter_map_lower_case)
    return join_array_to_string(string_array)




# randomize letter maps one with upper and one with lower case
def randomize_letter_maps(letter_map_upper_case, letter_map_lower_case):
    valLetters = list(letter_map_upper_case.values())
    valLetters_lower = list(letter_map_lower_case.values())
    shuffle(valLetters)
    shuffle(valLetters_lower)
    letter_map_upper_case = dict(zip(letter_map_upper_case.keys(), valLetters))
    letter_map_lower_case = dict(zip(letter_map_lower_case.keys(), valLetters_lower))
    return letter_map_upper_case, letter_map_lower_case





# crete random 2 letter maps one with upper and one with lower case
def create_random_letter_map():
    # Create random 2 letter maps one with upper and one with lower case
    # Input: letter map upper case and letter map lower case
    # Output: letter map upper case and letter map lower case
    letter_map_upper_case = {}
    letter_map_lower_case = {}
    for i in range(26):
        # make 2 maps with random letters 
        letter_map_upper_case[chr(i + 65)] = chr(i + 65)
        letter_map_lower_case[chr(i + 97)] = chr(i + 97)
        # randomize the maps
        letter_map_upper_case, letter_map_lower_case = randomize_letter_maps(letter_map_upper_case, letter_map_lower_case)
    return letter_map_upper_case, letter_map_lower_case


# get random letter map



def encrypt_new(string,key,out):
    letter_map_upper_case, letter_map_lower_case = create_random_letter_map()
    enc = encrypt(string,letter_map_lower_case,letter_map_upper_case)
    keys = {
        'lower': letter_map_lower_case,
        'upper': letter_map_upper_case
    }

    # save keys to file
    
    with open(key, 'w') as outfile:
        json.dump(keys, outfile)
    with open(out, 'w') as outfile:
        json.dump(enc, outfile)
def decrypt_new(string,keys,output):
    # read keys.json
    # load json string
    
    with open(keys) as json_file:
        data = json.load(json_file)
        letter_map_lower_case = data['lower']
        letter_map_upper_case = data['upper']

    with open(string) as json_file:
        data = json.load(json_file)
    dec = decrypt(data, letter_map_lower_case, letter_map_upper_case)

    with open(output, 'w') as outfile:
        json.dump(dec, outfile)
