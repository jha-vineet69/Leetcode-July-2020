# Approach 1: Can't use in interviews
from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        p = []
        for i in range(len(nums)+1):
            p.extend(combinations(nums, i))
        plist = [list(item) for item in p]
        return(plist)


#Approach 2:
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            size = len(res)
            for j in range(size):
                r = res[j] + [i]
                res.append(r)
        
        return res
        