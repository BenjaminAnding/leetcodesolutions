class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if (len(s) == 0):
            return True
        if (len(s) % 2 != 0):
            return False
        queue = []
        for c in s:
            if (c in ['(', '{', '[']):
                queue.append(c)
            elif len(c) > 0 and len(queue) == 0:
                return False
            elif c == ')' and queue.pop() != '(':
                return False
            elif c == ']' and queue.pop() != '[':  
                return False
            elif c == '}' and queue.pop() != '{':
                return False
        if len(queue) > 0:
            return False
        else:
            return True
