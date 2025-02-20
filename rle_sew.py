from typing import List



class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        swords = sorted(words,key=len,reverse=True)

        s = ''
        for word in swords:
            if f'{word}#' not in s:
                s = s + word + '#'
        
        # print(s)
        return len(s)
    
inps = [["time","me","bell"],["t"]]
sol = Solution()
for i in inps:
    print(sol.minimumLengthEncoding(i))