from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = 0
        while i < j:
            cur_max = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, cur_max)
            if (height[i] < height[j]):
                i = i + 1
            else:
                j = j - 1
        return max_area
solution=Solution()
height=list(map(int,input("Enter heights ").split(',')))
print(solution.maxArea(height))