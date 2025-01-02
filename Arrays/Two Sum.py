from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map={}
        for i,num in enumerate(nums):
            more=target-num

            if more in num_map:
                return [num_map[more],i]

            num_map[num]=i

        return []

solution = Solution()

nums = list(map(int,input("Enter the list").split()))
target = int(input("Enter target: "))
result = solution.twoSum(nums, target)
print(result)