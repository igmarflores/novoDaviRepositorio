class Node:
    def _init_(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        root = Node(value)
    else:
        if value < root.value:
            if root.left is None:
                root.left = Node(value)
            else:
                insert(root.left, value)
        else:
            if root.right is None:
                root.right = Node(value)
            else:
                insert(root.right, value)

def buscaBinaria(root, value):
    if root is None or root.value == value:
        return root
    if root.value < value:
        return buscaBinaria(root.right, value)
    return buscaBinaria(root.left, value)

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.value, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=' ')