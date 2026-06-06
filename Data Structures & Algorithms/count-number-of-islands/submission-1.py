class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        global ones_so_far 
        ones_so_far = 0
        islands = 0
        def BFS(start):
            queue = {tuple(start)}
            global ones_so_far
            while len(queue)!=0:
                pos = queue.pop()
                print("Current ",pos)
                grid[pos[0]][pos[1]] = "0"
                ones_so_far += 1
                if pos[0]!=0:
                    if grid[pos[0]-1][pos[1]] == "1":
                        queue.add(tuple([pos[0]-1,pos[1]]))
                        print("Added ",(pos[0]-1,pos[1]))
                if pos[0]!=len(grid)-1:
                    if grid[pos[0]+1][pos[1]] == "1":
                        queue.add(tuple([pos[0]+1,pos[1]]))
                        print("Added ",(pos[0]+1,pos[1]))
                if pos[1]!=0:
                    if grid[pos[0]][pos[1]-1] == "1":
                        queue.add(tuple([pos[0],pos[1]-1]))
                        print("Added ",(pos[0],pos[1]-1))
                if pos[1]!=len(grid[0])-1:
                    if grid[pos[0]][pos[1]+1] == "1":
                        queue.add(tuple([pos[0],pos[1]+1]))
                        print("Added ",(pos[0],pos[1]+1))
        def find_one():
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j]=="1":
                        return (i,j)
            return None
        def total_ones():
            cnt = 0
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j]=="1":
                        cnt+=1
            return cnt
        total = total_ones()
        print(total)
        while ones_so_far < total:
            pos = find_one()
            BFS(pos)
            islands += 1
            print("Islands: ",islands," ones so far ",ones_so_far)
        return islands


        