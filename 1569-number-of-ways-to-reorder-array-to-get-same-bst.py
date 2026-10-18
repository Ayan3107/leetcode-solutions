import sys
from math import comb

sys.setrecursionlimit(10000)


class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def count_ways(arr: list[int]) -> int:
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            left_ways = count_ways(left)
            right_ways = count_ways(right)

            ways_to_interleave = comb(len(left) + len(right), len(left))

            return (ways_to_interleave * left_ways * right_ways) % MOD

        return (count_ways(nums) - 1) % MOD
