class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        xstr = str(x)
        for i in range(len(xstr)):
            if xstr[i] != xstr[len(xstr)-1-i]:
                return False
        return True
