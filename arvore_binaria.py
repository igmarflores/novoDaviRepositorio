from arvore_binaria import *

root = Node(50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

print("Inorder traversal:")
inorder_traversal(root)
print("\nPreorder traversal:")
preorder_traversal(root)
print("\nPostorder traversal:")
postorder_traversal(root)

result = search(root, 60)
if result is not None:
    print("\nFound node with value:", result.value)
else:
    print("\nNode not found")