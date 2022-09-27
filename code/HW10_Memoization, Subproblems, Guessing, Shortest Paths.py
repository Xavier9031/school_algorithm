def Fib(n):
    F = [0, 1]
    for i in range(2, n+1):
        F.append(F[-1] + F[-2])
    return F[-1]

while True:
    try:
        x = input()
        x = int(x)
        print(Fib(x))
    except:
        break