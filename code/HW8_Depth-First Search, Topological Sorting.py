import sys

def dfs(start_x,start_y,end_x,end_y,migong_array):
    next_step = [ [0,-1],[-1,0], [1,0], [0,1]]

    if (start_x == end_x and start_y == end_y):
        global flag
        flag = True
        print(W*start_x + start_y, end="")
        return
    print(W*start_x + start_y, end=" ")
    for i in range(len(next_step)):
        next_x = start_x + next_step[i][0]
        next_y = start_y + next_step[i][1]
        # if(next_x < 0 or next_y < 0 or next_x > len(migong_array) or next_y > len(migong_array[0])):
        #     continue
        if((migong_array[next_x][next_y] == ' ' or migong_array[next_x][next_y] == 'T') and book[next_x][next_y] == 0):
            book[next_x][next_y] = 1
            dfs(next_x,next_y,end_x,end_y,migong_array)
            if(flag):
                return
            # book[next_x][next_y] = 0
    return

MazeString = sys.stdin.read()
book = [[0 for col in range(100)] for row in range(100)]#標記數組
flag = False
line = MazeString.split('\n')
H = len(line) - 1
W = len(line[0])
# print("W:"+str(W))
# print("H:"+str(H))
Maze = []
S_x = 0
S_y = 0
T_x = 0
T_y = 0
line.pop()
for i in range(H):
    temp_str = line[i]
    temp= []
    for j in range(W):
        if(temp_str[j] == "S"):
            S_x = i
            S_y = j
        if(temp_str[j] == "T"):
            T_x = i
            T_y = j
        temp.append(temp_str[j])
    Maze.append(temp)

book[S_x][S_y] = 1
dfs(S_x,S_y,T_x,T_y,Maze)