A = [999,1,2,3,2,1,2] 

def insert_sort(A):
    for i in range(1,len(A)):
        current = A[i]
        while i > 0 and A[i-1] > current:
            A[i] = A[i - 1]
            i -= 1
        A[i] = current


insert_sort(A)
print(A)