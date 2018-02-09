#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/8 13:48
# @Author  : 1oscar
# @Site    :
# @File    : test.py
# @Software: PyCharm

"""
题目：
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9
return [0, 1].

"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
     """
        for i, ele in enumerate(nums):
            if (target - ele) in nums[i + 1:]:
                if ele == target - ele:
                    return list([nums.index(ele), nums[i + 1:].index(target - ele) + i + 1])
                else:
                    return list([nums.index(ele), nums.index(target - ele)])


# 更优的算法：

class Solution_best(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
     """

        def twoSum(self, nums, target):
            d = {}
            for i, n in enumerate(nums):
                m = target - n
                if m in d:
                    return [d[m], i]
                else:
                    d[n] = i


print Solution().twoSum(list([3, 2, 4]), 6)
print Solution().twoSum(list([3, 3]), 6)
print Solution().twoSum(list([2, 5, 5, 11]), 10)
print Solution().twoSum(list([3, 2, 3]), 6)


"""
时间复杂度： O(n)
空间 
Solution: O(1) 
Solution_best: O(n)

right answer 

[1, 2]
[0, 1]
[1, 2]
[0, 2]

"""
