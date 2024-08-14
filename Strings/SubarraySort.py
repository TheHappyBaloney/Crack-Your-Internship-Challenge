# Check if array is sorted
#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        n = len(arr)
        temp = [0] * n 
        for i in range(n): 
            temp[i] = arr[i] 
      
        temp.sort() 
      
        for front in range(n): 
            if temp[front] != arr[front]: 
                break
      
        for back in range(n - 1, -1, -1): 
            if temp[back] != arr[back]: 
                break
      
        if front >= back: 
            return True
        while front != back: 
            front += 1
            if arr[front - 1] < arr[front]: 
                return False
        return True

#{ 
 # Driver Code Starts
# Importing necessary modules
import sys
from typing import List

# Main function
if __name__ == "__main__":
    input = sys.stdin.read().strip().split("\n")
    t = int(input[0])
    index = 1
    solution = Solution()

    for _ in range(t):
        line = list(map(int, input[index].strip().split()))
        index += 1
        ans = solution.arraySortedOrNot(line)
        print("true" if ans else "false")
# } Driver Code Ends
