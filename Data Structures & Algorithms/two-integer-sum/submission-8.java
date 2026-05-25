class Solution {
    public int[] twoSum(int[] nums, int target) {
        if (nums.length==2){
            int[] answer = new int[2];
            answer[0] = 0;
            answer[1] = 1;
            return answer;
        }
        int j = nums.length-1;
        while (j>0){
            int i=0;
            while (i<j){
                if (nums[i]+nums[j]==target){
                    int[] answer = new int[2];
                    answer[0] = i;
                    answer[1] = j;
                    return answer;
                }
                i++;
            }
            j--;
        }
        int[] answer = new int[2];
        answer[0] = 0;
        answer[1] = j;
        return answer;
    }
}
