class Solution(object):
    def gcdOfStrings(self, str1, str2):
        s1_len = len(str1)
        s2_len = len(str2)

        def valid(k):
            if s1_len % k or s2_len % k:
                return False
            n1 = s1_len // k
            n2 = s2_len // k
            base = str1[:k]
            return str1 == base * n1 and str2 == base * n2

        for i in range(min(s1_len, s2_len), 0, -1):
            if valid(i):
                return str1[:i]
        
        return ""
        

        