import sys
sys.setrecursionlimit(10**6)

class Solution():
    def printSubSequence(self,seq):
        if seq == "":
            return [""]
        ch = seq[0]
        rseq = seq[1:]
        result = self.printSubSequence(rseq)
        actual_result_y=[ch+s for s in result]
        actual_result_n=[s for s in result]
        return actual_result_y+actual_result_n
        
str = input()
result = Solution().printSubSequence("abc")
print(result[::-1])