# 680. Valid Palindrome II

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        low , high = 0 , len(s) - 1
        c = 0
        while low < high:
            t1 , t2 = s[low] , s[high]
            if t1 == t2:
                low += 1
                high -= 1
            else:
                temp1 = s[ 0 : low ] + s[ low + 1 : ]
                temp2 = s[ 0 : high ] + s[ high + 1 : ]
                if temp1 == temp1[ : : -1 ]:
                    return True
                elif temp2 == temp2[ : : -1 ]:
                    return True
                else:
                    return False
        return True
