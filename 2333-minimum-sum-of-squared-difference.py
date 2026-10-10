from typing import List


class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2
        total = sum(diffs)

        if k >= total:
            return 0

        left, right = 0, max(diffs)

        while left < right:
            mid = (left + right) // 2
            needed = sum(max(0, diff - mid) for diff in diffs)

            if needed <= k:
                right = mid
            else:
                left = mid + 1

        level = left
        used = sum(max(0, diff - level) for diff in diffs)
        remaining = k - used

        answer = sum(min(diff, level) ** 2 for diff in diffs)
        answer -= remaining * (2 * level - 1)

        return answer
