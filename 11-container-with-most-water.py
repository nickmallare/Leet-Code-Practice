""" 
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        #O(n^2) brute force method, look into refactoring
        
        currLength = 0
        currHeight = 0
        index = 0
        answer = 0
        for x in height:
            for y in range(index, len(height) - 1, +1):
                if x < height[y]:
                    currHeight = x
                else:
                    currHeight = height[y]
                if (currHeight * (y - index)) > answer:
                    answer = currHeight * (y - index)
            index = index + 1
        return answer




