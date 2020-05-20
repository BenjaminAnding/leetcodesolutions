class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        temp = str( int(''.join(map(str,digits)))+1 )
        return [int(c) for c in temp]
