from unittest import result
from LL import LinkedList,Node


class Solution():
    def findMid(self, head, tail):
        slow = head
        fast = head
        while(fast != tail and fast.next != tail):
            fast = fast.next.next
            slow = slow.next
        return slow

    def MergeSort(self, head, tail):
        if head == tail:
            result = LinkedList()
            result.addLast(head.data)
            return result
        
        mid = self.findMid(head,tail)
        fh = self.MergeSort(head, mid)
        sh = self.MergeSort(mid.next, tail)
        final = self.merge(fh.head, sh.head)
        return final

    def merge(self, l1, l2):
        result = LinkedList()
        first = l1
        second = l2

        while(first and second):
            if first.data < second.data:
                result.addLast(first.data)
                first = first.next
            else:
                result.addLast(second.data)
                second = second.next

        while(first):
            result.addLast(first.data)
            first = first.next
        while(second):
            result.addLast(second.data)
            second = second.next

        return result


l1 = LinkedList()
l2 = LinkedList()
for i in range(2, 11, 2):
    l1.addLast(i)

for i in range(1, 11, 2):
    l1.addLast(i)

result = Solution().MergeSort(l1.head,l1.tail)
result.display()