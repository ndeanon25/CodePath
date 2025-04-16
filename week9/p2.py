class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
  if not root:
     return 0
  
  left_val = root.left.val
  right_val = root.right.val

  if root.val == "+":
     return left_val + right_val
  elif root.val == "-":
     return left_val - right_val
  elif root.val == "*":
     return left_val * right_val
  elif root.val == "-":
     return left_val / right_val
  else:
     return 0

apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))
apple_tree = TreeNode("-", TreeNode(7), TreeNode(5))
print(calculate_yield(apple_tree))