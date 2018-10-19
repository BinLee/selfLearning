#!/usr/bin/python

'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

nums1 = [1, 3]
nums2 = [2]
The median is 2.0

nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        ans = nums1+nums2
        ans.sort()
        if len(ans)%2 == 0:
            return (float(ans[len(ans)/2-1])+float(ans[len(ans)/2]))/2
        else:
            return float(ans[len(ans)/2])

    def findMedianSortedArrays2(self, nums1, nums2):
        """
        O(log(m+n)) alogrithm
         
        divided into two part, [0,m] for nums1, and [0,n] for nums2
        if  want to divide into two equal part and max(left_part) <= min(right_part)
        there will be i for m and j will be  i+j=(m+n)/2 - 1

        """
        
        m = len(nums1)
        n = len(nums2)
        
        A = nums1
        B = nums2

        if m>n:
            m,n,A,B=n,m,nums2,nums1
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m+n+1)/2
        while imin<=imax:
            i = (imin+imax)/2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                imin = i+1
            elif i > 0 and A[i-1] > B[j]:
                imax = i-1
            else:
                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1],B[j-1])

                if (m+n)%2 == 1:
                    return max_of_left
                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i],B[j])

                return (max_of_left+min_of_right)/2.0

if __name__ == "__main__":
    nums1 = [1,2]
    nums2 = [3,4]

    a = Solution()
    print a.findMedianSortedArrays(nums1,nums2)
