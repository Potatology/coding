import timeit

def test1(): 
    l = []
    for i in range(1000):
        l+=[i]
    print(len(l))

def test2():
    l = []
    for i in range(1000):
        l.append(i)
    print(len(l))

def test3():
    l = [i for i in range(1000)]
    print(len(l))

def test4():
    l = list(range(1000))
    print(len(l))

test1()
test2()
test3()
test4()