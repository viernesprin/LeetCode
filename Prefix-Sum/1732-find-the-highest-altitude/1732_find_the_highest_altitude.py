<<<<<<< HEAD
class Solution(object):
    def largestAltitude(self, gain):
        altitudes = [0]
        max = 0

        for i in range(len(gain)):
            temp = gain[i] + altitudes [i]
            altitudes.append(temp)

            if temp > max:
                max = temp
=======
class Solution(object):
    def largestAltitude(self, gain):
        altitudes = [0]
        max = 0

        for i in range(len(gain)):
            temp = gain[i] + altitudes [i]
            altitudes.append(temp)

            if temp > max:
                max = temp
>>>>>>> 217cbfda8fc661c365c68536e588296e8150d6ea
        return max