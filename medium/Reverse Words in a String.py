

"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


"""

class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.strip()
        str_list = s.split()

        rev_list = str_list[::-1]
        # l = 0
        # r = len(str_list)-1
        # while l < r:
        #     str_list[l], str_list[r] = str_list[r], str_list[l]
        #     l += 1
        #     r -= 1

        return " ".join(rev_list)