def pullword(word_file,minle,maxle):
    validword = false
    while validword:
        fp = open(word_file,'r')
        w_index = random.randint(0,466550)
        for x in range(0,w_index):
            fp.readline()
        word = fp.readline()
        ##put valid word checker here
        fp.close()
    return word
