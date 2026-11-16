class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c in '+*-/':
                num2 = stack.pop()
                num1 = stack.pop()
                if c == '+':
                    num1 += num2
                elif c == '*':
                    num1 *= num2
                elif c == '-':
                    num1 -= num2
                else:
                    num1 = int(num1/num2)
                stack.append(num1)
            else:
                stack.append(int(c))

        return stack[-1] if stack else 0