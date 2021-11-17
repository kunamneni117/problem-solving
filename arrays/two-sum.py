from typing import List,Optional
class Solution:
    def twoSumBruteforce(self, nums: List[int], target: int) -> Optional[List[int]]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target-nums[i]==nums[j]:
                    return [i,j]
        return None
    def twoSum(self,nums: List[int],target:int) -> Optional[List[int]]:
        position_array=nums
        if len(nums) and len(nums)>1:
            nums=sorted(nums)
            start=0
            end=len(nums)-1
            while(start<end):
                if nums[start]+nums[end]==target:
                    if nums[start]==nums[end]:
                        return [position_array.index(nums[start]),position_array.index(nums[end])+1] 
                    else:
                        return [position_array.index(nums[start]),position_array.index(nums[end])]
                elif nums[start]+nums[end]>target:
                    end-=1
                else:
                    start+=1

        else:
            return None