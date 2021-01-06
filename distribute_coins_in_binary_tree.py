class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


class Solution:
    def distribute_coins(self, root: TreeNode) -> int:
        visited, exhausted = [], []
        self.exhaust_node(root, visited, exhausted)


        return 1

    def exhaust_node(self, node: TreeNode, visited: [], exhausted: []):
        print('node', node.val)
        if node.val > 0:
            visited.append(node)
            if node.left:
                if node.left.val == 0:
                    print('moving coin')
                    node.val -= 1
                    node.left.val = 1
                    self.exhaust_node(node.left, visited, exhausted)

            if node.right:
                if node.right.val == 0:
                    print('moving coin')
                    node.val -= 1
                    node.right.val = 1
                    self.exhaust_node(node.right, visited, exhausted)

            if node.left is None and node.right is None:
                exhausted.append(node)
                visited.pop()
        else:
            if node.left and node.left.val > 0:
                self.exhaust_node(node.left, visited, exhausted)
            elif node.right and node.right.val > 0:
                self.exhaust_node(node.left, visited, exhausted)


        print('node', node.val, 'visited', visited, 'exhausted', exhausted)


root = TreeNode(3)
root.left = TreeNode(0)
root.right = TreeNode(0)

solution = Solution()
print(solution.distribute_coins(root))
