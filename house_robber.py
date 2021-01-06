# The approach using even and odds doesn't work cause the robber can visit another houses
# class Solution:
#     def rob(self, nums: [int]) -> int:
#         even, odd = 0, 0
#         index_even, index_odd = 0, 1
#         while index_even <= len(nums)-1:
#             even += nums[index_even]
#             index_even += 2
#
#         while index_odd <= len(nums)-1:
#             odd += nums[index_odd]
#             index_odd += 2
#         return max(even, odd)

# DP to solve this? yeah like the coin problem but without constrains, it's a maximum situation


class Solution:
    def rob(self, nums: [int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        possible_amount = [0] * len(nums)
        possible_amount[0] = nums[0]
        possible_amount[1] = max(nums[0], nums[1])

        for index in range(2, len(nums)):
            possible_amount[index] = max(nums[index] + possible_amount[index-2], possible_amount[index-1])

        return possible_amount[-1]


solution = Solution()
print(solution.rob([2,1,1,2]))
