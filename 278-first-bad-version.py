# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

#TODO: Optimize this solution
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        tail = 0
        head = n
        split = n // 2
        
        if n == 1:
            return 1
        if n == 0:
            return 0
        for x in range(n):
            if  (not isBadVersion(split)) and isBadVersion(split + 1):
                return split + 1
            elif isBadVersion(split):
                #take left portion of list
                head = split
                split = (tail + split) // 2
            else:
                #take right portion of list
                tail = split
                split = (split + head) // 2
                
        return -1