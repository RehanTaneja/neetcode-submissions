class KthLargest {

    public int[] nums;
    public int k;

    public KthLargest(int k, int[] nums) {
        this.k = 0;
        this.nums = new int[k];
        int j = 0;
        while(j<=k-1 && j<nums.length){
            this.nums[j] = nums[j];
            j++;
            this.k++;
        }
        minHeapify();
        int i = k;
        while(i<nums.length){
            add(nums[i]);
            i++;
        }
    }

    public void minHeapify(){
        int[] nums = this.nums;
        int i = (int)Math.floor(nums.length/2)-1;
        while(i>=0){
            int left = (2*i)+1;
            int right = (2*i)+2;
            if(right>=nums.length){
                if(nums[left]<nums[i]){
                    int temp = nums[i];
                    nums[i] = nums[left];
                    nums[left] = temp;
                }
            }else{
                int smaller = nums[left]<nums[right]?left:right;
                if(nums[smaller]<nums[i]){
                    int temp = nums[i];
                    nums[i] = nums[smaller];
                    nums[smaller] = temp;
                }
            }
            i--;
        }
        this.nums = nums;
    }


    
    public int add(int val) {
        if(this.k<=this.nums.length-1){
            this.nums[this.k] = val;
            this.k+=1;
        }else if(this.nums[0]<val){
            this.nums[0] = val;
        }
        minHeapify();
        return this.nums[0];
    }
}
