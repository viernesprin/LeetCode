class Solution(object):
    def largestAltitude(self, gain):
        altitudes = [0]
        max = 0

        for i in range(len(gain)):
            temp = gain[i] + altitudes [i]
            altitudes.append(temp)

            if temp > max:
                max = temp
        return max