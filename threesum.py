class Solution:
    def get_numbers_combinations(self, nums: [], length: int) -> []:
        if length == 0:
            return [[]]
        combo = []
        for i in range(0, len(nums)):
            item = nums[i]
            rem_nums = nums[i + 1:]
            for combination in self.get_numbers_combinations(nums=rem_nums, length=length - 1):
                combo.append([item] + combination)
        return combo


solution = Solution()
solutions = []
nums = [0,3,0,1,1,-1,-5,-5,3,-3,-3,0]
combinations = solution.get_numbers_combinations(nums=nums, length=3)
for combination in combinations:
    insert_combination = True
    if sum(combination) == 0:
        for solution in solutions:
            solution_drop = solution[:]
            find_all = 0
            for digit in combination:
                if digit in solution_drop:
                    solution_drop.remove(digit)
                    find_all += 1
                if find_all == 3:
                    insert_combination = False
                    break
        if insert_combination:
            solutions.insert(0, combination)
print(solutions)


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         results = []
#         sort_results = []
#         combinations = self.get_numbers_combinations(nums=nums, r=3)
#         for combination in combinations:
#             sort_list = combination[:]
#             sort_list.sort()
#             if sum(combination) == 0 and sort_list not in sort_results:
#                 sort_results.append(sort_list)
#                 results.insert(0, combination)
#         return results
#
#     def get_numbers_combinations(self, nums: [], r: int) -> []:
#         pool = tuple(nums)
#         n = len(pool)
#         if r > n:
#             return
#         indices = list(range(r))
#         yield list(pool[i] for i in indices)
#         while True:
#             for i in reversed(range(r)):
#                 if indices[i] != i + n - r:
#                     break
#             else:
#                 return
#             indices[i] += 1
#             for j in range(i + 1, r):
#                 indices[j] = indices[j - 1] + 1
#             yield list(pool[i] for i in indices)


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         results = []
#         sort_results = []
#         combinations = self.get_numbers_combinations(nums=nums, length=3)
#         for combination in combinations:
#             sort_list = combination[:]
#             sort_list.sort()
#             if sum(combination) == 0 and sort_list not in sort_results:
#                 sort_results.append(sort_list)
#                 results.insert(0, combination)
#         return results
#
#     def get_numbers_combinations(self, nums: [], length: int) -> []:
#         if length == 0:
#             return [[]]
#         combo = []
#         for i in range(0, len(nums)):
#             item = nums[i]
#             rem_nums = nums[i + 1:]
#             for combination in self.get_numbers_combinations(nums=rem_nums, length=length - 1):
#                 combo.append([item] + combination)
#         return combo