from construct import *


is_balance = True
def solution(root):
    '''
        gap of left height and right_height should not be more then one
        strictly zero or one
    '''
    if root is None:
        return 0

    left_height = solution(root.left)
    right_height = solution(root.right)
    balance = abs(left_height - right_height)
    if balance > 1:
        global is_balance
        is_balance = False
    th = max(left_height ,right_height) + 1
    return th


btree = Binary_Tree()
root = btree.construct([50, 25, 12, None, None, None, 37, 30, None,
                       None, 51, None, None, 75, 62, 60, None, None, 70, None, None, None])
solution(root)
btree.display(root)
print(is_balance)
