class Solution:
    def isValid(self, s: str) -> bool:
        temp = {"(":")", "[":"]", "{":"}" }
        stack = []
        for i in s:
            if i in temp.keys():
                stack.append(i)
            elif stack and temp[stack[-1]] == i:
                stack.pop()
            else: 
                return False
        if len(stack) == 0:
            return True
        else:
            return False
            
                