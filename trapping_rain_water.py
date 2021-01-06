class Solution:
    def trap(self, height: [int]) -> int:
        if not height:
            return 0

        max_l = [height[0]] * len(height)
        max_r = [height[-1]] * len(height)
        for i in range(1, len(height)):
            print('max_l', max_l[i - 1], 'height', height[i])
            max_l[i] = max(max_l[i - 1], height[i])
        for j in range(len(height) - 2, -1, -1):
            max_r[j] = max(max_r[j + 1], height[j])
        water = []
        for i in range(len(height)):
            water.append((min(max_l[i], max_r[i])) - height[i])
        print(max_r)
        print(max_l)
        print(height)
        print(water)
        return sum(water)
    # def trap(self, height: [int]) -> int:
    #     index_1, index_2 = 0, 1
    #     valley = []
    #     collected_water = 0
    #     while index_1 <= len(height) - 1 and index_2 <= len(height) - 1:
    #         # print(index_1, index_2)
    #         if height[index_1] <= height[index_2]:
    #             # print('height_1', height[index_1], 'height_2', height[index_2], valley)
    #             if valley:
    #                 h_ = min(height[index_1], height[index_2])
    #                 for item in valley:
    #                     collected_water += (h_ - item)
    #                 valley = []
    #             index_1 = index_2
    #             # print('collected', collected_water)
    #         elif index_2 == len(height) - 1 and valley:
    #             if height[index_2] > max(valley):
    #                 previous_collected = collected_water
    #                 h_ = min(height[index_1], height[index_2])
    #                 for item in valley:
    #                     if item < h_:
    #                         collected_water += (h_ - item)
    #                 if collected_water != previous_collected:
    #                     index_1 = index_2
    #                 # print('valley', valley, 'h', h_, 'collected', collected_water)
    #             else:
    #                 for i in range(len(valley)):
    #                     if valley[i] >= height[index_2] and valley[i] == max(valley):
    #                         index_2 = index_1 + i + 1
    #                         h_ = min(height[index_1], height[index_2])
    #                         # print(valley[:i])
    #                         for item in valley[:i]:
    #                             collected_water += (h_ - item)
    #                         break
    #                 # print(height[index_1], height[index_2], 'collected', collected_water)
    #                 index_1 = index_2-1
    #
    #             index_1 += 1
    #             index_2 = index_1
    #             valley = []
    #         else:
    #             valley.append(height[index_2])
    #         index_2 += 1
    #
    #         # print('height', height[height_index], 'index_1', index_1, 'index_2', index_2, 'valley', valley)
    #
    #     return collected_water


solution = Solution()
# print(solution.trap([4,2,0,3,2,5]), 9)
# print(solution.trap([4,2,3]), 1)
# print(solution.trap([4,9,4,5,3,2]), 1)
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6)
# print(solution.trap([9,2,9,3,2,2,1,4,8]), 35)
