from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for s in strs:
            sorted_str = ''.join(sorted(s))
            anagram_dict[sorted_str].append(s)

        return list(anagram_dict.values())
solution = Solution()

strs =input("Enter the words: ").split()
print(solution.groupAnagrams(strs))