class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class Solution:
    def is_unival_tree(self, root: TreeNode) -> bool:
        nodes = []
        self.traverse_tree(node=root, nodes=nodes)
        return len(nodes) == 1

    def traverse_tree(self, node: TreeNode, nodes: []):
        if node:
            if node.val not in nodes:
                nodes.append(node.val)
            self.traverse_tree(node.left, nodes)
            self.traverse_tree(node.right, nodes)


root = TreeNode(1)
two = TreeNode(1)
three = TreeNode(2)
four = TreeNode(1)
five = TreeNode(1)
six = TreeNode(1)

root.left = two
root.right = five
two.left = three
two.right = four
five.right = six

solution = Solution()
print(solution.is_unival_tree(root=root))
