class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = (int)(sqrt(2*n))
        sum = (int)(k*(k+1))/2
        if sum >n: 
            return k-1
        return k

# k(k+1)≤2N. Complete the square and isolating k gives the formula.
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (int)((2 * n + 0.25)**0.5 - 0.5)