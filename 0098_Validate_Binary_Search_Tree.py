class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bst_check(node, bounds) -> bool:
        if node is None:
            return True
        return bounds[0] < node.val < bounds[1] and\
            Solution.bst_check(node.left, (bounds[0], node.val)) and\
            Solution.bst_check(node.right, (node.val, bounds[1]))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return Solution.bst_check(root, (float("-inf"), float("+inf")))
