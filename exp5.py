# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None


    # Insert
    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.data:
            root.left = self.insert(root.left, key)
        elif key > root.data:
            root.right = self.insert(root.right, key)

        return root


    # Search
    def search(self, root, key):
        if root is None:
            return False

        if root.data == key:
            return True
        elif key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)


    # Find minimum value node
    def min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current


    # Delete
    def delete(self, root, key):
        if root is None:
            return root

        if key < root.data:
            root.left = self.delete(root.left, key)

        elif key > root.data:
            root.right = self.delete(root.right, key)

        else:
            # Case 1: No child
            if root.left is None and root.right is None:
                return None

            # Case 2: One child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 3: Two children
            temp = self.min_value_node(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root


    # Inorder Traversal (LNR)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)


    # Preorder Traversal (NLR)
    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)


    # Postorder Traversal (LRN)
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


# Driver Program
tree = BST()

# Insert values
values = [50, 30, 70, 20, 40, 60, 80]
for v in values:
    tree.root = tree.insert(tree.root, v)

print("Inorder Traversal:")
tree.inorder(tree.root)

print("\nPreorder Traversal:")
tree.preorder(tree.root)

print("\nPostorder Traversal:")
tree.postorder(tree.root)

# Search
key = int(input("\nEnter element to search: "))
if tree.search(tree.root, key):
    print("Element found")
else:
    print("Element not found")

# Delete
del_key = int(input("Enter element to delete: "))
tree.root = tree.delete(tree.root, del_key)

print("Inorder after deletion:")
tree.inorder(tree.root)