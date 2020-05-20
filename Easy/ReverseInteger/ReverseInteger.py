class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        xstr = str(x)
        newstr = ''
        if xstr[0] == '-':
            newstr += '-'
            for i in range(len(xstr)-1):
                newstr += xstr[len(xstr)-1-i]
        else:
            for i in range(len(xstr)):
                newstr += xstr[len(xstr)-1-i]
        newx = int(newstr)
        if newx > ((2 ** 31) - 1) or newx < -(2 ** 31):
            return 0
        else: 
            return newx
