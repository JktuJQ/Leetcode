class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def symmetry_check(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        return left.val == right.val and\
            Solution.symmetry_check(left.left, right.right) and\
            Solution.symmetry_check(left.right, right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return Solution.symmetry_check(root.left, root.right)
