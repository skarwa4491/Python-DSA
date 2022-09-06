from LL import LinkedList


class Solution():

    def reverseGroups(self, l1, k):
        prev = None
        
        while l1.size > 0:
            current = LinkedList()
            if l1.size >= k:
                i = 0
                while i < k:
                    val = l1.removeFirst().data
                    current.addFirst(val)
                    i+=1
            else:
                s = l1.size
                i=0
                while i<s:
                    val = l1.removeFirst().data
                    current.addLast(val)
                    i+=1
                    
            if prev is None:
                    prev=current
            else:
                prev.tail.next = current.head
                prev.tail=current.tail
                prev.size += current.size
        l1.head = prev.head
        l1.tail = prev.tail
        l1.size = prev.size

l1 = LinkedList()
for i in range(1, 13):
    l1.addLast(i)

Solution().reverseGroups(l1,3)
l1.display()
