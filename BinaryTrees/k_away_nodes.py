
from construct import *

'''
    print k levels away from key
'''


def k_levels_away(root, key, k):

    def node_to_root_path(root, key):

        if root is None:
            return path

        if root.data == key:
            path.append(root)
            return

        node_to_root_path(root.left, key)
        if len(path) > 0:
            path.append(root)
            return

        node_to_root_path(root.right, key)
        if len(path) > 0:
            path.append(root)
            return

    def print_k_levels_down(root, k, blocker):
        if root is None or k < 0 or root == blocker:
            return
        if k == 0:
            ans.append(root.data)

        print_k_levels_down(root.left, k-1, blocker)
        print_k_levels_down(root.right, k-1, blocker)

    path = list()
    ans = list()
    node_to_root_path(root, key)
    i = 0
    while i < len(path) and i <= k:
        blocker = None if i == 0 else path[i-1]
        print_k_levels_down(path[i], k-i, blocker)
        i += 1
    print(ans)


btree = Binary_Tree()
root = btree.construct([50, 25, 12, None, None, 37, 30, None,
                        None, None, 75, 62, None, 70, None, None, 87, None, None])
k_levels_away(root, 37, 2)
