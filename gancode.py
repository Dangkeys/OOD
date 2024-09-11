class AVLTree:

    class AVLNode:

        def __init__(self, data, left = None, right = None):

            self.data = data

            self.left = None if left is None else left

            self.right = None if right is None else right

            self.height = self.setHeight()

        

        def __str__(self):

            return str(self.data)

        

        def setHeight(self):

                a = self.getHeight(self.left)

                b = self.getHeight(self.right)

                self.height = 1 + max(a,b)

                return self.height

            

        def getHeight(self, node):

            return -1 if node == None else node.height

            

        def balanceValue(self):      
            
            return self.getHeight(self.right) - self.getHeight(self.left)

    

    def __init__(self, root = None):

        self.root = None if root is None else root

    

    def add(self, data):
        self.root = AVLTree._add(self.root,int(data))

    def _add(root, data):
        if not root:
            return AVLTree.AVLNode(data)
        if data < root.data:
            root.left = AVLTree._add(root.left, data)
        else:
            root.right = AVLTree._add(root.right, data)
        root.setHeight()
        return AVLTree._rebalance(root)
    
        

    def rotateLeftChild(node: AVLNode):
        newRoot = node.left
        node.left = newRoot.right
        newRoot.right = node
        node.setHeight()
        newRoot.setHeight()
        return newRoot

    def rotateRightChild(node: AVLNode):
        newRoot = node.right
        node.right = newRoot.left
        newRoot.left = node
        node.setHeight()
        newRoot.setHeight()
        return newRoot


    def postOrder(self, node = None):
        if node == None:
            node = self.root
        if node.left:
            self.postOrder(node.left)
        if node.right:
            self.postOrder(node.right)
        print(node.data, end=" ")


    def printTree(self):

        AVLTree._printTree(self.root)

        print()

    

    def _printTree(node , level=0):

        if not node is None:

            AVLTree._printTree(node.right, level + 1)

            print('     ' * level, node.data)

            AVLTree._printTree(node.left, level + 1)

    def _rebalance(node: AVLNode):
        balance = node.balanceValue()
        if balance == -2:
            if not isinstance(node.right,AVLTree.AVLNode):
                return 'Error'
            if node.right.balanceValue() == 1:
                node.right = AVLTree.rotateLeftChild(node.right)
            node = AVLTree.rotateRightChild(node)
        elif balance == 2:
            if not isinstance(node.left, AVLTree.AVLNode):
                return 'Error'
            if node.left.balanceValue() == -1:
                node.left = AVLTree.rotateRightChild(node.left)
            node = AVLTree.rotateLeftChild(node)
        return node
                
avl1 = AVLTree()

inp = input('Enter Input : ').split(',')

for i in inp:
    if i[:2] == "AD":
        avl1.add(i[3:])
    elif i[:2] == "PR":
        avl1.printTree()
    elif i[:2] == "PO":
        print("AVLTree post-order : ", end="")
        avl1.postOrder()
        print()