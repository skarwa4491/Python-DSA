from LL import LinkedList

class Solution():
    def getMid(self,ll):
        slow = ll.head
        fast = ll.head
        while(fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow.data

ll = LinkedList()
for i in range(1,6):
    ll.addLast(i)

ll.display()
print(Solution().getMid(ll))