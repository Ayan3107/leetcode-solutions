from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_count = [0] * 31

        for num in nums:
            for bit in range(31):
                if (num >> bit) & 1:
                    bit_count[bit] += 1

        ans = 0

        for _ in range(k):
            value = 0

            for bit in range(31):
                if bit_count[bit] > 0:
                    value |= 1 << bit
                    bit_count[bit] -= 1

            ans = (ans + value * value) % MOD

        return ans
