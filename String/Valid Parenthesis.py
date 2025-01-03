class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if bracket_map.get(char) != top:
                    return False
        return not stack
solution= Solution()
s="{[}"
print(solution.isValid(s))