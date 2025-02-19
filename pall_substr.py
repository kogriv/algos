class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        lp = ''
        n=len(s)
        if n == 1:
            lp = s
        if n>=2 and s[0] == s[1]:
            lp = s[0:2]
        for i in range(1,n):
            print('i:',i,'letter:',s[i])
            lp1 = self.expand_around_center(s,i,i)
            print('lp1:',lp1)
            lp2 = self.expand_around_center(s,i,i+1)
            print('lp2:',lp2)
            lp3 = lp1 if len(lp1) >= len(lp2) else lp2
            print('lp3:',lp3)
            lp = lp3 if len(lp3) > len(lp) else lp
            print('lp:',lp)
            print('------------------------')

        return lp
        
    def expand_around_center(self, s, left_idx, right_idx):
        repeat = True
        lp = ''
        while repeat:
            
            print('left_idx:',left_idx, ', right_idx',right_idx)
            if left_idx>=0 and right_idx < len(s):
                print('s[left_idx]:',s[left_idx],', s[right_idx]:',s[right_idx])
            if left_idx>=0 and right_idx < len(s) and s[left_idx]==s[right_idx]:
                lp = s[left_idx: right_idx+1]
                print('=== lp:',lp)

                left_idx -= 1
                right_idx += 1
            else:
                repeat = False
        print('----')
        return lp
    
sol = Solution()
ss = [
    # '','aba','abba',
    #   "babad",
    #   "a"
    "ccd"
      ]
for s in ss:
    print(sol.longestPalindrome(s))
