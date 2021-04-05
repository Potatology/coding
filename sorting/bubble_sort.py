numbers = [99,1,2,6,5,4]

def bubble_sort(numbers):
    passes_left = len(numbers)-1
    for onepass in range(passes_left, 0, -1):
            print(onepass)
            for i in range(0, passes_left):
                if is_larger(numbers[i], numbers[i+1]):
                    change_place(i, i+1, numbers)
    return numbers

def bubble_short(numbers):
    passes_left = len(numbers)-1
    haschanges = True
    while passes_left > 0 and haschanges:
        print(passes_left)
        haschanges = False
        for i in range(0, passes_left):
            if is_larger(numbers[i], numbers[i+1]):
                change_place(i, i+1, numbers)
                haschanges = True
        passes_left = passes_left - 1
    return numbers


def is_larger(prev, current):
    return prev > current

def change_place(i_prev, i_current,numbers):
    print('haschanges set to True')
    numbers[i_prev],numbers[i_current] = numbers[i_current],numbers[i_prev]



def test_bs():
    print(bubble_short(numbers))

test_bs()