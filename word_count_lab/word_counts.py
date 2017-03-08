from collections import Counter

def words(word):
    """ Check the number of times an element appears in a word"""
    new_list = []
    
    for i in word.split():
        new_list.append(i)
    return Counter(new_list)

    

        


