from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp={}
        for num in nums:
            if num in temp:
                temp[num]+=1
            else:
                temp[num]=1
        for key,value in temp.items():
            if value>1:
                return True
        return False
    
    def containsDuplicate_nlogn(self, nums: List[int]) -> bool:
        nums=sorted(nums)
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False