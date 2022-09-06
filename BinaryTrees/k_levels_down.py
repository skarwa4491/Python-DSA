from construct import *


def print_k_levels_down(root, k):
    if root is None or k < 0:
        return
    if k == 0:
        print(root.data)

    print_k_levels_down(root.left, k-1)
    print_k_levels_down(root.right, k-1)


btree = Binary_Tree()
root = btree.construct([20, 25, 12, None, None, 37, 30, None,
                        None, None, 75, 62, None, 70, None, None, 87, None, None])
print_k_levels_down(root,1)