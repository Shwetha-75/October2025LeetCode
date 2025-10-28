/**
 * @param {number[]} nums
 * @return {number}
 */
var countValidSelections = function(nums) {
    let sum_left=nums.slice();
    let n=nums.length;
    let sum_right=nums.slice();
    let count=0;
    for(let i=1;i<nums;i++){
        sum_left[i]+=sum_left[i-1];
    }
    for(let i=n-2;i>=0;i--){
        sum_right[i]+=sum_right[i+1];
    }
    for(let i=0;i<n;i++){
        if(nums[i]===0){

            let left=i>0 ? sum_left[i-1]:0 
            let right=i<n-1 ? sum_right[i+1]:0 
            if(left===right){
                count+=2
                
            }else if(left-1===right){
                count++
            }else if(right-1===left){
                count++
            }
        }
    }
    return count;
};