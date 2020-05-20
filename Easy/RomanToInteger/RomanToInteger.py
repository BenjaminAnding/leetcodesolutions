class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        prevChar = None
        for i in s[::-1]:
            if i == 'I' and prevChar not in ('V', 'X'):
                total += 1
            if i == 'I' and prevChar in ('V', 'X'):
                total -= 1
            if i == 'V':
                total += 5
            if i == 'X' and prevChar not in ('L', 'C'):
                total += 10
            if i == 'X' and prevChar in ('L', 'C'):
                total -= 10
            if i == 'L':
                total += 50
            if i == 'C' and prevChar not in ('D', 'M'):
                total += 100
            if i == 'C' and prevChar in ('D', 'M'):
                total -= 100
            if i == 'D':
                total += 500
            if i == 'M':
                total += 1000
            prevChar = i
        return total
