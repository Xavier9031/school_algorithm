from collections import deque 
def k_move(_x, _y, x, y):
        Dir = [(-2, -1), (-2, 1), (-1, 2), (1, 2),(2, 1), (2, -1), (1, -2), (-1, -2)]
        q = deque()
        q.append((_x, _y))
        d_dict = {(_x, _y): 0}
        while q:
            i, j = q.popleft()
            if (i, j) == (x, y):
                return d_dict[(i, j)]
            for dx, dy in Dir:
                next_i, next_j = i + dx, j + dy
                if (next_i, next_j) in d_dict:
                    continue
                q.append((next_i, next_j))
                d_dict[(next_i, next_j)] = d_dict[(i, j)] + 1
                
        return -1

while True:
    try:
        x = input()
        if(x == ""):
            break
        arr_x = x.split(",")
        arr_x = list(map(int, arr_x))
        print("To get from Point( "+str(arr_x[0])+" , "+str(arr_x[1])+" ) to Point( "+str(arr_x[2])+" , "+str(arr_x[3])+" ) takes "+str(k_move(arr_x[0], arr_x[1], arr_x[2], arr_x[3]))+" knight moves.")
        
    except:
        break