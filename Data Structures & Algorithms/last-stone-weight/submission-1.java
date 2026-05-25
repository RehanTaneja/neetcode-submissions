class Solution {
    public int[] stones;
    public int last;
    public int lastStoneWeight(int[] stones) {
        if(stones.length==1){
            return stones[0];
        }
        this.stones = stones;
        this.last = this.stones.length-1;
        while(this.last>0){
            this.last = smash();
        }
        return this.stones[0];
    }
    public int smash(){
        if(this.last==1){
            this.stones[0] = Math.abs(this.stones[0]-this.stones[1]);
            return this.last - 1;
        }
        int i = (int)Math.floor((this.last+1)/2)-1;
        while(i>=0){
            int left = (2*i)+1;
            int right = (2*i)+2;
            int bigger;
            if(right>=this.last+1){
                bigger = left;
            }else{
                bigger = this.stones[left]>this.stones[right]?left:right;
            }
            if(this.stones[bigger]>this.stones[i]){
                    int temp = this.stones[i];
                    this.stones[i] = this.stones[bigger];
                    this.stones[bigger] = temp;
            }
            i--;
        }
        i = (int)Math.floor((this.last)/2);
        while(i>=1){
            int left = (2*i);
            int right = (2*i)+1;
            int bigger;
            if(right>=this.last+1){
                bigger = left;
            }else{
                bigger = this.stones[left]>this.stones[right]?left:right;
            }
            if(this.stones[bigger]>this.stones[i]){
                    int temp = this.stones[i];
                    this.stones[i] = this.stones[bigger];
                    this.stones[bigger] = temp;
            }
            i--;
        }
        this.stones[1] = this.stones[0]-this.stones[1];
        this.stones[0] = this.stones[this.last];
        return this.last - 1;
    }
}
