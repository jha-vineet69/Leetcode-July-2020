class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hm = {}
        return self.findprofit(0, 0, prices, hm)
    
    def findprofit(self, i, bos, prices, hm):
        if i>= len(prices):
            return 0
        key = str(i) + " " + str(bos)
        
        if key in hm:
            return hm[key]
        
        profit = 0
        
        if bos == 0:
            buy = self.findprofit(i+1, 1, prices, hm) - prices[i]
            nobuy = self.findprofit(i+1, 0, prices, hm)
            profit = max(buy, nobuy)
        
        else:
            sell = self.findprofit(i+2, 0, prices, hm) + prices[i]
            nosell = self.findprofit(i+1, 1, prices, hm)
            profit = max(sell, nosell)
        
        hm[key] = profit
        
        return profit
        
        