class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length==1){return 1;}
        if (nums.length==0){return 0;}
        int answer = 0;
        Arrays.sort(nums);
        List<Integer> newNum = new ArrayList<Integer>();
        newNum.add(nums[0]);
        for (int i=1;i<nums.length;i++){
            if (nums[i-1]!=nums[i]){
                newNum.add(nums[i]);
            }
        }
        int curr = 0;
        int maxi = 0;
        for (int i=0;i<newNum.size()-1;i++){
            if ((newNum.get(i+1)==newNum.get(i)+1) || (newNum.get(i+1)==newNum.get(i))){
                curr++;
            }else{
                if (curr>maxi){
                    maxi = curr;
                }
                curr=0;
            }
        }
        if (curr>maxi){
            maxi = curr;
        }
        return maxi+1;
    }
}
