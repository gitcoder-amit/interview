
# Time Complexity: O(n)
# Space Complexity: O(n)

def lengthOfLongestSubstring(s) :
        n = len(s)
        max_len = 0
        m = {}
        l, r = 0, 0

        while r < n:
            if s[r] in m and m[s[r]] >= l:
                l = m[s[r]] + 1
            max_len = max(max_len, r-l+1)

            m[s[r]] = r
            r += 1

        return max_len
        