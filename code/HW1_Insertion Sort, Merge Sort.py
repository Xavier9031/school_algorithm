def findpeak_1(arr, n, start , end):
    mid = int(end + (start - end)/2)

    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
        (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return arr[mid]
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return findpeak_1(arr, n, start, (mid - 1))
    else:
        return findpeak_1(arr, n, (mid + 1), end)

while True:
    try:
        _inlist = []
        _inlist = list(map(int, input().split(",")))
        lenth = len(_inlist)
        print("Find it! The peak element is "+str(findpeak_1(_inlist, lenth, 0, lenth-1)))
    except:
        break