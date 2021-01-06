class Solution:
    def num_islands(self, grid: [[str]]) -> int:
        islands = 0

        # implementing the Depth First Search
        def deep_first_search(row_, col_):
            print('Point to apply DFS row:', row_, 'col:', col_)
            grid[row_][col_] = '-1'

            # check up
            if row_-1 >= 0 and grid[row_-1][col_] == '1':
                deep_first_search(row_-1, col_)

            # check right
            if col_+1 < len(grid[0]) and grid[row_][col_+1] == '1':
                deep_first_search(row_, col_+1)

            # check down
            if row_+1 < len(grid) and grid[row_+1][col_] == '1':
                deep_first_search(row_+1, col_)

            # check left
            if col_-1 >= 0 and grid[row_][col_-1] == '1':
                deep_first_search(row_, col_-1)

            # Simplified
            # for x, y in [(row_, col_+1), (row_-1, col_),  (row_, col_-1), (row_+1, col_)]:
            #     print(x, y)
            #     if grid[x][y] == '1' and x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid):
            #         deep_first_search(x, y)

        for row_index in range(len(grid)):
            for col_index in range(len(grid[0])):
                if grid[row_index][col_index] == '1':
                    islands += 1
                    deep_first_search(row_index, col_index)

        return islands


solution = Solution()
print(solution.num_islands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))

# [
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"]
# ]
