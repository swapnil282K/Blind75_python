from typing import List


class Solution:
    def findMin(self, arr: List[int]) -> int:
        s, e = 0, len(arr) - 1
        ans = float('inf')  # Initialize to positive infinity

        while s <= e:
            mid = (s + e) // 2

            # If the array segment is already sorted
            if arr[s] <= arr[e]:
                ans = min(ans, arr[s])
                break

            # If the left half is sorted
            if arr[s] <= arr[mid]:
                ans = min(ans, arr[s])
                s = mid + 1
            else:  # If the right half is sorted
                ans = min(ans, arr[mid])
                e = mid - 1

        return ans
solution = Solution()
nums = list(map(int,input("Enter the list").split()))
result = solution.findMin(nums)
print(result)