from typing import List

"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1
        vowels = "aeiou"

        while left < right:
            if s[left].lower() not in vowels:
                left += 1
                continue
            if s[right].lower() not in vowels:
                right -= 1
                continue
            # temp = s[left]
            # s[left] = s[right]
            # s[right] = temp
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1
        return "".join(s)



