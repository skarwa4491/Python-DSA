from tkinter.messagebox import NO
from LL import LinkedList

class Solution():
    def fold_helper(self,ll,floor):
        if(ll is None):
            return
        self.fold_helper(ll.next,floor+1)
        if floor > self.size//2:
            current = self.left.next
            self.left.next = ll
            ll.next = current
            self.left = current
        elif floor == self.size//2:
            self.ll.tail = ll
            self.ll.tail.next = None
            
        
    def fold(self,ll):
        self.ll = ll
        self.size = ll.size
        self.left = ll.head
        self.fold_helper(ll.head,0)


ll = LinkedList()
for i in range(1,10):
    ll.addLast(i)
ll.display()
Solution().fold(ll)
ll.display()