class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n >=1 and n <= 9:
            return -1
        digits = [int(x) for x in str(n)]
        flag = False
        for i in range(len(digits)-1,0,-1):
            if digits[i-1] < digits[i]:
                low = i-1
                hi = i
                while (low < len(digits) and hi < len(digits)):
                    flag = True
                    digits[low],digits[hi] = digits[hi],digits[low]
                    low+=1
                    hi+=1
                break
        if flag:
            digits = [str(x) for x in digits]
            result = ''.join(digits)
            return int(result)
        else:
            return -1

print(Solution().nextGreaterElement(230241))