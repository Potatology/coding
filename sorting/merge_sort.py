A = [4,8,2,7,5,5,5]

def merge_sort(A):
    if len(A)>1:
        left = merge_sort(A[:len(A)//2])
        right = merge_sort(A[len(A)//2:])
        merge(A, left, right)
    return A

def merge(A, Aleft, Aright):
    i = 0
    j = 0
    k = 0
    while i < len(Aleft) and j < len(Aright):
        if Aleft[i] < Aright[j]:
            A[k] = Aleft[i]
            i+=1
            k+=1
        else: 
            A[k] = Aright[j]
            k+=1
            j+=1
    while i < len(Aleft):
        A[k] = Aleft[i]
        i+=1
        k+=1
    while j < len(Aright):
            A[k] = Aright[j]
            j+=1
            k+=1
    return A

print(merge_sort(A))    
