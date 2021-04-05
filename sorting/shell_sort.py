def shellsort(A):
    sublistcount = len(A)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(A,startposition,sublistcount)
            print("After increments of size", sublistcount, "The list is",A)
            sublistcount // 2

def gatInsertionSort(A,start,gap):
    for i in range(start+gap,len(A),gap):
        current = A[i]
        position = i
        while position>=gap and A[position-gap]>current:
            A[position]=A[position-gap]
            position = position - gap
        A[position]=current