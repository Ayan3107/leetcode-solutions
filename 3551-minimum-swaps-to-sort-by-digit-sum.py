class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def digit_sum(num):
            total = 0
            while num:
                total += num % 10
                num //= 10
            return total

        target = sorted(nums, key=lambda x: (digit_sum(x), x))
        position = {num: i for i, num in enumerate(nums)}
        swaps = 0

        for i in range(len(nums)):
            if nums[i] == target[i]:
                continue

            j = position[target[i]]

            position[nums[i]] = j
            position[target[i]] = i
            nums[i], nums[j] = nums[j], nums[i]
            swaps += 1

        return swaps
