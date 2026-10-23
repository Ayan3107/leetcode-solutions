class Solution:
    def sortPermutation(self, nums):
        k = -1

        for i in range(len(nums)):
            if nums[i] != i:
                if k == -1:
                    k = nums[i]
                else:
                    k &= nums[i]

        if k == -1:
            return 0

        return k
