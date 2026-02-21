# Node class
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    # Get height
    def get_height(self, root):
        if not root:
            return 0
        return root.height


    # Get balance factor
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)


    # Right Rotation
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x


    # Left Rotation
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y


    # Insert
    def insert(self, root, key):

        # Normal BST insert
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Update height
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        # Get balance factor
        balance = self.get_balance(root)

        # LL Rotation
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # RR Rotation
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # LR Rotation
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL Rotation
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root


    # Inorder traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)


# Driver Program
tree = AVLTree()
root = None

values = [10, 20, 30, 40, 50, 25]

for v in values:
    root = tree.insert(root, v)

print("Inorder Traversal of Balanced AVL Tree:")
tree.inorder(root)