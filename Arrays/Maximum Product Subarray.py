from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0;
        min_product = max_product = res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                min_product, max_product = max_product, min_product
            min_product = min(nums[i], min_product * nums[i])
            max_product = max(nums[i], max_product * nums[i])
            res = max(res, max_product)
        return res

nums = list(map(int, input("Enter the numbers: ").split()))
solution = Solution()
print("The maximum product subarray is:", solution.maxProduct(nums))
