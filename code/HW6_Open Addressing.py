def hash1(k):
    return k % 13
def hash2(k):
    return 1 + k//13 % (12)

def hash0(k, i):
    return (hash1(k) + i * hash2(k)) % 13

while True:
    try:
        table = ["no","no","no","no","no","no","no","no","no","no","no","no","no"]
        x = input()
        if(x == ""):
            break
        arr_x = x.split(",")
        arr_x = list(map(int, arr_x))
        npos = 0
        flag = False
        for n in arr_x:
            if(flag):
                break
            pos = hash0(n, 0)
            npos = pos
            if(table[pos] == "no"):
                table[pos] = n
            else:
                for i in range(1,13):
                    pos = hash0(n, i)
                    if(table[pos] == "no"):
                        table[pos] = n
                        break
                    if(i == 12):
                        flag = True
                        break
                print("Collision has occurred for element " + str(n) +" at position "+ str(npos)+" finding new Position at position "+ str(pos))
        print("Done")
        
    except:
        break