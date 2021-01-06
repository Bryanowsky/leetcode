# Solution brute force, slicing it is ok but it is O(n) by every iteration
# class Solution:
#     def product_except_self(self, nums: [int]) -> [int]:
#         products = []
#         for i in range(len(nums)):
#             products.append(self.calculate_product(nums[:i]+nums[i+1:]))
#         return products
#
#     def calculate_product(self, sub_nums: [int]) -> int:
#         product = sub_nums.pop(0)
#         for num in sub_nums:
#             product = num * product
#         return product

# In this approach you will go to right and left to calculate the product, I need to avoid the first value in the go to
# right for and in the left to right what I need to avoid is the last value


class Solution:
    def product_except_self(self, nums: [int]) -> [int]:
        products = []
        current_product = 1
        for num in nums:
            products.append(current_product)
            current_product *= num

        current_product = 1 * nums[-1]
        for j in range(len(nums)-2, -1, -1):
            products[j] *= current_product
            current_product *= nums[j]
        return products


solution = Solution()
print(solution.product_except_self(nums=[1, 2, 3, 4]))
