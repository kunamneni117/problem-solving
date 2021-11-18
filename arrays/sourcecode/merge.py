from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j,k,l=m-1,n-1,m+n-1
        for i in range(m+n):
            if nums2[k]>nums1[j] and k>=0 and j>=0:
                nums1[l]=nums2[k]
                l-=1
                k-=1
            else:
                nums1[l]=nums1[j]
                l-=1
                j-=1
