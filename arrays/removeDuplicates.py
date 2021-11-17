from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ## given sorted array need to remove duplicates inplace
        pivot:int=1
        for i in range(1,len(nums)):
            if nums[i-1]!=nums[i]:
                nums[pivot]=nums[i]
                pivot+=1
        return pivot