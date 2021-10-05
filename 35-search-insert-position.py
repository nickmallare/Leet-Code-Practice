""" 
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        head = 0
        tail = len(nums) - 1    
        while(head <= tail):
            index = (head + tail) //2
            val = nums[index]
            if val == target:
                return index
            #take the "middle" value and take the left or right side based on the middle number
            if val > target:
                tail = index - 1
            else:
                head = index + 1
        return head

