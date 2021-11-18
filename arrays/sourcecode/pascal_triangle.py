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