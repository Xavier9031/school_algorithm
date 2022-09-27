def search(txt, pat, m, a):
    txt_len = len(txt)
    pat_len = len(pat)
    h = pow(m,pat_len-1)%a
    p = 0
    t = 0
    result = []
    for i in range(pat_len): 
        p = (m*p+ord(pat[i]))%a
        t = (m*t+ord(txt[i]))%a
    for s in range(txt_len-pat_len+1): 
        if p == t: 
            match = True
            for i in range(pat_len):
                if pat[i] != txt[s+i]:
                    match = False
                    break
            if match:
                result = result + [s]
        if s < txt_len-pat_len:
            t = (t-h*ord(txt[s]))%a 
            t = (t*m+ord(txt[s+pat_len]))%a 
            t = (t+a)%a 
    return result

while True:
    try:
        x = input()
        if(x == ""):
            break
        arr_x = x.split(",")
        ans = search(arr_x[0], arr_x[1], int(arr_x[2]), int(arr_x[3]))
        for i in ans:
            print("Pattern found at index " + str(i))
        print("Done")
        
    except:
        break