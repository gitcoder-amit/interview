# 5. Longest Palindromic Substring

'''Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.'''



# This is a brute force solution that checks all substrings to find the longest palindromic substring.
# Time Complexity: O(n^3) due to nested loops and string reversal checks.
# Space Complexity: O(1)
def longestPalindrome(self, s: str) -> str:
        n = len(s)
        r = ''
        for i in range(n):
            s1 = ''
            for j in range(i, n):
                s1 += s[j]
                if s1 == s1[::-1] and len(s1)>len(r):
                    r = s1
                    print(r)
        return r



# Time Complexity: O(n^2) due to the two-pointer expansion method.
# Space Complexity: O(1) since we are not using any additional data structures that grow with input size.
def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s


        LPS = ''

        for i in range(1, n):
            # consider odd length

            low = i
            high = i

            while s[low] == s[high]:
                low -= 1
                high += 1
                if low == -1 or high == n:
                    break
                
            

            palindrome = s[low+1: high]
            
            if len(palindrome) > len(LPS):
                LPS = palindrome

            
            # consider even length
            
            low = i-1
            high = i

            while s[low] == s[high]:
                low -= 1
                high += 1

                if low == -1 or high == n:
                    break

            palindrome = s[low+1: high]
            if len(palindrome) > len(LPS):
                LPS = palindrome

        return LPS
