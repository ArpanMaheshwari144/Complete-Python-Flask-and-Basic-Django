openList = ['(', '{', '[']
closeList = [')', '}', ']']
checker = dict(zip(openList, closeList))


def isComplete(input):
    stack = []
    for char in input:
        if char in openList:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            if checker[stack[-1]] == char:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


print(isComplete('[(({}))]'))
