def left(index):
    return 2*index

def right(index):
    return 2*index+1

def max_heapfy(arr, i):
    if(i > (len(arr)-1)/2):
        return arr
    
    if(right(i) > (len(arr)-1)):
        max_id = left(i)
    elif(arr[left(i)] > arr[right(i)]):
        max_id = left(i)
    else:
        max_id = right(i)
            
    if(arr[i] > arr[max_id]):
        return arr
    else:
        arr[i], arr[max_id] = arr[max_id], arr[i]
        return max_heapfy(arr, max_id)

def build_max_heap(arr):
    arr.insert(0, 0)
    for i in range(int((len(arr)-1)/2),0,-1):
        arr = max_heapfy(arr, i)
    arr.pop(0)
    return arr

def print_arr(arr_x):
    print("The array representation of the heap is [", end = "")
    for i in range(0,len(arr_x)-1):
        print(arr_x[i], end = " ")
    print(arr_x[len(arr_x)-1], end = "")
    print("]")
    
while True:
    try:
        x = input()
        arr_x = x.split(",")
        arr_x = list(map(int, arr_x))
        arr_x = build_max_heap(arr_x)
        print_arr(arr_x)
    except:
        break