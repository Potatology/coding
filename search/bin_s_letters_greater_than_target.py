def nextGreatestLetter(self, letters, target):
    low = letters[0]
    high = len(letters) - 1
    while low != high:
        middlePoint = (low + high) // 2
        guess = letters[middlePoint]
        if guess == target:
            if letters[middlePoint + 1]:
                return middlePoint + 1
            else:
                return 0
        elif guess < target:
            low = middlePoint + 1
        elif guess > target:
            high = middlePoint - 1
    if letters[low] > target:
        return low
    elif letters[low] < target and low == len(letters):
        return 0




    


