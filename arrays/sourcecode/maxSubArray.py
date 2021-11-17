from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadane algorithm (Dynamic programming)
        """
        :type nums: List[int]
        :rtype: int
        """
        currentSum = nums[0] #setting current sum to be the first element
        maxSum = nums[0] #same thing for maxSum
        for i in range(1,len(nums)):
            if currentSum < 0:  #if currentsum is negative then that means ignore all the prev elements
                currentSum = nums[i]
            else:
                currentSum += nums[i] #if not add the current element to the currentSum
                    
            maxSum = max(currentSum, maxSum) #compare currentSum to maxSum. 
            
        return maxSum   