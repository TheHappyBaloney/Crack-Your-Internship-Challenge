# 844. Backspace String Compare

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(s: str) -> list:
            stack = []
            for char in s:
                if char == '#':
                    if stack:
                        stack.pop()  
                else:
                    stack.append(char)  
            return stack
            
        processed_s = process_string(s)
        processed_t = process_string(t)
            
        return processed_s == processed_t
