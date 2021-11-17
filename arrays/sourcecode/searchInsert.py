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
        l=0
        r=len(nums)
        while(l<r):
            mid=(l+r)//2
            if(nums[mid]>=target):
                r=mid
            else:
                l=mid+1
        return l


                