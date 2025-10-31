"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:

        # i = 0
        # holds = 0
        # while i < len(height)-1:
        #     j = i + 1
        #     while j < len(height):
        #         dist = j-i
        #         if height[i] > height[j]:
        #             if height[j] * dist > holds:
        #                 holds = height[j] * dist
        #         else:
        #             if height[i] * dist > holds:
        #                 holds = height[i] * dist
        #         j += 1
        #     i += 1
        # return holds

        left = 0 
        right = len(height)-1
        max_hold = 0 

        while left < right:
            dist = right - left
            holds = dist * min(height[left], height[right])  #area, basically
            if holds > max_hold:
                max_hold = holds
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_hold


from typing import List