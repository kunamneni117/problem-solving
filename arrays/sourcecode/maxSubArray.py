from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadane algorithm (Dynamic programming)
        if not nums:
            return 0
        cursorsum=maxsum=nums[0]
        for i in range(1,len(nums)):
            cursorsum=max(nums[i],cursorsum+nums[i])
            maxsum=max(maxsum,cursorsum)
        return maxsum