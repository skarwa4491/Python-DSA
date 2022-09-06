from construct import *

# node to root path if key exist
def node_to_root_path(root, key, ans):
    if root is None:
        return ans

    if root.data == key:
        ans.append(root.data)
        return True

    left_result = node_to_root_path(root.left, key, ans)
    if left_result:
        ans.append(root.data)
        return True
    right_result = node_to_root_path(root.right, key, ans)
    if right_result:
        ans.append(root.data)
        return True
    
    return False


btree = Binary_Tree()
root = btree.construct([20, 25, 12, None, None, 37, 30, None,
                        None, None, 75, 62, None, 70, None, None, 87, None, None])
ans = list()
print(node_to_root_path(root, 87, ans))
print(ans[::-1])
