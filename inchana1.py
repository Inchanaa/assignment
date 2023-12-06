class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    if not root:
        return None

    # If both nodes are smaller than the root, go left
    if p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left, p, q)

    # If both nodes are larger than the root, go right
    elif p.val > root.val and q.val > root.val:
        return lowestCommonAncestor(root.right, p, q)

    # If one node is smaller and the other is larger, or one of them is equal to the root
    # then the current root is the lowest common ancestor
    else:
        return root

# Example usage:
# Construct the BST from the example
root = TreeNode(6)
root.left = TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5)))
root.right = TreeNode(8, TreeNode(7), TreeNode(9))

# Create nodes for p and q
p = TreeNode(2)
q = TreeNode(8)

# Find the lowest common ancestor
result = lowestCommonAncestor(root, p, q)
print(result.val) 
