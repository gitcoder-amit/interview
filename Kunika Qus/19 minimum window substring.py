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

        sindex = -1
        min_len = 100000000
        for i in range(n):
            c = 0
            # h = {}
            h = [0]*256
            for k in t:
                # h[k] = h.get(i, 0) + 1
                h[ord(k)] += 1
            # print(h)
            for j in range(i, n):
                if h[ord(s[j])] != 0:
                    c += 1
                    h[ord(s[j])] -= 1
                    # if h[s[j]] == 0:
                    #     del h[s[j]]

            
                if c == m:
                    if j-i+1 < min_len:
                        min_len = j-i+1
                        sindex = i
        return s[sindex: sindex + min_len]


    def minWindow(self, s: str, t: str) -> str:
        # Time Complexity: O(n + m)
        # Space Complexity: O(1) for the hash map
        
        """ Variable to store the minimum 
        length of substring found """
        minLen = float('inf')
        
        """ Variable to store the starting index
        of the minimum length substring """
        sIndex = -1
        
        """ Array to count frequencies
        of characters in string t"""
        hash = [0] * 256
        
        # Count the frequencies of characters in t
        for c in t:
            hash[ord(c)] += 1
            
        count = 0
        l, r = 0, 0
        
        # Iterate through current window 
        while r < len(s):
            # Include the current character in the window
            if hash[ord(s[r])] > 0:
                count += 1
            hash[ord(s[r])] -= 1
                
            """ If all characters from t 
            are found in current window """
            while count == len(t):
                    
                """ Update minLen and sIndex
                if current window is smaller """
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    sIndex = l
                
                # Remove leftmost character from window
                hash[ord(s[l])] += 1
                if hash[ord(s[l])] > 0:
                    count -= 1
                l += 1
            r += 1
        
        # Return minimum length substring from s
        return s[sIndex:sIndex + minLen] if sIndex != -1 else ""

