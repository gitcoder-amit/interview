# 438. Find All Anagrams in a String

'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.

'''




class Solution:
    # Time Complexity: O(26 * (n1-n2+1)) * O(n2) ~ O(n1*n2)
    # Space Complexity: O(1)
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n1 = len(s)
        n2 = len(p)
        ans = []
        m1 = [0]*26

        for ele in p:
            m1[ord(ele)-ord('a')] += 1


        i = 0
        while i < n1-n2+1:
            m2 = [0]*26
            for j in range(i, i+n2):
                m2[ord(s[j])-ord('a')] += 1
            if m1 == m2:
                ans.append(i)
            i += 1
        
        return ans

    # Time Complexity: O(n1 + n2)
    # Space Complexity: O(1)
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n1 = len(s)
        n2 = len(p)
        ans = []
        m1 = [0]*26

        if n1 < n2:
            return ans

        for ele in p:
            m1[ord(ele)-ord('a')] += 1



        m2 = [0]*26
        for j in range(n2):
            m2[ord(s[j])- ord('a')] += 1
        
        i, j = 0, n2-1
        ans = []
        while i < n1 and j < n1:
            if m1 == m2:
                ans.append(i)
            
            m2[ord(s[i])-ord('a')] -= 1
            i += 1
            j += 1
            if j < n1:
                m2[ord(s[j])-ord('a')] += 1
        
        return ans

    




        