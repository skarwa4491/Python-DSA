from os import remove


def removeDuplicates(s: str) -> str:
        result = []
        result.append(s[0])
        for ch in s[1:]:
            if len(result)>0 and ch==result[-1]:
                result.pop()
            else:
                result.append(ch)
        return ''.join(result)
    
print(removeDuplicates('abbaca'))