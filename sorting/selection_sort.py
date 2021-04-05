
A = [100000002,5,6,9,2,3,1]

def sel_sort(A):
    num_passes = len(A)
    while num_passes > 0:
        max_index = 0
        for i in range(0, num_passes):
            if A[i] > A[max_index]:
                max_num = A[i]
                max_index = i
        A[max_index], A[num_passes-1] = A[num_passes-1], A[max_index]
        num_passes -= 1
    return (A)

print(sel_sort(A))