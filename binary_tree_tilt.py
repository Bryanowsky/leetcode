"""
Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the
sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:
Input:
         1
       /   \
      2     3
Output: 1
Explanation:
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1
Note:

The sum of node values in any subtree won't exceed the range of 32-bit integer.
All the tilt values won't exceed the range of 32-bit integer.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def findTilt(self, root: Node) -> int:
        if not root:
            return 0

        value = self.traverse(root)
        return value

    def traverse(self, root: Node) -> int:
        value = 0
        if root:
            left_ = self.findTilt(root.left)
            right_ = self.findTilt(root.right)
            value = abs(left_ - right_)
            print('value_abs', value)
            value = root.value + left_ + right_
            print('value_', value)
        return value


root = Node(1)
two = Node(2)
three = Node(3)
root.left = two
root.right = three

solution = Solution()
print(solution.findTilt(root))

