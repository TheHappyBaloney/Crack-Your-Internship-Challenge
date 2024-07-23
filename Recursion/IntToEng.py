# 273. Integer to English Words

class Solution:
    def __init__(self):
        self.ones = [ '' , ' One' , ' Two' , ' Three' , ' Four' , ' Five' , ' Six' , ' Seven' , ' Eight' , ' Nine' , ' Ten', ' Eleven' , ' Twelve' , ' Thirteen' , ' Fourteen' , ' Fifteen' , ' Sixteen' , ' Seventeen' , ' Eighteen' , ' Nineteen' ]
        self.tens = [ '' , ' Ten' , ' Twenty' , ' Thirty' , ' Forty' , ' Fifty' , ' Sixty' , ' Seventy' , ' Eighty' , ' Ninety' ]
        self.thousands = [ '' , ' Thousand' , ' Million' , ' Billion' ]
    
    def helper(self, num: int) -> str:
        if num < 20 :
            return self.ones[num]

        elif num < 100 :
           return self.tens[ num // 10 ] + self.ones[num % 10]

        elif num < 1000:
            return self.ones[ num // 100 ] + " Hundred" + self.helper( num % 100 )
        else:
            for i in range(3,0,-1):
                if num >= 1000 ** i :
                    return self.helper(num // (1000 ** i)) + self.thousands[i] + self.helper(num % (1000 ** i))
        return ''
    
    def numberToWords(self, num: int) -> str:
        if num == 0 :
            return 'Zero'

        return self.helper(num).lstrip()
        
