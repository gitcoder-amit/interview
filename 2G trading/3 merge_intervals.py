# 56. Merge Intervals
def merge(self, intervals):
    # Time complexity: O(n log n + n)
    # Space complexity: O(n)
    n = len(intervals)
    if n <= 1:
        return intervals
    intervals.sort()
    ans = []
    for i in range(n):
        if ans == [] or intervals[i][0] > ans[-1][1]:
            ans.append(intervals[i])
        else:
            ans[-1][1] = max(ans[-1][1], intervals[i][1])
    return ans
        