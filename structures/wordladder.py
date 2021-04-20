
def word_ladder(word_list):
    g = {}
    for word in word_list:
        g[word] = []
    buckets = {}
    for word in word_list:
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i + 1:]
            if bucket in buckets:
                buckets[bucket].append(word)
            else:
                buckets[bucket] = [word]
    for bucket in buckets.keys():
        #print(f'{bucket} : {buckets[bucket]}')
        for word1 in buckets[bucket]:
            for word2 in buckets[bucket]:
                if word1 != word2:
                    g[word1].append(word2)
    return g
word_list = ['pope','rope','dope','nope','cope','lope','mope','pipe','pape','pepe','pype','pole','pore','pose','poke','pops','popz','popr','popg']

print(word_ladder(word_list))





