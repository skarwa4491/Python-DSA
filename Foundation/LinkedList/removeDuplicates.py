from pickletools import read_uint1
from LL import LinkedList


class Solution():

    def remove_duplicates(self, l1):
        sanitized = LinkedList()
        node = l1.head
        while l1.size > 0:
            first = l1.removeFirst()
            if(sanitized.size == 0 or sanitized.tail.data != first.data):
                sanitized.addLast(first.data)

        return sanitized


l1 = LinkedList()
for i in range(1, 10):
    l1.addLast(i)
    l1.addLast(i)

result = Solution().remove_duplicates(l1)
result.display()

