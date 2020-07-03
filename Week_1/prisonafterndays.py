#Brute Force Solution - TLE
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        dp = [[0]*8 for i in range(N+1)]
        dp[0] = cells
        for i in range(1,N+1):
            for j in range(1,7):
                if dp[i-1][j-1] == dp[i-1][j+1]:
                    dp[i][j] = 1
        
        return dp[N]

# https://bit.ly/2YXb1Ys
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        count = N % 14
        if count == 0:
            count = 14
        while count:
            temp = []
            temp.append(0)
            for i in range(1,7):
                if cells[i-1] == cells[i+1]:
                    temp.append(1)
                else:
                    temp.append(0)
            temp.append(0)
            cells = temp
            count-=1
        return cells

