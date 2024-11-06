class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr) - 2
        i = 1
        while i <= n:
            mid = i + (n-i)//2
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] < arr[mid+1]:
                i = mid+1
            else:
                n = mid-1
        return 0 
