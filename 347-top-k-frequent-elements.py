"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        answer = []
        
        #place into KVP where key = the value and value = number of occurences
        for x in nums:
            if x in dict:
                dict[x] = dict[x] + 1
            else:
                dict[x] = 1

        #sort the dictionary by descending value, x[1] is the value and x[0] would be key
        #append each key to list *already sorted by descending so value(# of occurences doesnt matter)
        sortedDict = sorted(dict.items(), reverse=True, key=lambda x:x[1]); 
        for num in sortedDict:
            answer.append(num[0])
        
        return answer[0:k];

test = Solution();
test.topKFrequent([1,1,1,1,2,3,4,5,5], 2)
