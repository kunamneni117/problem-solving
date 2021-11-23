from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        first_index,last_index=0,len(height)-1
        for i in range(len(height)-1,-1,-1):
            if height[i]>=height[last_index]:
                first_index=i
        return (last_index-first_index)*min(height[last_index],height[first_index])