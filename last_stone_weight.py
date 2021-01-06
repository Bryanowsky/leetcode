# We have a collection of rocks, each rock has a positive integer weight.
#
# Each turn, we choose any two rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:
#
# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the smallest possible weight of this stone (the weight is 0 if there are no stones left.)
#
#
#
# Example 1:
#
# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We can combine 2 and 4 to get 2 so the array converts to [2,7,1,8,1] then,
# we can combine 7 and 8 to get 1 so the array converts to [2,1,1,1] then,
# we can combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we can combine 1 and 1 to get 0 so the array converts to [1] then that's the optimal value.

# This solutions works only to comparing just the two heaviest every iteration
# class Solution:
#     def last_stone_weightII(self, stones: [int]) -> int:
#         while len(stones) > 1:
#             print(stones, end=' ')
#             y = max(stones)
#             stones.remove(y)
#             x = max(stones)
#             stones.remove(x)
#             print(x, y)
#             if x < y:
#                 y -= x
#                 stones.insert(0, y)
#         if stones:
#             return stones[0]
#         return 0

# The key of this problem is that we have n possible solutions what we want is which returns the minimum possible value,
# it's possible to use DP

class Solution:
    def last_stone_weightII(self, stones: [int]) -> int:
        n, target = len(stones), sum(stones)
        dp = [0 for i in range(target // 2 + 1)]
        print(dp)
        for i in stones:
            for j in range(target // 2, 0, -1):
                if j >= i:
                    dp[j] = max(dp[j], dp[j - i] + i)
        print(dp)
        print('target', target, 'other stuff', 2 * dp[target // 2])
        return target - 2 * dp[target // 2]


solution = Solution()
print(solution.last_stone_weightII([31,26,33,21,40]))
