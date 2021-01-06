# A conveyor belt has packages that must be shipped from one port to another within D days.
#
# The i-th package on the conveyor belt has a weight of weights[i].  Each day, we load the ship with packages on the
# conveyor belt (in the order given by weights).
# We may not load more weight than the maximum weight capacity of the ship.
#
# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being
# shipped within D days

# To solve this problem we need to create packages, the sum of that packages will be the capacity of the shipment.
# The shipment capacity it will be at least equal to the max weight in the weights and the max value will be the weights
# sum

# Approach 1, Brute Force
# Works fine but 'Time Limit Exceeded' result

# class Solution:
#     def ship_within_days(self, weights: [int], D: int) -> int:
#         min_shipment = max(weights)
#         max_shipment = sum(weights)
#         possible_capacity = 0
#         for capacity in range(min_shipment, max_shipment+1):
#             print(capacity)
#             load = 0
#             package = []
#             days = []
#             for item in weights:
#                 if load + item <= capacity:
#                     package.append(item)
#                     load += item
#                 else:
#                     days.append(package)
#                     package = list()
#                     package.append(item)
#                     load = item
#             if package:
#                 days.append(package)
#             print(days)
#
#             if len(days) <= D:
#                 possible_capacity = capacity
#                 break
#         return possible_capacity


# Approach 2, Binary search to avoid visit every number and instead of use arrays to package and count the days I could
# use bare integers.


class Solution:
    def ship_within_days(self, weights: [int], D: int) -> int:
        min_shipment = max(weights)
        max_shipment = sum(weights)
        steps = 0
        while min_shipment <= max_shipment:
            print('min', min_shipment, 'max', max_shipment)
            steps += 1
            capacity = min_shipment + (max_shipment - min_shipment) // 2

            if self.test_capacity(weights, capacity) < D:
                max_shipment = capacity - 1
            else:
                min_shipment = capacity + 1
        print('min', min_shipment, 'max', max_shipment)
        print(steps)
        return min_shipment

    def test_capacity(self, weights: [int], capacity: int) -> int:
        load = 0
        days = 0
        for item in weights:
            load += item
            if capacity < load:
                days += 1
                load = item
        print('capacity', capacity, 'days', days)
        return days


solution = Solution()
print(solution.ship_within_days(
    [500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
     500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
     500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
     500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
     500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
     500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
     500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
     500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
     500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
     500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
     500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
     500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
     500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
     500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
     500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
     500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
     500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
     500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
     500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
     500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
     500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
     500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500], 1))
