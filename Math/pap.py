# Product array puzzle


#User function Template for python3

class Solution:
    def productExceptSelf(self, nums, n):
        if n == 1:
            return [1]
            
        i ,  temp = 1 , 1
        
        prod = [ 1 for i in range(n)]
        
        for i in range(n):
            prod[i] = temp
            temp *= arr[i]
            
        temp = 1
        
        for i in range(n - 1, -1, -1):
            prod[i] *= temp
            temp *= arr[i]
            
        
        return prod


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends
