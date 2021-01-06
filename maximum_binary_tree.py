"""
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    /
     2  0
       \
        1
Note:
The size of the given array will be in the range [1,1000].

To solve this problem is like create a node every step, the value will be the max value of the array argument.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: [int]) -> TreeNode:
        root = self.create_sub_tree(nums)
        return root

    def create_sub_tree(self, nums: [int]):
        if not nums:
            return

        max_num = max(nums)
        root = TreeNode(max_num)

        left_nums = nums[:nums.index(max_num):]
        right_nums = nums[nums.index(max_num) + 1:]

        if left_nums:
            root.left = self.create_sub_tree(left_nums)
        if right_nums:
            root.right = self.create_sub_tree(right_nums)

        return root

    def print_tree(self, node: TreeNode):
        print(node.val, end=' ')
        if node.left:
            self.print_tree(node.left)
        if node.right:
            self.print_tree(node.right)


solution = Solution()
tree = solution.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
solution.print_tree(tree)
