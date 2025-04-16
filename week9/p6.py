class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def survey_tree(root):
    if root is None:
        return []
    left = survey_tree(root.left)
    right = survey_tree(root.right)
    current = [root.val]

    return left + right + current

magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

print(survey_tree(magnolia))

# ["Leaf1", "Node1", "Leaf2", "Leaf3", "Node2", "Root"]