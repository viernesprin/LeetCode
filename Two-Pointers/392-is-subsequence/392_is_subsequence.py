class Solution(object):
    def isSubsequence(self, s, t):
        i = 0
        j = 0

        if len(s) == 0:
            return True
        
        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)