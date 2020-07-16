class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow
        
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        
        if n < 0: return 1.0 / self.myPow(x, -n)
        
        half = self.myPow(x, n // 2)
        
        if n % 2 == 0:
            return half * half
        
        else:
            return half * half * x
        