class Node:
    def __init__(self,data,left = None, right = None) -> None:
        self.data = data
        self.left =left
        self.right = right
    def __str__(self) -> str:
        return str(self.data)
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
        if not node:
            return
        self.print_tree(node.right, level+1)
        print('     '*level,node)
        self.print_tree(node.left, level+1)
    def print_tree_k(self,node,k ,level = 0):
        if not node:
            return
        # formatted_node = node
        if node.data > k: node.data *= 3
        self.print_tree_k(node.right, k,level+1)
        print('     '*level,node)
        self.print_tree_k(node.left, k,level+1)
T = BST()
lst,k = input('Enter Input : ').split('/')
inp = [int(x) for x in lst.split()]
k = int(k)
for i in inp:
    T.insert(i)
T.print_tree(T.root)
print('--------------------------------------------------')
T.print_tree_k(T.root,k)