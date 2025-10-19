import java.util.LinkedHashMap;
import java.util.Map;

class SmallestMissingNonnegativeIntegerAfterOperations{
    
    private class Solution{
            public int findSmallestInteger(int[] nums, int value) {
                 int mex=0,n=nums.length;
                 Map<Integer,Integer> map=new LinkedHashMap<Integer,Integer>();
                 for(int i=0;i<n;i++){
                    int temp=((nums[i]%value)+value)%value; 
                    map.put(temp, map.getOrDefault(temp,0)+1);

                 }
                 while(true){
                    if(!map.containsKey(mex%value) || map.get(mex%value)==0){
                        return mex;

                    }
                    map.put(mex%value, map.get(mex%value)-1);
                    mex++;

                 }

            }
    }
    
    public static void main(String[] args) {
        
    }

    public int findSmallestInteger(int[] nums,int k){
        return new Solution().findSmallestInteger(nums, k);
    }


}
