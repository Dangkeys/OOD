class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        # This will help you when debugging later.
        return f"Node({self.data})"

    def height(self):
        return (max(Node.height(self.left), Node.height(self.right)) + 1) if self else -1
    
    def balance(self):
        return Node.height(self.left) - Node.height(self.right) if self else 0

    def leftRotate(z):
        newRoot = z.left
        z.left = newRoot.right
        newRoot.right = z
        return newRoot

    def rightRotate(z):
        newRoot = z.right
        z.right = newRoot.left
        newRoot.left = z
        return newRoot
    
    def _rebalance(node):
        balance = node.balance()
        if balance == -2:
            if node.right.balance() == 1:
                node.right = Node.leftRotate(node.right)
            node = Node.rightRotate(node)
        elif balance == 2:
            if node.left.balance() == -1:
                node.left = Node.rightRotate(node.left)
            node = Node.leftRotate(node)
        return node

    def insert(root, data, direction, is_balance = True):
        if root is None:
            return Node(data)
        if not is_balance:
            if data < root.data:
                branch = "left"
            elif data > root.data:
                branch = "right"
            else:
                branch = direction
        else:
            branch = "left" if data < root.data else "right"
        root.__dict__[branch] = Node.insert(root.__dict__[branch], data, direction, is_balance)

        # Balance this tree
        if is_balance:
            return Node._rebalance(root)
        return root

    def inorder_traversal(self, root):
        # Helper function to perform in-order traversal and return a sorted list
        if root is None:
            return []
        return (
            self.inorder_traversal(root.left)
            + [root.data]
            + self.inorder_traversal(root.right)
        )
    
    def find_node(root, data):
        if root.data == data:
            return root
        if data < root.data:
            try:
                return Node.find_node(root.left, data)
            except:
                pass
        else:
            try:
                return Node.find_node(root.right, data)
            except:
                pass

    def find_node_and_replace(root, data, node):
        if root.data == data:
            return node
        if data < root.data:
            try:
                root.left = Node.find_node_and_replace(root.left, data, node)
            except:
                pass
        else:
            try:
                root.right = Node.find_node_and_replace(root.right, data, node)
            except:
                pass
        return root

    def _gen_display(self) -> 'tuple[list, int, int, int]':
        '''
        return
        - tree image: list[str]
        - left spacing: int
        - value width: int
        - right spacing: int
        '''
        if self is None:
            return [], 0, 0, 0
        left_tree, left_fill, left_width, left_branch = Node._gen_display(self.left)
        right_tree, right_fill, right_width, right_branch = Node._gen_display(self.right)
        data = str(self.data)
        if not left_tree and not right_tree:
            return [data], 0, len(data), 0
        add_left, add_right = int(bool(left_tree)), int(bool(right_tree))
        line = ((' '*(left_fill+left_width) + '/' + ' '*(left_branch)) * add_left +
                ' ' * len(data) +
                (' '*right_fill + '\\' + ' '*(right_width+right_branch)) * add_right)
        out = [' '*(left_fill+left_width+add_left) + '_'*left_branch + data +
                '_'*right_fill + ' '*(right_width+right_branch+add_right), line]
        if len(left_tree) > len(right_tree):
            right_tree.extend([' ' * (right_fill+right_width+right_branch)] * (len(left_tree) - len(right_tree)))
        elif len(left_tree) < len(right_tree):
            left_tree.extend([' ' * (left_fill+left_width+left_branch)] * (len(right_tree) - len(left_tree)))
        for l, r in zip(left_tree, right_tree):
            out.append(l + ' '*(len(data)+add_left+add_right) + r)
        return out, (left_fill+left_width+left_branch+add_left), len(data), (right_fill+right_width+right_branch+add_right)

rotate, direction, inp = input('Enter input: ').split(',')
rotate = int(rotate)
root = None

def rearrange_node(direction, node: Node):
    root = None
    if direction == "right":
        orders = node.inorder_traversal(node)
    else:
        orders = reversed(node.inorder_traversal(node))
    for i in orders:
        root = Node.insert(root, i,direction, False)
    return root

for i in map(int, inp.split()):
    root = Node.insert(root, i, direction)
tree_image = root._gen_display()
print("Before")
print(*tree_image[0], sep='\n')
print("-" * sum(tree_image[1:]))

founded_node = Node.find_node(root, rotate)
if founded_node is None:
    print(f"No {rotate} in this tree")
    exit()
node = rearrange_node(direction, founded_node)
root = Node.find_node_and_replace(root, rotate, node)
tree_image = root._gen_display()



print("After")
print(*tree_image[0], sep='\n')