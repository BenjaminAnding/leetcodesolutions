class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        idx = [-1] * 256
        length = 0
        i = 0
        for j in range(len(s)):
            i = max(i, idx[ord(s[j])] + 1)
            length = max(length, j - i + 1)
            idx[ord(s[j])] = j
        return length
