# class Trie:
#     def __init__(self):
#         self.head = {}
#         self.end_node = False
#
#     def add(self, word):
#         current = Trie()
#
#         for char in word:
#             if char not in current.head:
#                 current.head[char] = {}
#             current.head[char] = char
#         current.end_node = '*'
#
#     def search(self, word):
#         current = Trie()
#
#         for char in word:
#             if char not in current.head:
#                 return False
#             current = current.head[char]
#
#         if current.head == '*':
#             return True
#         else:
#             return False


class Trie:
    head = {}

    def add(self, word):
        current = self.head
        print('adding word', word, 'to', current)
        for char in word:
            print('char', char, 'current', current.keys(), current.items())
            if char not in current:
                current[char] = {}
            current = current[char]
        current['*'] = True

    def search(self, word):
        current = self.head

        for char in word:
            if char not in current:
                return False
            current = current[char]

        if '*' in current:
            return True
        else:
            return False


trie = Trie()
trie.add('hello')
trie.add('hell')
trie.add('help')
print(trie.head)
# trie.add('hola')
# trie.add('papaya')
# trie.add('pelon')
# trie.add('pelonete')
print(trie.head.keys(), trie.head.items())
print(trie.search('hello'))

