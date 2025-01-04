from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize prefix and suffix products
        pre, suf = 1, 1
        # Initialize the answer to negative infinity
        ans = float('-inf')
        # Length of the array
        n = len(nums)

        for i in range(n):
            # Reset prefix product if it becomes zero
            if pre == 0:
                pre = 1
            # Reset suffix product if it becomes zero
            if suf == 0:
                suf = 1

            # Update prefix and suffix products
            pre *= nums[i]
            suf *= nums[n - i - 1]

            # Update the maximum product found so far
            ans = max(ans, pre, suf)

        return ans


# Main program to take user input
if __name__ == "__main__":
    # Taking input from the user
    nums = list(map(int, input("Enter the numbers separated by spaces: ").split()))

    # Creating an instance of the Solution class
    solution = Solution()

    # Calculating and printing the maximum product subarray
    print("The maximum product subarray is:", solution.maxProduct(nums))
