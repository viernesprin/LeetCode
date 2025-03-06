class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = []

        for i in candies:
            total_candies = i + extraCandies
            if total_candies >= max(candies):
                result.append(True)
            else:
                result.append(False)

        return result

