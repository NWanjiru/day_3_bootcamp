def word_counts(word):
  """ Check the number of times an element appears in a word"""
    repeat = []
    length = len(word)
    count =0
    counter =[]
    words = {}
    for l in range(0,length):
        for c in range(l +1, length):
            if word[l] == word[c]:
                repeat.append(word[l])
                print(repeat)
            
                count = count +1
                counter.append(count)
            count +=1
    print(counter)
