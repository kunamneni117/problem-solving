from typing import List

class solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows<=2:
            return [[1]] if numRows <=1 else [[1],[1,1]]
        output=[[1],[1,1]]
        for i in range(2,numRows):
            temp=1
            local_output=[]
            while(True):
                if temp==i:
                    break
                local_output.append(output[i-1][temp-1]+output[i-1][temp])
                temp+=1
            output.append([1]+local_output+[1])
        return output

    def generate_optimized(self, numRows: int) -> List[List[int]]:
        dp=[[1 for i in range(j+1)] for j in range(numRows)]
        
        for i in range(2,len(dp)):
            for j in range(1,len(dp[i])-1):
                dp[i][j]=dp[i-1][j]+dp[i-1][j-1]
        
        return dp

    def generate_optimized1(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
		#fill in all the 1s
            res.append([1] * (i + 1))
        if numRows < 3:
            return res
        for i in range(2, numRows):
            for j in range(1, i):
			#fill in middle nums
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        return res