class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        stack = []
        for i in s:
            if i=="(" or i=="[" or i=="{":
                stack+=i
            else:
                if len(stack)==0:
                    return False
                elif i==")":
                    if stack[len(stack)-1]=="(":
                        stack.pop()
                    else:
                        return False
                elif i=="]":
                    if stack[len(stack)-1]=="[":
                        stack.pop()
                    else:
                        return False
                elif i=="}":
                    if stack[len(stack)-1]=="{":
                        stack.pop()
                    else:
                        return False
        return len(stack)==0