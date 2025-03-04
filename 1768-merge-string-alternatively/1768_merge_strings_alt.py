class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        w1_len = len(word1)
        w2_len = len(word2)
        i = 0
        j = 0
        result = []

        while i < w1_len or j < w2_len:
            if i < w1_len:
                result.append(word1[i])
                i += 1
            if j < w2_len:
                result.append(word2[j])
                j += 1
               
        return "".join(result)