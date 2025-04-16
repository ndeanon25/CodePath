class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

    

root = TreeNode("Trunk")
root.left = TreeNode("Mcintosh")
root.right = TreeNode("Granny Smith")
root.left.left = TreeNode("Fuji")
root.left.right = TreeNode("Opal")
root.right.left = TreeNode("Crab")
root.right.right = TreeNode("Gala")
def print_tree(node):
    if node is not None:
        print(node.val)
        print_tree(node.left)
        print_tree(node.right)

print_tree(root)
#['Trunk', 'Mcintosh', 'Granny Smith', 'Fuji', 'Opal', 'Crab', 'Gala']