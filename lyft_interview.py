"""
Question: Given a binary tree. Write a class where the object of the class holds a binary tree and has a function
called next() which returns the next node in preorder. For example:
                2
              /  \
             5    6
            /  \   \
           10  3    11
          /
        22
next() -> 2
next() -> 5
next() -> 10
And so on, the rest of the calls will return 3, 6, 11
Once the tree is exhausted the subsequent calls will return null.

In this problem I could use deep first search, the difference between the problems that I solved before is
that the recursive approach is not possible cause we want to iterate step by step.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# I need to go deeper in every node, so I could exhaust first.
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


## Creating manually the tree
two = Node(2)
six = Node(6)
eleven = Node(11)
ten = Node(10)
three = Node(3)
five = Node(5)
twenty_one = Node(21)
five.left = ten
five.right = three
ten.left = twenty_one
two.left = five
two.right = six
six.right = eleven
tree = Tree(two)
print(tree.next())
print(tree.next())
print(tree.next())
print(tree.next())
print(tree.next())
print(tree.next())
print(tree.next())
print(tree.next())
print(tree.next())
print(tree.next())
