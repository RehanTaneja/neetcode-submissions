class Solution {
    public int search(int[] nums, int target) {
        int first = 0;
        int last = nums.length - 1;
        if(nums.length<3){
            if(nums[first]==target){
                return first;
            }else if(nums[last]==target){
                return last;
            }else{
                return -1;
            }
        }
        while(first<=last){
            int mid = first+(int)Math.floor((last-first)/2);
            if(nums[mid]==target){
                return mid;
            }else if(nums[mid]<target){
                first = mid+1;
            }else{
                last = mid-1;
            }
        }
        return -1;
    }
}
