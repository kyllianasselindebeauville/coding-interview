# Tree

class BinaryTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        return self.str_representation(self.root)

    def str_representation(self, node, indent=0):
        if node is None:
            return ''

        return str(
            self.str_representation(node.right, indent + 1) +
            indent * '\t' + str(node) + '\n' +
            self.str_representation(node.left, indent + 1)
        )
