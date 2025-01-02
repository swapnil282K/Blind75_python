from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        min_price = float('inf')
        for price in prices:
            min_price = min(min_price, price)
            maxprofit = max(maxprofit, price - min_price)

        return maxprofit

solution = Solution()

nums = list(map(int,input("Enter the list").split()))
result = solution.maxProfit(nums)
print(result)