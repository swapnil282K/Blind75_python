from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, word, i, j, index):
            if index == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
                return False
            temp = board[i][j]
            board[i][j] = ''
            result = (dfs(board, word, i + 1, j, index + 1) or dfs(board, word, i - 1, j, index + 1) or dfs(board, word,
                                                                                                            i, j + 1,
                                                                                                            index + 1) or dfs(
                board, word, i, j - 1, index + 1))

            board[i][j] = temp
            return result

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(board, word, i, j, 0):
                        return True
        return False
n,m=map(int,input("Enter size of matrix").split())
board=[]
for _ in range(n):
    row=list(input())
    board.append(row)
word=input("Enter word")

solution=Solution()
if solution.exist(board,word):
    print("True")
else:
    print("False")

