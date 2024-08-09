# 22. Generate Parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(l,r,s):
            if len(s) == n * 2:
                result.append(s)
                return

            if l < n :
                dfs( l + 1 , r , s + '(' )
            
            if r < l :
                dfs( l , r + 1 , s + ')' )

        dfs(0,0,'')
        return result
