"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        

        # calculate sum of the window
        sum = 0
        for i in range(0, k):
            sum += nums[i]

        max_sum = sum

        # slide the window across the array and calculate max_sum
        for i in range(k, len(nums)):
            sum += nums[i]
            sum -= nums[i-k]
            max_sum = max(max_sum, sum)

        # return average 
        return float(max_sum/k) 