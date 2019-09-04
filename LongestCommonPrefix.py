class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        temp = 9999999
        prefix = ""
        lastchar = None
        for str in strs:
            if len(str) < temp:
                temp = len(str)        
        for i in range(temp):
            good = True
            for str in strs:
                if lastchar is not None:
                    if str[i] != lastchar:
                        good = False
                lastchar = str[i]
            if good == True:
                if lastchar is not None:
                    prefix += lastchar
            else: 
                break
            lastchar = None
        return prefix
