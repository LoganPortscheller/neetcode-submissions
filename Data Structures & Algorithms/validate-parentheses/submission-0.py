from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        openingChars = {'(', '{', '['}
        closingChars = {')', '}', ']'}

        stack = deque()

        for c in s:
            if c in openingChars:
                stack.append(c)
            elif c in closingChars:
                if len(stack) == 0:
                    return False
                
                lastOpeningChar = stack.pop()
                if ((c == ')' and lastOpeningChar != '(') or 
                    (c == '}' and lastOpeningChar != '{') or 
                    (c == ']' and lastOpeningChar != '[')):
                    return False
            else:
                return False

        return True if len(stack) == 0 else False