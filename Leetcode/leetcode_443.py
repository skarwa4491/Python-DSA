class Solution:
    def compress(self, chars):
        result = [chars[0]]
        count =1
        for curr_char in chars[1:len(chars)]:
            if curr_char == result[-1]:
                count +=1
            else:
                if count >1:
                    result.append(str(count))
                result.append(curr_char)
                count = 1
        if count>1:
            result.append(str(count))
        print(result)
        return len(result)
                    
Solution().compress(["a","a","b","b","c","c","c"])