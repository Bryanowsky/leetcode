class Solution:
    def can_place_flower(self, flowerbed: [int], n: int) -> bool:
        if flowerbed[0] == 0 and len(flowerbed) == 1:
            return True

        for index in range(len(flowerbed)):
            print(flowerbed[index])

            if flowerbed[index] == 0:
                if index == 0 and flowerbed[index + 1] == 0:
                    n -= 1
                    print('possible spot at', index)
                    flowerbed[index] = 1
                elif index == len(flowerbed) - 1 and flowerbed[index - 1] == 0:
                    n -= 1
                    print('possible spot at', index)
                    flowerbed[index] = 1
                elif flowerbed[index - 1] == 0 and flowerbed[index + 1] == 0:
                    n -= 1
                    print('possible spot at', index)
                    flowerbed[index] = 1

        if n < 1:
            return True
        return False


solution = Solution()
print(solution.can_place_flower([0, 0, 1, 0, 1], 1))
