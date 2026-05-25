class Solution {
    public int maxArea(int[] heights) {
        int i = 0;
        int j = heights.length - 1;
        int area = 0;
        while (i<j){
            int temp = Math.min(heights[i],heights[j]) * (j-i);
            if(temp>area){
                area = temp;
            }
            if(heights[i]<heights[j]){
                i += 1;
            }else if(heights[i]>heights[j]){
                j -= 1;
            }else{
                if(heights[i+1]>heights[j-1]){
                    i += 1;
                }else{
                    j -= 1;
                }
            }
        }
        return area;
    }
}
