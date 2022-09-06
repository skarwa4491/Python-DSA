from construct import *


def level_order_traversal(root):

    queue = [root]
    while len(queue) > 0:
        count = len(queue)
        for i in range(count):
            node = queue.pop(0)
            print(node.data, end="\t")
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        print()


btree = Binary_Tree()
root = btree.construct([20, 25, 12, None, None, 37, 30, None,
                        None, None, 75, 62, None, 70, None, None, 87, None, None])

level_order_traversal(root)
