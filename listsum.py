numbers = [1,2,3,4,5]

def list_sum(numbers):
    if len(numbers) == 1:
        return numbers[0]
    return numbers[0] + list_sum(numbers[1:])


print([0]*63)