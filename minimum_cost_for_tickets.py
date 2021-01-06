# In a country popular for train travel, you have planned some train travelling one year in advance.
# The days of the year that you will travel is given as an array days.
# Each day is an integer from 1 to 365.
#
# Train tickets are sold in 3 different ways:
#
# a 1-day pass is sold for costs[0] dollars;
# a 7-day pass is sold for costs[1] dollars;
# a 30-day pass is sold for costs[2] dollars.
#
# The passes allow that many days of consecutive travel.
# For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.
#
# Return the minimum number of dollars you need to travel every day in the given list of days.
#
# Example 1:
#
# Input: days = [1,4,6,7,8,20], costs = [2,7,15]
# Output: 11
# Explanation:
# For example, here is one way to buy passes that lets you travel your travel plan:
# On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
# On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
# On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
# In total you spent $11 and covered all the days of your travel.
#
# Example 2:
#
# Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
# Output: 17
# Explanation:
# For example, here is one way to buy passes that lets you travel your travel plan:
# On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
# On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
# In total you spent $17 and covered all the days of your travel.
#
# We can solve this problem generate any possible combination for every day and considering the range between days,
# sounds too complex, so what we could do is use DP, similar to the coin change but in this case we need to discard
# (carry the DP value) for that days that is not in the agenda.


class Solution:
    def min_cost_tickets(self, days: [int], costs: [int]) -> int:
        minimum_cost = [max(days) * costs[2]] * (max(days) + 1)
        minimum_cost[0] = 0

        for day in range(1, max(days) + 1):
            if day in days:
                minimum_cost[day] = min(
                    minimum_cost[day - 1 if day >= 1 else 0] + costs[0],
                    minimum_cost[day - 7 if day >= 7 else 0] + costs[1],
                    minimum_cost[day - 30 if day >= 30 else 0] + costs[2]
                )
                # It's ok but we don't have any limitation to buy another
                # # minimum cost for 1-day pass
                # if 1 <= day:
                #     minimum_cost[day] = min(minimum_cost[day - 1] + costs[0], minimum_cost[day])
                # # minimum cost for 7-day pass
                # if 7 <= day:
                #     minimum_cost[day] = min(minimum_cost[day - 7] + costs[1], minimum_cost[day])
                # # minimum cost for 30-day pass
                # if 30 <= day:
                #     minimum_cost[day] = min(minimum_cost[day - 30] + costs[2], minimum_cost[day])

            else:
                minimum_cost[day] = minimum_cost[day - 1]
        return minimum_cost[-1]


solution = Solution()
# print(solution.min_cost_tickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]))
print(solution.min_cost_tickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))
# print(solution.min_cost_tickets([1, 4, 6, 7, 8, 20], [7, 2, 15]))
