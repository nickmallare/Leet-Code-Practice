"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dict = {}
        
        index = 0
        for x in nums:
            if x in dict:
                dict[x] = dict[x] + 1
            else:
                dict[x] = 0

        #get k top values in the KVP
        for y in nums:
            y