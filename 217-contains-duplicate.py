""" 
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        dict = {}

        index = 0
        for x in nums:
            if x in dict:
                return True
            else:
                dict[x] = index
                index = index + 1
        return False


