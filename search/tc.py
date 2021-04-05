def nextGreatestLetter(letters, target):
        n = len(letters)-1
        low, high = 0, n
        if target<letters[0]:
            return letters[0]
        if target>=letters[n]:
            return letters[0]
        
        res = None
        while low<=high:
            mid = (low+high)//2
            if target>=letters[mid]:
                low=mid+1
            else:
                res = letters[mid]
                high = mid-1
        return res


letters = ['c','f','g']
target = 'c'

print(nextGreatestLetter(letters, target))