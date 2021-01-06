class Solution:
    def exist(self, board: [[str]], word: str) -> bool:

        # When you have a problem with a grid you could use a DFS
        def deep_first_search(row_index, column_index, word_, count, direction):
            # Check out boundaries
            if row_index < 0 or row_index >= len(board) or column_index < 0 or column_index >= len(board[0]):
                return False

            # if the board position is not equal to the word position
            if board[row_index][column_index] != word_[count]:
                return False

            print('Applying DFS to', board[row_index][column_index], 'at', row_index, column_index, 'count:', count,
                  'direction', direction)

            # The counter equals to the len of the word
            if len(word_) - 1 == count and word[count] == board[row_index][column_index]:
                print('Word was founded')
                return True

            actual_letter = board[row_index][column_index]
            board[row_index][column_index] = ''

            # Searching in all directions (up, right, down, left) if we did it one by one, we always did n calls
            # up = deep_first_search(row_index-1, column_index, word_, count+1, 'up')
            # right = deep_first_search(row_index, column_index+1, word_, count+1, 'right')
            # down = deep_first_search(row_index+1, column_index, word_, count+1, 'down')
            # left = deep_first_search(row_index, column_index-1, word_, count+1, 'left')
            # Or, if we found a letter no matter the direction the recursive call continue

            # This or can help if we find a previous solution and is no needed the other calls
            found = deep_first_search(row_index - 1, column_index, word_, count + 1, 'up') or \
                    deep_first_search(row_index, column_index + 1, word_, count + 1, 'right') or \
                    deep_first_search(row_index + 1, column_index, word_, count + 1, 'down') or \
                    deep_first_search(row_index, column_index - 1, word_, count + 1, 'left')

            board[row_index][column_index] = actual_letter

            return found

        for row in range(len(board)):
            for column in range(len(board[0])):
                print(board[row][column], end=' ')
                if board[row][column] == word[0] and deep_first_search(row, column, word, 0, 'init'):
                    return True
            print()
        return False


solution = Solution()
print(solution.exist([
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
], 'SEE'))
