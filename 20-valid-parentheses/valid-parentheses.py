class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)

            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()

                if c == ')':
                    if last != '(':
                        return False

                if c == ']':
                    if last != '[':
                        return False

                if c == '}':
                    if last != '{':
                        return False
        if len(stack) == 0:
            return True
        else:
            return False