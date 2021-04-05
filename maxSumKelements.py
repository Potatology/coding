# Given an array of integers of size ‘n’.
# Our aim is to calculate the maximum sum possible for ‘k’ consecutive elements in the array.

# Input  : arr[] = {100, 200, 300, 400}
#          k = 2
# Output : 700

def maxSumKElem(arr, k):
for i in len(arr) - k - 1:
    for j