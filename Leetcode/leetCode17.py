class Solution:
    mappings = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz",
    }

    def letterCombinations(self, digits):
        if digits =="":
            return [""]
        
        c = digits[0]
        rod = digits[1:] 
        
        ros_words = self.letterCombinations(rod)
        result =[]
        for word in ros_words:
            for ch in self.mappings.get(int(c)):
                result.append(ch+word)
        result.sort()
        return result

result = Solution().letterCombinations("23")
print(result)
