from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        col0 = 1
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] != 0:
                    if matrix[0][j] == 0 or matrix[i][0] == 0:
                        matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0
        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0
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
    solution.setZeroes(matrix)

    print("\nModified Matrix:")
    for row in matrix:
        print(row)

if __name__==main():
    main()
