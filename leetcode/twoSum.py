#!/usr/bin/python
#2018-06-28
'''
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

solution: the most directive way is brute force, time O(N^2), space O(1)
'''
import pdb
class Solution(object):
    def twoSum(self, nums, target):
        '''
        :type nums: List[int]
        :type target: int
        :rtype List[int]
         '''
        for i in range(len(nums)):
            for j in range(len(nums)):
                ans = nums[i]+nums[j]
                if ans == target:
                    return [i,j]

    def twoSum1(self ,nums, target):
        lookup = {}
        #pdb.set_trace()
        for i ,num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target-num], i]
            lookup[num] = 1

#test case 
if __name__ == '__main__':
    nums = [2,7,11]
    target = 9
    f = Solution()
    print f.twoSum1(nums , target)
