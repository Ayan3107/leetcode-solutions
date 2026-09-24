class Solution(object):
    def sallestindex(self,nums):
        for i, num in enumerate(nums):
            if sum(map(int, str(num)))==i:
                return i

        return -1    