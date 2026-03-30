'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

'''






class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Time Complexity: O(n*m)
        # Space Complexity: O(1) for the hash map
        #your code goes here
        n = len(s)
        m = len(t)
        res = ''
        min_len = 1000000000
        
        for i in range(n):
            st = ''
            c = 0
            h = [0]*256
            for ch in t:
                h[ord(ch)] += 1
            for j in range(i, n):
                st += s[j]
                if h[ord(s[j])] > 0:
                    c += 1
                    h[ord(s[j])] -= 1
                
                if c == m:
                    if j-i+1 < min_len:
                        min_len = j-i+1
                        res = st

        return res


    def minWindow(self, s: str, t: str) -> str:
        # Time Complexity: O(n + m)
        # Space Complexity: O(1) for the hash map
        n = len(s)
        m = len(t)
        h = [0]*256
        l, r = 0, 0
        res = ''
        min_len = 1000000

        for ch in t:
            h[ord(ch)] += 1
        c = 0
        while r < n:
            if h[ord(s[r])] > 0:
                c += 1
            h[ord(s[r])] -= 1

            while c == m:
                if r-l+1 < min_len:
                    min_len = r-l+1
                    res = s[l:r+1]

                h[ord(s[l])] += 1
                if h[ord(s[l])] > 0:
                    c -= 1
                l += 1
            
            r += 1

        return res

