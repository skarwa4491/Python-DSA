from construct import *


def size(root):
    if root is None:
        return 0
    size_left = size(root.left)
    size_right = size(root.right)

    return size_left + size_right + 1


def sum(root):
    
    if root is None:
        return 0
    
    sum_left = sum(root.left)
    sum_right = sum(root.right)
    
    return sum_left + sum_right + root.data


def maximum(root):
    if root is None:
        return 0
    
    max_left = maximum(root.left)
    max_right = maximum(root.right)
    
    return max(max_left,max_right,root.data)


def height(root):
    if root is None:
        return 0
    
    height_left = height(root.left)
    height_right = height(root.right)
    
    return max(height_left,height_right)+1


btree = Binary_Tree()
root = btree.construct([20, 25, 12, None, None, 37, 30, None,
                        None, None, 75, 62, None, 70, None, None, 87, None, None])

print(height(root))
