class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        idx = 0
        signed = False
        sign = 1
        if len(str.strip()) == 1 and (str.strip()[0] == '-' or str.strip()[0] == '+'):
            return 0
        for i in range(len(str.strip())):
            if str.strip()[i] == '-':
                if i == 0:
                    signed = True
                    sign = -1
                else:
                    break
            elif str.strip()[i] == '+':
                if i == 0:
                    signed = True
                    sign = 1
                else:
                    break
            elif str.strip()[i].isdigit():
                idx += 1
            else:
                break
        if idx > 0:
            if signed:
                idx += 1
            if sign > 0:
                return min((int(str.strip()[0:idx])), 2 ** 31 - 1)
            if sign < 0:
                return max((int(str.strip()[0:idx])), -2 ** 31)
        else:
            return 0
        
