


def groupAnagrams(self, strs):
    # T-> O(N * K) S-> O(N)
    # N -> number of strings
    # K -> length of the longest string
    anagram_map = {}
    for s in strs:
        count = [0] * 26  
        for char in s:
            count[ord(char) - ord('a')] += 1
        key = tuple(count)
        if key in anagram_map:
            anagram_map[key].append(s)
        else:
            anagram_map[key] = [s]
    
    return list(anagram_map.values())

        
        