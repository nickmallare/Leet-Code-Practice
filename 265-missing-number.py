""" 
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #solve with binary sort? O(log(n))

        #place into dictionary O(n)
        #loop while looking up KVP O(n)
        dict = {}
        counter = 0
        for x in nums:
            dict[x] = counter
            counter = counter + 1

        ans = 0
        for z in range(len(nums) + 1):
            if z in dict:
                ans = ans + 1
            else:
                return ans


