from operator import truediv


def balanced(str):
    stack = []
    for ch in str:
        if ch == '(' or ch == '[' or ch == '{':
            stack .append(ch)
        elif ch == ')' or ch == ']' or ch == '}':
            if len(stack) == 0:
                return False
            elif ch == ')' and stack[-1] == '(':
                stack.pop()
            elif ch == ']' and stack[-1] == '[':
                stack.pop()
            elif ch == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False

    return True if len(stack) == 0 else False


print(balanced('[(a+b)+{(c+d)*(e/f)}]'))
print(balanced('[(a+b)+{(c+d)*(e/f)]}'))
