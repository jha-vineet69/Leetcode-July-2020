class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        temp = 0
        for num in nums:
            temp^= num
        
        res = [0,0]
        lowbit = temp & (-temp)
        for num in nums:
            if (num & lowbit):
                res[0]^= num
            else:
                res[1]^= num
        return res
                
        