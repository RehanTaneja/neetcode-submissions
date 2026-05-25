class MinStack {
    private int[] stack;
    private int size;
    private int min;

    public MinStack() {
        this.stack = new int[10];
        this.size = 0;
        this.min = -1;
    }
    
    public void push(int val) {
        if(this.size>=this.stack.length){
            int[] n = new int[this.stack.length*2];
            for(int i = 0;i<this.size;i++){
                n[i] = this.stack[i];
            }
            this.stack = n;
        }
        this.stack[this.size] = val;
        if(this.min==-1 || val<this.stack[this.min]){
            this.min = this.size;
        }
        this.size++;

    }
    
    public void pop() {
        this.size--;
    }
    
    public int top() {
        return this.stack[this.size-1];
    }
    
    public int getMin() {
        if(this.min>=this.size){
            this.min = 0;
            for(int i = 1;i<this.size;i++){
                if(this.stack[i]<this.min){
                    this.min = i;
                }
            }
        }
        return this.stack[this.min];
    }
}
