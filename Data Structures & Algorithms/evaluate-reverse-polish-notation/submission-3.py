import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                operand2 = stack.pop()
                operand1 = stack.pop()
                print("got ",operand1,"+",operand2,"=",operand1+operand2)
                stack.append(operand1 + operand2)
            elif tokens[i] == "-":
                operand2 = stack.pop()
                operand1 = stack.pop()
                print("got ",operand1,"-",operand2,"=",operand1-operand2)
                stack.append(operand1 - operand2)
            elif tokens[i] == "*":
                operand2 = stack.pop()
                operand1 = stack.pop()
                print("got ",operand1,"*",operand2,"=",operand1*operand2)
                stack.append(operand1*operand2)
            elif tokens[i] == "/":
                operand2 = stack.pop()
                operand1 = stack.pop()
                ans = float(operand1/operand2)
                ans = math.floor(ans) if ans>0 else math.ceil(ans)
                print("got ",operand1,"/",operand2,"=",ans)
                stack.append(ans)
            else:
                print("appending..",tokens[i])
                stack.append(int(tokens[i]))
        return math.floor(stack.pop())
        