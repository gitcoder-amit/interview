# 1423. Maximum Points You Can Obtain from Cards
# There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

# Your score is the sum of the points of the cards you have taken.

# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.


# T -> O(k)
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s = 0
        for i in range(k):
            s += cardPoints[i]
        
        lsum = s
        rsum = 0
        maxsum = lsum
       
        rindex = len(cardPoints)-1

        for i in range(k-1, -1, -1):
            lsum -= cardPoints[i]
            rsum += cardPoints[rindex]
            rindex -= 1
            maxsum = max(maxsum, lsum+rsum)
        
        return maxsum



        