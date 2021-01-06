"""
Implementation of the binary tree using python
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        # print('self.data', self.data, 'data', data)
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data, end=' ')
        if self.right:
            self.right.print_tree()

    # In-order traversal
    # Left -> Root -> Right
    def in_order_traversal(self, node):
        in_order_result = []
        if node:
            in_order_result = self.in_order_traversal(node.left)
            in_order_result.append(node.data)
            in_order_result = in_order_result + self.in_order_traversal(node.right)
        return in_order_result

    # Pre-order traversal
    # Root -> Left -> Right
    def pre_order_traversal(self, node):
        pre_order_result = []
        if node:
            pre_order_result.append(node.data)
            pre_order_result += self.pre_order_traversal(node.left)
            pre_order_result += self.pre_order_traversal(node.right)
        return pre_order_result

    # Post-order-traversal
    # Left -> Right -> Root
    def post_order_result(self, node):
        post_order_result = []
        if node:
            post_order_result += self.post_order_result(node.left)
            post_order_result += self.post_order_result(node.right)
            post_order_result.append(node.data)
        return post_order_result



class Tree:
    def __init__(self, root: Node):
        self.root = root
        self.visited = []
        self.exhausted = []

    def get_next(self, node: Node):
        data = None
        if node not in self.visited and node not in self.exhausted:
            data = node.data
            self.visited.append(node)
        else:
            if node.left and node.left not in self.visited and node.left not in self.exhausted:
                data = node.left.data
                self.root = node.left
                self.visited.append(node.left)
            elif node.right and node.right not in self.visited and node.right not in self.exhausted:
                data = node.right.data
                self.root = node.right
                self.visited.append(node.right)
        return data

    def next(self):
        data = None

        if self.root not in self.visited:
            data = self.get_next(self.root)
        else:
            if self.root.left is not None:
                self.root = self.root.left
                data = self.get_next(self.root)
            elif self.root.right is not None:
                self.root = self.root.right
                data = self.get_next(self.root)

        while not data and self.visited:
            self.exhausted.append(self.root)
            self.visited.pop()
            if not self.visited:
                return data
            self.root = self.visited[-1]
            data = self.get_next(self.root)

        return data


root = Node(10)
root.insert(8)
root.insert(2)
root.insert(5)
root.insert(1)
root.insert(9)
root.insert(3)
root.insert(6)
root.insert(4)
root.insert(7)
root.print_tree()
print()
print(root.in_order_traversal(root))
print(root.pre_order_traversal(root))
print(root.post_order_result(root))
tree = Tree(root)

next_node = tree.next()
while next_node:
    print(next_node, ' ')
    next_node = tree.next()
