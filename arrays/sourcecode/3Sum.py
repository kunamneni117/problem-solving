from typing import List

class Solution:
    def threeSum_optimized(self, nums: List[int]) -> List[List[int]]:
        nums, n, answer = sorted(nums), len(nums), []
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: 
                continue    # skip duplicates
                
            left, right =  i+1, n-1
            while left < right:
                sum3 = nums[i] + nums[left] + nums[right]
                if left > i+1 and nums[left] == nums[left-1]: left += 1   # skip duplicates
                elif sum3 < 0: left += 1
                elif sum3 > 0: right -= 1
                else: 
                    answer.append([nums[i], nums[left], nums[right]])
                    left += 1
        return answer

    def threeSum(self, nums):
        if len(nums) <3: # deal with special input
            return []
        elif len(nums) == 3:
            if sum(nums) == 0:
                return [sorted(nums)]


        nums = sorted(nums) # sorted, O(nlgn)
        ans = []

        for i in range(len(nums) -2):
            j = i+1
            k = len(nums) -1 # hence i < j < k

            while j<k: # if not cross line
                temp_sum = nums[i] + nums[j] + nums[k]
                if temp_sum == 0:
                    ans.append((nums[i], nums[j], nums[k]))

                if temp_sum > 0: # which means we need smaller sum, move k backward, remember we sort the array
                    k -= 1
                else:
                    j += 1
        return [list(x) for x in set(tuple(x) for x in ans)]