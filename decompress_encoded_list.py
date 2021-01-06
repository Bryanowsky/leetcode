class Solution:
    def decompress_list(self, nums: [int]) -> [int]:
        decompressed_nums = []
        index_freq, index_val = 0, 1
        while index_val < len(nums):
            decompressed_nums.extend([nums[index_val]] * nums[index_freq])
            index_freq += 2
            index_val += 2
        return decompressed_nums


solution = Solution()
print(solution.decompress_list([1, 2, 3, 4]))
