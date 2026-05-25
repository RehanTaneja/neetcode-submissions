class Solution {
    public int findMin(int[] nums) {
        if(nums.length==1){
            return nums[0];
        }else if(nums.length==2){
            if(nums[0]>nums[1]){
                return nums[1];
            }else{
                return nums[0];
            }
        }
        int p1 = 0;
        int p2 = nums.length-1;
        while(p2>0){
            if(nums[p1]<nums[p2]){
                return nums[p1];
            }else{
                p1 = p2;
                p2 -= 1;
            }
        }
        return nums[1];
    }
}
