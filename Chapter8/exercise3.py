class AVLNode:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right
        self.height = self.set_height()

    def __str__(self) -> str:
        return str(self.data)

    def set_height(self):
        left = self.get_height(self.left)
        right = self.get_height(self.right)
        self.height = max(left, right) + 1
        return self.height

    def get_height(self, node):
        return -1 if not node else node.height

    def balance_value(self):
        return self.get_height(self.left) - self.get_height(self.right)


class AVLTree:
    def __init__(self, root=None) -> None:
        self.root = root

    def insert(self, data):
        self.root = self._add(self.root, data)

    def _add(self, node, data):
        if node is None:
            return AVLNode(data)

        if data < node.data:
            node.left = self._add(node.left, data)
        else:
            node.right = self._add(node.right, data)

        # Update the height of the node
        node.set_height()

        # Rebalance the node
        node = self._rebalance(node)

        return node

    def rotate_left_child(self, node: AVLNode):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        node.set_height()
        new_root.set_height()
        return new_root

    def rotate_right_child(self, node: AVLNode):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        node.set_height()
        new_root.set_height()
        return new_root

    def _rebalance(self, node):
        balance_value = node.balance_value()

        if balance_value > 1: 
            if node.left.balance_value() < 0:
                print("Right Left Rotation")
                
                node.left = self.rotate_right_child(node.left)
            else:
                print("Right Right Rotation")
                
            node = self.rotate_left_child(node)

        elif balance_value < -1:
            if node.right.balance_value() > 0:
                print("Left Right Rotation")
                node.right = self.rotate_left_child(node.right)
            else:
                print("Left Left Rotation")
            node = self.rotate_right_child(node)

        return node

    def postOrder(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postOrder(node.left)
        if node.right:
            self.postOrder(node.right)
        print(node.data, end=" ")

def printTree90(node, level=0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

# Example of usage:
myTree = AVLTree()

print(" *** AVL Tree Insert Element ***")
data = input("Enter Input : ").split()
for e in data:
    print("insert :", e)
    myTree.insert(int(e))  # Convert input to integer
    printTree90(myTree.root)
    print("====================")
