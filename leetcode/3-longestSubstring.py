#!/usr/bin/python

import string

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        start = 0
        searchIndex = 0
        current = searchIndex+1
        while searchIndex < len(s) and current < len(s):
            a = s.find(s[current],searchIndex,current)
            if a < 0:
                current +=1
                maxLen = max(maxLen, current-searchIndex)
            else:
                l = current - searchIndex
                if maxLen < l:
                    maxLen = l
                searchIndex = a+1
                current = searchIndex +1

        return maxLen

    def lengthOfLongestSubstring2(self,s):
        a = []
        ans = 0
        index = 0
        while index < len(s):
            if s[index] in a:
                a.append(s[index])
                a = a[a.index(s[index])+1:]
            else:
                a.append(s[index])
            index += 1 
            if len(a) >ans:
                ans = len(a)
        return ans

    def lengthOfLongestSubstring3(slef,s):
        dic = {}
        start = maxLen = 0
        for i in range(len(s)):
            if s[i] in dic and start <= dic[s[i]]:
                start = dic[s[i]]+1
            else:
                maxLen = max(maxLen,i-start+1)
            dic[s[i]] = i
        return maxLen
            
if __name__ == '__main__':
    a = Solution()
    s = ""
    print a.lengthOfLongestSubstring2(s)
    
