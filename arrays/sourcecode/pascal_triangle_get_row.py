from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for i in range(rowIndex+1):
		#fill in all the 1s
            res.append([1] * (i + 1))
        if rowIndex < 2:
            return res[-1]
        for i in range(2, rowIndex+1):
            for j in range(1, i):
			#fill in middle nums
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        return res[-1]
        
