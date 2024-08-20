class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.data)

class Queue:
    def __init__(self, items=None, maxSize=None) -> None:
        self.items = items if items else []
        self.maxSize = maxSize

    def __str__(self) -> str:
        return str(self.items)
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []
    
    def isFull(self):
        return self.maxSize is not None and self.size() >= self.maxSize
    
    def enQueue(self, i):
        self.items.append(i)
    
    def deQueue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return None

class BST:
    def __init__(self, root=None) -> None:
        self.root = root
        self.q = Queue()
        
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return
        current = self.root
        while True:
            if data < current.data:
                if not current.left:
                    current.left = Node(data)
                    return
                current = current.left
            else:
                if not current.right:
                    current.right = Node(data)
                    return
                current = current.right
                
    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print('     ' * level, node)
            self.print_tree(node.left, level + 1)
    
    def print_pre_order(self, node):
        if not node:
            return
        print(node, end=' ')
        self.print_pre_order(node.left)
        self.print_pre_order(node.right)
        
    def print_in_order(self, node):
        if not node:
            return
        self.print_in_order(node.left)
        print(node, end=' ')
        self.print_in_order(node.right)
        
    def print_post_order(self, node):
        if not node:
            return
        self.print_post_order(node.left)
        self.print_post_order(node.right)
        print(node, end=' ')
    
    def print_breadth(self, node):
        if not node:
            return
        self.q.enQueue(node)
        while not self.q.isEmpty():
            n = self.q.deQueue()
            print(n, end=' ')
            if n.left:
                self.q.enQueue(n.left)
            if n.right:
                self.q.enQueue(n.right)
            
# Example usage
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i, item in enumerate(inp):
    if i == 0:
        T.insert(item)  # Insert the root node
    else:
        T.insert(item)

print('Preorder : ', end='')
T.print_pre_order(T.root)
print()

print('Inorder : ', end='')
T.print_in_order(T.root)
print()

print('Postorder : ', end='')
T.print_post_order(T.root)
print()

print('Breadth : ', end='')
T.print_breadth(T.root)
print()
