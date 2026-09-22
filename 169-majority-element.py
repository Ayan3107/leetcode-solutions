class Solution(object):
    def majorityElements(self, nums):
        counter = {}

        for num in nums:
            if num in counter:
                counter+=1
            else:
                counter[num]=1

                highest-count=0
                majority=0

        for num in counter:
            if counter[num]>highest_count:
                highest_count=counter[num]
                majority=num

        return(majority)                