from construct import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        remove all leaf nodes with specified target , if leaf nodes are
        removed and parent have same value , now parent becomes the lead node
        hence remove parent as well
    '''
    def removeLeafNodes(self, root, target):
        
        if root is None:
            return None
        
        if root.left is None and root.right is None and root.val==target:
            return None
        
        root.left = self.removeLeafNodes(root.left,target)
        root.right = self.removeLeafNodes(root.right,target)
        
        if root.left is None and root.right is None and root.val==target:
            return None
        
        return root

btree = Binary_Tree()
root = btree.construct([20, 25, 12, None, None, 37, 30, None,
                        None, None, 75, 62, None, 70, None, None, 87, None, None])