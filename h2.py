def compare(x,y):
    """Compare 2 numbers.
    x,y integer
    Return 0 if x and y are equal
    -1 if x <y
    1 if x>y"""

    if x == y:
        return 0
    elif x < y:
        return -1
    else:
        return 1

# compare(10, 5)
# compare(3, 3)
# compare(2, 6)

def is_between(x,y,z):
    """Decide if the 2nd number is in interval [x,z],
    including the margins.
    x,y,z: integer
    Return: true if x <= y <=z, false otherwise"""

    if x <= y <= z:
        return True
    else:
        return False
# is_between(1, 2, 3)
# is_between(9,8,7)
# is_between(3, 3, 3)


def find_index(letter, word):
    """find index of first occurence of letter in word.
    letter:one-character string
    word:string
    return: -1 on failure"""

    for letter in word:
        letter.find(word)
    return word
#find_index('d', 'dog')
#find_index('c', 'cat')
#find_index('o', 'fox')


def remove_leading_blanks(sentence):
    """return copy of sentence with leading blanks removed.
    sentence: string
    return: string"""

    pass

def make_title(word_list):
    """capitalize words in word_list
    word_list: list of strings
    returns: copy of word_list where all original words
    are capitalized"""
    capitalized_word_list = [ ]
    for word in word_list:
        capword= word.upper()
        capitalized_word_list.append(capword)
    return capitalized_word_list

# make_title(['dog', 'cat'])
# make_title(['today', 'is', 'friday'])
# make_title(['mon', 'tues', 'wed'])

def shorter_than_5(word_list):
    """filter out strings that are shorter than 5 in word_list
    word_list:string with whitespacce-seperated strings
    returns:copy of word_list where all words have lenfth 5 or higher"""
    for word in word_list:
        if len(word_list) < 5:
    return word_list

# shorter_than_5([umbrella, tree, coconut, cat])
# shorter_than_5([purse, Hi, two])
# shorter_than_5([cake, lemon, fan, can])
