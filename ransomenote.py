import time

#magazine[a,b,c,d,e,e,d,d,c]
#note[cabdedec]
#note[abdedecz]

def ransomeNote(magazine, rNote):
    magCharSet=dict.fromkeys(magazine, 0)
    for char in magazine:
        magCharSet[char]+=1
    for char in rNote:
        if char not in magCharSet: return False 
        elif magCharSet[char]>=1:
            magCharSet[char]-=1
        else: return False
    return True

def ransomeNoteClean(magazine, rNote):
    if ransomeNote=='':
        return True
    if ransomeNote=='' and magazine=='':
        return True
    if magazine=='':
        return False
    
    magCharSet=dict.fromkeys(magazine, 0)
    for char in magazine:
        magCharSet[char]+=1
    for char in rNote:
        if magCharSet[char]<=0:
           return False
        magCharSet[char]-=1
    return True


def ransomeNoteCrossOut(magazine, rNote):
    for i in rNote:
        if i not in magazine:
            return False
        else: 
            magazine[magazine.index(i)]=None
    return True

def timer(func, *args):
    start = time.process_time()
    for i in range(1000):
        func(*args)
    return time.process_time()-start
    
print(timer(ransomeNoteCrossOut, ['a','b','c','d','e','e','d','d','c']*10000, 'ceddd'*10000))
print(timer(ransomeNote, ['a','b','c','d','e','e','d','d','c']*10000, 'ceddd'*10000))
#print(timer(ransomeNoteClean, ['a','b','c','d','e','e','d','d','c']*10000, 'ceddd'))


#print(ransomeNoteClean(['a','b','c','d','e','e','d','d','c'],'adasd'))