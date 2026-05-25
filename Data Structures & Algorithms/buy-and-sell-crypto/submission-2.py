class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = 0
        start = 1
        max_index = 0
        profit = 0
        while start < len(prices):
            if start > max_index:
                i = start
                max_index = start
                while i < len(prices):
                    if prices[i] > prices[max_index]:
                        max_index = i
                    i+=1
            temp = prices[max_index] - prices[curr]
            if temp > profit:
                profit = temp
            curr+=1
            start+=1
        return profit