from typing import List

class Solution:
    def searchInsert_bruteforce_n(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        for id,value in enumerate(nums):
            if target ==value:
                return id
            if id < len(nums)-1:
                if target > value and target < nums[id+1]:
                    return id+1
        return len(nums)

    def searchInsert(self,nums:List[int],target:int) -> int:
        start:int=0
        end:int=len(nums)
        
        if target <= nums[0]:
            return 0
        while(start<end):
            mid:int=(start+end)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] < target:
                start=mid+1
            else:
                end=mid
        return start


                