from typing import List

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ...

        gr = defaultdict(list)

        for key in strs:
            skey = "".join(sorted(key))
            gr[skey].append(key)
        
        return list(gr.values())

inps = [[""],["eat","tea","tan","ate","nat","bat",'ftr'],["a"]]
sol = Solution()
for i in inps:
    print(sol.groupAnagrams(i))
