from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pivot:int=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[pivot]=nums[i]
                pivot+=1
        return pivot