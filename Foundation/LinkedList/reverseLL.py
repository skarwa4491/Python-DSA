from LL import LinkedList, Node


class Solution():

    def _getNodeAt(self, head, idx):
        i = 0
        node = head
        while i < idx:
            node = node.next
            i += 1
        return node

    def reverse_ll_data_iterative(self, ll):
        low = 0
        high = ll.size-1
        while low < high:
            low_node = self._getNodeAt(ll.head, low)
            high_node = self._getNodeAt(ll.head, high)
            temp = low_node.data
            low_node.data = high_node.data
            high_node.data = temp
            low += 1
            high -= 1

    def reverse_ll_pointer_iterative(self, ll):
        prev = None
        current = ll.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        temp = ll.head
        ll.head = ll.tail
        ll.tail = temp

    def print_reverse_ll_data_recursive(self, li):
        # print only
        if(li == None):
            return
        self.reverse_ll_data_recursive(li.next)
        print(li.data, end="\t")

    def reverse_ll_pointer_recursive(self, ll):
        self.reverse_ll_pointer_recursive_helper(ll.head, ll.tail)
        ll.head.next = None
        temp = ll.head
        ll.head = ll.tail
        ll.tail = temp
        print()

    def reverse_ll_pointer_recursive_helper(self, ll, tail):
        if ll is None:
            return
        self.reverse_ll_pointer_recursive_helper(ll.next, tail)
        if ll == tail:
            pass
        else:
            ll.next.next = ll


ll = LinkedList()
for i in range(1, 5):
    ll.addLast(i)
ll.display()
print('\n')
Solution().reverse_ll_pointer_recursive(ll)
ll.display()
