class Node:
    def __init__(self, data, left = None, right = None) -> None:
        self.data = data
        self.left = left
        self.right =right
class BST:
    def __init__(self,root = None) -> None:
        self.root = root
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return data
        current = self.root
        while True:
            if data < current.data:
                if not current.left:
                    current.left = Node(data)
                    return data
                current = current.left
            else:
                if not current.right:
                    current.right = Node(data)
                    return data
                current = current.right
    def print_tree(self,node, level = 0):
        self.print_tree(node.right,level+1)
        print('     '*level,node)
        self.print_tree(node.left, level+1)
    def height(self, node):
        if not node:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1
    
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    T.insert(i)

print('Height of this tree is : ' + str(T.height(T.root)))
