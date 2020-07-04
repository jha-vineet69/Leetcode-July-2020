class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = []
        nums.append(1)
        i = j = k = 0
        size = 1
        while (size < n):
            temp1 = nums[i]*2
            temp2 = nums[j]*3
            temp3 = nums[k]*5
            
            minNum = min(temp1, temp2, temp3)
            
            nums.append(minNum)
            size+= 1
            
            if minNum == temp1: i+=1
            if minNum == temp2: j+=1
            if minNum == temp3: k+=1
        return nums[-1]
        