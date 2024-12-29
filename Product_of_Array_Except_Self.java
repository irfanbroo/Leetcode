class Solution {
    public int[] productExceptSelf(int[] nums) {
      int  N = nums.length;
        int[] left_array = new int[N];
        int[] right_array = new int[N];
        left_array[0]=1;
        right_array[N-1]=1;
        for(int i=1;i<N;i++)
        {
            left_array[i] = left_array[i-1]*nums[i-1];
        }
        for(int i=N-2;i>=0;i--)
        {
            right_array[i] = right_array[i+1]*nums[i+1];
        }
        for(int i=0;i<N;i++)
        {
            nums[i]=right_array[i]*left_array[i];
        }
        return nums;
    }
}




class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        larr=[1] * n 
        rarr=[1] * n
        arr=[0] * n
        
        larr[0] = 1
        rarr[n-1] = 1
        for i in range(1,n):
            larr[i] = larr[i-1] * nums[i-1]
        for j in range(n-2,-1,-1):
            rarr[j] = rarr[j+1] * nums[j+1]
        for i in range(n):
            arr[i] = larr[i] * rarr[i]
        return arr 
