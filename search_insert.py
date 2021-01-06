class Solution:
    def search_insert(self, nums: [int], target: int) -> int:
        try:
            search_index = nums.index(target)
            return search_index
        except ValueError:
            search_index = 0

        if target < nums[0]:
            return 0
        elif target > nums[len(nums) - 1]:
            return len(nums)
        else:
            cutted_nums = nums[:]
            while not search_index:
                print(cutted_nums, len(cutted_nums), len(nums) // 2 - 1)
                if target > cutted_nums[len(cutted_nums) // 2 - 1]:
                    cutted_nums = cutted_nums[len(cutted_nums) // 2:]
                    print(cutted_nums)
                else:
                    cutted_nums = cutted_nums[:len(cutted_nums) // 2]
                    print(cutted_nums)
                if len(cutted_nums) == 1:
                    last_number = cutted_nums[0]
                    possible_index = nums.index(cutted_nums[0])
                    search_index = possible_index + 1 if target > last_number else possible_index
        return search_index


solution = Solution()
print(solution.search_insert([1], 1))
