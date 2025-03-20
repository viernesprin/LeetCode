class Solution(object):
    def uniqueOccurrences(self, arr):
        freq = {}
        occurrences = set()

        for i in arr:
            num = arr.count(i)
            freq.update({i: num})
        
        for count in freq.values():
            if count in occurrences:
                return False
            occurrences.add(count)
        
        return True