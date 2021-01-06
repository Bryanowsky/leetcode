# This problem is a little bit tricky cause what you need is just to think before instead of starting code or thinking
# into apply any fancy algorithm, so this requires to consider the constrains, at most two people at the boat.
# this solution try to match a couple of persons in one boat if not we just go to the next heaviest and the same
# lightest person, if they can go in the same boat, I can go with the next lightest.


class Solution:
    def num_rescue_boats(self, people: [int], limit: int) -> int:
        people.sort()
        light_ = 0
        heavy_ = len(people) - 1
        boats = 0

        while light_ <= heavy_:
            print(people[light_], people[heavy_])
            if people[light_] + people[heavy_] <= limit:
                light_ += 1
            heavy_ -= 1
            boats += 1

        return boats


solution = Solution()
print(solution.num_rescue_boats([3, 2, 2, 1], 3))
