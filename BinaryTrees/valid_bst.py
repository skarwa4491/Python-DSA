# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys

class Solution:
    def isValidBST(self, root):
        
        def helper(root, _min , _max):
            if root is None:
                return True
            
            if root.val < _min or root.val > _max:
                return False
            
            left_result = helper(root.left,_min,root.val)
            right_result = helper(root.right,root.val,_max)
            
            return left_result and right_result
        
        return helper(root,sys.max_size, -sys.max_size)