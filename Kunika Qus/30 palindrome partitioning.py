# 131. Palindrome Partitioning

'''

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.'''


#  Time complexity: O(2^n * n) due to the recursive nature of the solution, where n is the length of the string s. Each character can either be included in a partition or not, leading to 2^n possible combinations. The additional n factor comes from the time taken to check if a substring is a palindrome and to copy the current partition into the result list.
# Space complexity: O(n) for the recursion stack and the space used to store the current partition. The result list can grow up to O(2^n) in size, but this is not counted in the space complexity of the algorithm itself.
class Solution:
    def is_palindrome(self, s):
        l, r = 0, len(s)-1
        while l <= r:
            if s[r] != s[l]:
                return False
            l += 1
            r -= 1
        return True
    
    def helper(self, s, ans, li):
        if s == '':
            ans.append(li[:])
            return
        
        for partition in range(1, len(s)+1):
            prefix = s[0:partition]
            remaining = s[partition:]
            if self.is_palindrome(prefix):
                li.append(prefix)
                self.helper(remaining, ans, li)
                li.pop()

    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.helper(s, ans, [])
        return ans
        