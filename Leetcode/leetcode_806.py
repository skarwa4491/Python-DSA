class Solution():
    
    def numberOfLines(self,widths,s):
        current_capacity =0
        lines =0
        output = []
        for char in range(len(s)+1):
            if current_capacity < 100:
                current_capacity += widths[char]   
            else:
                lines+=1
                current_capacity=0
    
        output.append(lines)
        output.append(current_capacity)
        return output
                
                
Solution().numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"abcdefghijklmnopqrstuvwxyz")