from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        top = 0
        left = 0
        right = m - 1
        bottom = n - 1
        ans = []
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
        return ans
def main():
    print("Enter thr rows and columns")
    n,m=map(int,input().split())
    print("Enter the matrix row by row (space-separated):")
    matrix=[]
    for _ in range(n):
        row=list(map(int,input().split()))
        matrix.append(row)
    print("Original Matrix:")
    for row in matrix:
        print(row)

    solution = Solution()
    result=solution.spiralOrder(matrix)
    print(result)

if __name__==main():
    main()