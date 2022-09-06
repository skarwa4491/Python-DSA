from LL import LinkedList

class Solution():
    # get kth node from last of linkedList
    # no iteration,no recurssion , no use of size property
    def getKthNode(self,ll,k):
        if k==0:
            return ll.tail
        slow = ll.head
        fast = ll.head
        i=0
        while i<k:
            fast=fast.next
            i+=1
        while fast != ll.tail:
            slow= slow.next
            fast = fast.next
            
        return slow
    

ll = LinkedList()
for i in range(1, 5):
    ll.addLast(i)
ll.display()
print(Solution().getKthNode(ll,1).data)