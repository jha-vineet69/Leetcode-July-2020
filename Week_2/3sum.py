class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        length = len(nums)
        for i in range(length-2):
            if (i==0 or (i>0 and nums[i]!=nums[i-1])):
                left = i + 1
                right = length - 1
                while left < right:
                    currentSum = nums[i] + nums[left] + nums[right]
                    if currentSum < 0:
                        left+= 1
                    elif currentSum > 0:
                        right-= 1
                    else:
                        triplets.append([nums[i], nums[left], nums[right]])
                        while left<right and nums[left]==nums[left+1]: left+=1
                        while left<right and nums[right]==nums[right-1]: right-=1
                        left+= 1
                        right-= 1
                

        return triplets
        