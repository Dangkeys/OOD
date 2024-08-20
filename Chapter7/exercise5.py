class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.data)
class BST:
    def __init__(self, root=None) -> None:
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
                
    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print('     ' * level, node)
            self.print_tree(node.left, level + 1)
    def checkpos(self,data):
        current = self.root
        while current:
            if data < current.data:
                if not current.left:
                    print("Not exist")
                    return 
                current = current.left
            elif data > current.data:
                if not current.right:
                    print("Not exist")
                    return 
                current = current.right
            else:
                if current == self.root:
                    print('Root')
                    return 
                elif not current.right and not current.left:
                    print("Leaf")
                    return
                else:
                    print("Inner")
                    return 
        
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i, item in enumerate(inp):
    if i != 0:
        T.insert(item)
T.print_tree(T.root)
T.checkpos(inp[0])
