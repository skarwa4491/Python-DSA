from inspect import stack


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


class Pair:
    def __init__(self, node, state) -> None:
        # 1 -> attach to left
        # 2 --> attach to right
        # 3 --> pop from stack

        self.node = node
        self.state = state


class Binary_Tree():

    def contruct(self, list):
        root = Node(list[0], None, None)
        stack = []
        stack.append(Pair(root, 1))
        idx = 0
        while(len(stack) > 0):
            top = stack[-1]
            if(top.state == 1):
                # attach to left
                idx += 1
                if(list[idx] is not None):
                    top.node.left = Node(list[idx], None, None)
                    stack.append(Pair(top.node.left, 1))
                else:
                    top.node.left=None
                top.state += 1
                
            elif(top.state == 2):
                # attach to right
                idx+=1
                if(list[idx] is not None):
                    top.node.right = Node(list[idx], None, None)
                    stack.append(Pair(top.node.right, 1))
                else:
                    top.node.right=None
                top.state += 1
            else:
                stack.pop()
        return root
    
    def display(self,root):
        if(root is None):
            return
        display = ""
        display += "." if (root.left is None) else str(root.left.data)
        display += "<-- " + str(root.data) +" -->"
        display += "." if (root.right is None) else str(root.right.data)
        print(display)
        self.display(root.left)
        self.display(root.right)

btree = Binary_Tree()
root = btree.contruct([20, 25, 12, None, None, 37, 30,None, None, None, 75, 62, None, 70, None, None, 87, None, None])
btree.display(root)
