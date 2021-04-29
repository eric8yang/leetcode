# sorta cool solution using de morgans
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        start = end = 0
        maxL = 1
        less = True
        while end < len(arr) - 1:
            end+=1
            if end - start == 1:
                if arr[start] == arr[end]:
                    start = end
                less = arr[start] < arr[end]
            elif (arr[end - 1] == arr[end]):
                start = end
            elif ((arr[end - 1] > arr[end]) or not less) and ((arr[end - 1] < arr[end]) or less):
                start = end = end - 1
            
            if end - start + 1 > maxL:
                maxL = end - start + 1
            
            less = not less
        
        return maxL
                
                
        