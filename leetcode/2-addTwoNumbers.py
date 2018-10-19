#!/usr/bin/python
import pdb
#Definition for singly-linked list.
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
        ans = ListNode(0)
        current = ans
        mod = 0
        while l1 or l2 or mod:
            val = mod
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            mod,val = divmod(val,10)
            current.next  = ListNode(val)
            current = current.next
        return ans.next 

    def addTwoNumbers1(self,l1,l2):
        '''
        fit reverse and non-reverse version
        int to str and then add together
        '''
        a,b = str(l1.val),str(l2.val)
        l1 = l1.next
        l2 = l2.next
        while  l1:
            a = str(l1.val) + a
            l1 = l1.next
        while  l2:
            b = str(l2.val) + b
            l2 = l2.next
        ans = str(int(a) + int(b))
        result = ListNode(0)
        current = result
        for i in range(len(ans)):
            current.next = ListNode(int(ans[len(ans)-i-1]))
            current = current.next

        return result 

if __name__ == "__main__":
#    a = [2 4 3]
#    b = [5 6 4]

    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)


    a = Solution()
    #ans = a.addTwoNumbers(l1,l2)
    a.addTwoNumbers1(l1,l2)
    #print ans.val
    #print ans.next.val
    #print ans.next.next.val
