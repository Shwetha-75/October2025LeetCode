import java.util.Arrays;

class MakeArrayElementsEqualtoZero{
    private class Solution{
    public int countValidSelections(int[] nums) {

        int count=0,n=nums.length;
        int[] sum_left=Arrays.copyOf(nums, n);
        int[] sum_right=Arrays.copyOf(nums, n);
        for(int i=1;i<n;i++){
            sum_left[i]+=sum_left[i-1];
        }
        for(int i=n-2;i>=0;i--){
            sum_right[i]+=sum_right[i+1];
        }
        
        for(int i=0;i<n;i++){
            if(nums[i]==0){
                int left=i>0?sum_left[i-1]:0;
                int right=i<n-1?sum_right[i+1]:0; 
                if(left==right){
                    count+=2;
                }else if(left-1==right){
                    count++;
                }else if(right-1==left){
                    count++;
                }
            }
        }

        return count;

        
       }
    }
}