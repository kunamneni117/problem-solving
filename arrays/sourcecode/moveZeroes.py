from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] ==0 and i < len(nums)-k:
                j=i
                while(j<len(nums)-k):
                    nums[j]=nums[j+1]
                    j+=1
                nums[j]=0
                k+=1

    def moveZeros_Optimized(self,nums:List[int] )-> None:
        j:int=0
        for i in range(len(nums)):
            if nums[i]==0:
                continue
            else:
                k:int=i
                while(k>j):
                    nums[k],nums[k-1]=nums[k-1],nums[k]
                    k-=1
                nums[k],nums[j]=nums[j],nums[k]
                j+=1