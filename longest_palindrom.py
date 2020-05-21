import numpy as np


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        N = len(s)
        max_len = 1
        i_max,j_max = 0,0
        dp_mtx = np.empty(shape=(N,N),dtype=object)
        for i in range(N):
            dp_mtx[i,i] = (i,i)
            # if i<N-1:
            #     if s[i] ==s[i+1]:
            #         dp_mtx[i, i] = (i, i+1)
        len_range = list(range(2,len(s)+1,1))
        for len_ in len_range:
            for i in range(N):
                j = i+len_-1
                if j >=len(s):
                    break
                if s[i]==s[j]:
                    if (dp_mtx[i+1,j-1] is not None and dp_mtx[i+1,j-1][0]==i+1 and dp_mtx[i+1,j-1][1]==j-1) or (j==i+1):
                        dp_mtx[i, j] = i, j
                        if j-i+1 > max_len:
                            i_max,j_max = i,j
                else:
                    dp_mtx[i,j]=dp_mtx[i+1,j-1]
        return s[i_max:j_max+1]

soln = Solution()
s = "bb"
pal = soln.longestPalindrome(s)
print(f'large pal = {pal}')