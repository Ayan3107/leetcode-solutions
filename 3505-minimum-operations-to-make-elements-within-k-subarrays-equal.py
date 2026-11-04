import heapq
from collections import defaultdict


class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)

        # lower: max heap for the smaller half
        # upper: min heap for the larger half
        lower = []
        upper = []
        delayed = defaultdict(int)

        lower_size = 0
        upper_size = 0
        lower_sum = 0
        upper_sum = 0

        def prune(heap, is_lower):
            while heap:
                num = -heap[0] if is_lower else heap[0]

                if delayed[num] == 0:
                    break

                delayed[num] -= 1
                heapq.heappop(heap)

        def rebalance():
            nonlocal lower_size, upper_size
            nonlocal lower_sum, upper_sum

            if lower_size > upper_size + 1:
                num = -heapq.heappop(lower)
                lower_size -= 1
                upper_size += 1
                lower_sum -= num
                upper_sum += num
                heapq.heappush(upper, num)
                prune(lower, True)

            elif lower_size < upper_size:
                num = heapq.heappop(upper)
                upper_size -= 1
                lower_size += 1
                upper_sum -= num
                lower_sum += num
                heapq.heappush(lower, -num)
                prune(upper, False)

        def add(num):
            nonlocal lower_size, upper_size
            nonlocal lower_sum, upper_sum

            if not lower or num <= -lower[0]:
                heapq.heappush(lower, -num)
                lower_size += 1
                lower_sum += num
            else:
                heapq.heappush(upper, num)
                upper_size += 1
                upper_sum += num

            rebalance()

        def remove(num):
            nonlocal lower_size, upper_size
            nonlocal lower_sum, upper_sum

            delayed[num] += 1

            if num <= -lower[0]:
                lower_size -= 1
                lower_sum -= num

                if num == -lower[0]:
                    prune(lower, True)
            else:
                upper_size -= 1
                upper_sum -= num

                if upper and num == upper[0]:
                    prune(upper, False)

            rebalance()

        def get_cost():
            median = -lower[0]
            left_cost = median * lower_size - lower_sum
            right_cost = upper_sum - median * upper_size
            return left_cost + right_cost

        # Calculate the minimum equalization cost for every window of size x.
        costs = []

        for i in range(n):
            add(nums[i])

            if i >= x:
                remove(nums[i - x])

            if i >= x - 1:
                costs.append(get_cost())

        # dp[i][j] is the minimum cost to choose exactly j
        # non-overlapping windows from the first i elements.
        INF = float("inf")
        dp = [[INF] * (k + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                # Skip the current element.
                dp[i][j] = dp[i - 1][j]

                # Choose the window ending at index i - 1.
                if i >= x:
                    window_cost = costs[i - x]
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i - x][j - 1] + window_cost
                    )

        return dp[n][k]
