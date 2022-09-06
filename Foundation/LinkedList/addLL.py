from LL import LinkedList


class Solution():

    def __init__(self, l1, l2) -> None:
        self.l1 = l1
        self.l2 = l2

    def add_ll_helper(self, l1, p1, l2, p2, result):
        if ((l1 is None) and (l2 is None)):
            return 0
        data = 0
        if p1 > p2:
            carry = self.add_ll_helper(l1.next, p1-1, l2, p2, result)
            data = l1.data + carry

        elif p2 > p1:
            self.add_ll_helper(l1, p1, l2.next, p2-1, result)
            data = l2.data + carry
        else:
            carry = self.add_ll_helper(l1.next, p1-1, l2.next, p2-1, result)
            data = l1.data + l2.data + carry

        if data > 9:
            carry = data // 10
            data = data % 10
        else:
            carry = 0
        result.addFirst(data)
        return carry

    def add_ll(self, l1, l2):
        result = LinkedList()
        carry = self.add_ll_helper(l1, self.l1.size, l2, self.l2.size, result)
        if carry:
            result.addFirst(carry)
        return result


l1 = LinkedList()
l1.addLast(8)
l1.addLast(8)
l2 = LinkedList()
l2.addLast(8)
l2.addLast(8)

result = Solution(l1, l2).add_ll(l1.head, l2.head)
result.display()
