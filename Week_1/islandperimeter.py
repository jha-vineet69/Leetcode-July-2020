class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        r,c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    perimeter+=4
                    if i>0: perimeter-= grid[i-1][j]
                    if j>0: perimeter-= grid[i][j-1]
                    if i<r-1: perimeter-= grid[i+1][j]
                    if j<c-1: perimeter-= grid[i][j+1]
        return perimeter