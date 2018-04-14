from itertools import count

def count_empty_lines(source):
    """
    counts empty lines in text file named source
    """
    counter = source()
    with open(afile.txt, 'r') as f:
        for line in f.readlines():
            if not line.strip():
                source.next
        return source

def count_at_start(word, source):
    """
    counts occurences of word at the start of lines
    in a file source
    """
    count = 0
    for word in source:
        if firstchar(word) == word:
            count = count + 1
    return count


def split_fname(source):
    """
    puts a ',' between words in the file
    """
    x = source.split(',')
    for word in source:
        print word
