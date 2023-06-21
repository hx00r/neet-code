from collections import defaultdict
from typing import List

# 49. Group Anagrams
class Solution(object):
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] += 1
            res[tuple(count)].append(word)

        return res.values()

