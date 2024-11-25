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
