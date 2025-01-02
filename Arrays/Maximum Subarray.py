from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        maxSum = nums[0]
        for i in range(1,len(nums)):
            currSum=max(nums[i],currSum+nums[i])
            maxSum=max(maxSum,currSum)
        return maxSum
solution = Solution()

nums=list(map(int,input("Enter the list: ").split()))
print(solution.maxSubArray(nums))