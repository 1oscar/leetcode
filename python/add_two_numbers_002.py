#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/9 10:53
# @Author  : 1oscar
# @Software: PyCharm
"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        yushu = 0
        root=n=ListNode("root")
        while l1 or l2 or yushu:
            v1=v2=0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            yushu, chushu = divmod(v1 + v2 + yushu, 10)
            n.next=ListNode(chushu)
            n=n.next
        return root.next

# a = ListNode(2)
# a.next = ListNode(4)
# a.next.next = ListNode(3)
# b = ListNode(5)
# b.next = ListNode(6)
# b.next.next = ListNode(4)
# c = Solution().addTwoNumbers(a, b)
# print c.val, c.next.val, c.next.next.val
a = ListNode(5)
b = ListNode(5)
c = Solution().addTwoNumbers(a, b)
print c.val, c.next.val

"""
时间复杂度：max(O(l1),O(l2))
空间复杂度：max(O(l1),O(l2))或者max(O(l1),O(l2))

"""
