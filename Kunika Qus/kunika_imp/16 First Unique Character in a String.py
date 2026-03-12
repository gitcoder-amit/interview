'''
387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1

 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
'''


class Solution:
    # Initial Approach
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def firstUniqChar(self, s: str) -> int:
        char_count = {}

        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        for i in range(len(s)):
            if char_count[s[i]] == 1:
                return i

        return -1
    
    # Optimized Approach
    # Time Complexity: O(N)
    # Space Complexity: O(1) since only lowercase English letters
    def firstUniqChar(self, s: str) -> int:
        char_count = [0] * 26  # Since only lowercase English letters

        for char in s:
            char_count[ord(char) - ord('a')] += 1

        for i in range(len(s)):
            if char_count[ord(s[i]) - ord('a')] == 1:
                return i

        return -1