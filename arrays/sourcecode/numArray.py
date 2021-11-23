from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.summation=[0]
        for num in nums:
            self.summation+=self.summation[-1]+num,
            
    def sumRange(self, left: int, right: int) -> int:
        return self.summation[right+1]- self.summation[left]