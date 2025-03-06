class Solution(object):
    def reverseVowels(self, s):
        vowels = ['a', 'e', 'i','o','u']
        s_vowels = []
        new_string = []

        for c in s:
            if c.lower() in vowels:
                s_vowels.append(c)

        n = len(s_vowels) - 1

        for c in s:
            if c.lower() in vowels:
                new_string.append(s_vowels[n])
                n -= 1
                continue
            else:
                new_string.append(c)

        return ''.join(new_string)
