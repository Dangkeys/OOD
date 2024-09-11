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
        self.root = None

    def add(self, data):
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
        if not isinstance(new_root, AVLNode):
            return node
        node.left = new_root.right
        new_root.right = node
        node.set_height()
        new_root.set_height()
        return new_root

    def rotate_right_child(self, node: AVLNode):
        new_root = node.right
        if not isinstance(new_root, AVLNode):
            return node
        node.right = new_root.left
        new_root.left = node
        node.set_height()
        new_root.set_height()
        return new_root

    def print_tree(self):
        AVLTree._print_tree(self.root)
        print()

    @staticmethod
    def _print_tree(node, level=0):
        if not node:
            return
        AVLTree._print_tree(node.right, level + 1)
        print('     ' * level, node.data)
        AVLTree._print_tree(node.left, level + 1)

    def _rebalance(self, node):
        if not isinstance(node, AVLNode):
            return node
        balance_value = node.balance_value()
        if balance_value == 2:
            left = node.left
            if not isinstance(left, AVLNode):
                return node
            if left.balance_value() == -1:
                node.left = self.rotate_right_child(left)
            node = self.rotate_left_child(node)
        elif balance_value == -2:
            right = node.right
            if not isinstance(right, AVLNode):
                return node
            if right.balance_value() == 1:
                node.right = self.rotate_left_child(right)
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


# Example of usage:
avl1 = AVLTree()

inp = input('Enter Input : ').split(',')

for i in inp:
    if i[:2] == "AD":
        avl1.add(int(i[3:]))
    elif i[:2] == "PR":
        avl1.print_tree()
    elif i[:2] == "PO":
        print('AVLTree post-order : ', end="")
        avl1.postOrder()
        print()
