from typing import List
from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup= defaultdict(int)
        for num in nums:
            dup[num] +=1
            if dup[num] > 1:
                return True

        return False
solution = Solution()

nums = list(map(int,input("Enter the list").split()))
result = solution.containsDuplicate(nums)
print(result)