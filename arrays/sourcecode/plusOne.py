from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits)<=1:
            if digits[0]<9:
                return [digits[0]+1]
            else:
                return [1,0]
        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]=digits[i]+1
                return digits
            else:
                digits[i]=0
                
        digits.insert(0,1)
        return digits