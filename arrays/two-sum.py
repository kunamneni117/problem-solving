from typing import List,Optional
class Solution:
    def twoSumBruteforce_n2(self, nums: List[int], target: int) -> Optional[List[int]]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target-nums[i]==nums[j]:
                    return [i,j]
        return None

    def twoSum_nlogn(self,nums: List[int],target:int) -> Optional[List[int]]:
        position_array=nums
        if len(nums) and len(nums)>1:
            nums=sorted(nums)
            start=0
            end=len(nums)-1
            while(start<end):
                if nums[start]+nums[end]==target:
                    if nums[start]==nums[end]:
                        res=[]
                        for idx, val in enumerate(position_array):
                            if nums[start]== val:
                                res.append(idx)
                        return res
                    else:
                        return [position_array.index(nums[start]),position_array.index(nums[end])]
                elif nums[start]+nums[end]>target:
                    end-=1
                else:
                    start+=1

        else:
            return None

    def twoSum_n(self,nums: List[int],target: int)-> Optional[List[int]]:
        temp={value:id for id,value in enumerate(nums)}
        for i in range(len(nums)):
            subtract=target-nums[i]
            if subtract in temp and temp[subtract]!=i:
                return [i,temp[subtract]]