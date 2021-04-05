import stack

def balancedParents(parents):
    closedParentStack = stack.Stack()
    for parent in parents:
        if parent=='(':
            closedParentStack.push(')')
        else:
            if closedParentStack.isEmpty():
                return False
            else: 
                closedParentStack.pop()
    return closedParentStack.isEmpty()

            
print(balancedParents('((())()()((())))'))