# Inefficient Brute Force Solution
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val = int("".join(str(x) for x in digits)) + 1
        ansList = []
        while val!=0:
            ansList.append(val%10)
            val//=10
        return reversed(ansList)


# Noice Solution - Less use of inbuilt methods and functions.
# Time Complexity: O(n)
# Space Complexity: O(1) - No extra space used.
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for index in range(len(digits)-1, -1, -1):
            digits[index] += 1
            if digits[index] != 10:
                return digits
            digits[index] = 0
        digits.insert(0,1)
        return digits
            
        