import stack

def decimalToBinary(decNum):
    binStack = stack.Stack()
    binNumStr = ''
    while decNum > 0:
        binStack.push(decNum % 2)
        decNum = decNum // 2
    while not binStack.isEmpty():
        binNumStr += str(binStack.pop())
    return binNumStr

print(decimalToBinary(589))
