def find_duplicate_brackets(arr):
    stack = []
    is_duplicates = False
    for ch in arr:
        if ch != ')':
            stack.append(ch)
        else:
            if stack[-1] == '(':
                is_duplicates = True
                return is_duplicates
            while stack[-1] != '(':
                stack.pop()
            stack.pop()
            
    return is_duplicates


print(find_duplicate_brackets('((a+b)+(c+d))'))
print(find_duplicate_brackets('(a+b)+((c+d))'))
