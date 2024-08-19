# 150. Evaluate Reverse Polish Notation

class Solution:
    def resolve(self, a , b , Operator):
        if Operator == '+':
            return a + b
        elif Operator == '-':
            return b - a
        elif Operator == '*':
            return a * b
        elif Operator == '/':
            """if a > b :
                return int(a/b)
            else:"""
            return int(b/a) 
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if len(i) == 1 and ord(i) < 48:
                a = stack.pop()
                b = stack.pop()

                operator = i

                res = self.resolve(a,b,operator)
                stack.append(res)

            else:
                stack.append(int(i))

        return stack.pop()

