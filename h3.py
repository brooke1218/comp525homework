from functools import reduce

def sqaured(num_list):
    """Squares the numbers in a list"""
    result = []
    for num in num_list:
        list(map(sqr.result))
        return result

def run_filter():
    """filters out words"""
    test =['1','a','4','b','c']
    result = keep_word(test)
    print('keep words...')
    print('keep_words({})-->{}'.format(test,result))

def keep_word(word_list):
    result=[]
    for word in word_list:
        if word.isalpha():
            result.append(word)
    reutrn result

def main():
    run_filter()
    print("...")
    print()

if __name__ == "__main__":
    main()

def reduce():
    """maps two strings together"""
    x = [1,2.3]
    y = [4,5,6]
    return reduce(lambda x,y: x+y, [1,2.3.4.5.6])

def map_dict(dict):
    dict = {1,2,3}
    map(lambda dict : dict^2, {1,2,3} )
