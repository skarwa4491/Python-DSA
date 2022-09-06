from unittest import result
from LL import LinkedList

class Solution():
    
    def is_palindrome_helper(self,right):
        if right is None:
            return True
        result = self.is_palindrome_helper(right.next)
        if not result:
            return False
        elif self.left.data != right.data:
            return False
        else:
            self.left = self.left.next
            return True
        
    # use recursion
    def is_palindrome(self,l1):
        self.left = l1
        return self.is_palindrome_helper(l1)
    
    
li = LinkedList()
li.addLast(1)
li.addLast(2)
li.addLast(1)

ll = LinkedList()
for i in range(1,10):
    ll.addLast(i)

result = Solution().is_palindrome(ll.head)
print(result)