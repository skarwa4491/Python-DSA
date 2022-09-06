class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


class Pair:
    def __init__(self, node, state) -> None:
        # 1 to attach left
        # 2 to attach right
        # 3 to pop
        self.node = node
        self.state = state


class Binary_Tree():

    def construct(self, arr):
        root = Node(arr[0])
        pair = Pair(root, 1)
        stack = list()
        stack.append(pair)
        idx = 0
        while len(stack) > 0:
            top = stack[-1]
            if top.state == 1:
                idx += 1
                if arr[idx] is not None:
                    node = Node(arr[idx])
                    top.node.left = node
                    pair = Pair(node, 1)
                    stack.append(pair)
                else:
                    top.node.left = None
                top.state += 1

            elif top.state == 2:
                idx += 1
                if arr[idx] is not None:
                    node = Node(arr[idx])
                    top.node.right = node
                    pair = Pair(node, 1)
                    stack.append(pair)
                else:
                    top.node.right = None
                top.state += 1
            else:
                stack.pop()
        return root

    def display(self, root):
        if(root is None):
            return
        display = ""
        display += "." if (root.left is None) else str(root.left.data)
        display += "<-- " + str(root.data) + " -->"
        display += "." if (root.right is None) else str(root.right.data)
        print(display)
        self.display(root.left)
        self.display(root.right)

