# Evaluation of Postfix Expression

class Solution:
    #Function to evaluate a postfix expression.
    def evaluatePostfix(self, S):
        
        stack = []

        #iterating over the given string.
        for i in S:

            #if current character is an operand, we push it to the stack.
            if i.isdigit():
                stack.append(i)

            #else current character is an operator.
            else:
                
                #we pop and store the values of first two elements of stack.
                val1 = stack.pop()
                val2 = stack.pop()
                
                #we perform required operation and push the result in stack.
                if(i=='/'):
                    p="//"
                    stack.append(str(eval(val2 + p + val1)))
                else:
                    stack.append(str(eval(val2 + i + val1)))
        
        #returning the top element of the stack.
        return stack.pop()
