from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
def main():
    print("Enter size of square matrix")
    n=int(input())
    matrix=[]
    for _ in range(n):
        row=list(map(int,input().split()))
        matrix.append(row)

    sol=Solution()
    sol.rotate(matrix)

    print("Rotated Matrix:")
    for row in matrix:
        print(row)

if __name__==main():
    main()