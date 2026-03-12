'''
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
 

'''


class Solution:
    def check_hash(self, s1, s2):
        if len(s1) != len(s2):
            return False
        count = [0] * 26
        for i in range(len(s1)):
            count[ord(s1[i]) - ord('a')] += 1
            count[ord(s2[i]) - ord('a')] -= 1
            
        for c in count:
            if c != 0:
                return False
        return True
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        n = len(strs)
        for i in range(n):
            if strs[i] == -1:
                continue
            group = [strs[i]]
            strs[i] = -1
            for j in range(i+1, n):
                if strs[j] == -1:
                    continue
                check = self.check_hash(group[0], strs[j])
                if check:
                    group.append(strs[j]) 
                    strs[j] = -1
            ans.append(group)
        return ans

        # T-> O(N * KlogK) S-> O(N)
        # N -> number of strings
        # K -> length of the longest string
        anagram_map = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagram_map:
                anagram_map[sorted_s].append(s)
            else:
                anagram_map[sorted_s] = [s]

        return list(anagram_map.values())
    

        # T-> O(N * K) S-> O(N)
        # N -> number of strings
        # K -> length of the longest string
        anagram_map = {}
        for s in strs:
            count = [0] * 26  # Since the problem states that the strings consist of lowercase English letters
            for char in s:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            if key in anagram_map:
                anagram_map[key].append(s)
            else:
                anagram_map[key] = [s]
        
        return list(anagram_map.values())

        
        