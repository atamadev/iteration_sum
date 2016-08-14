x = []
while True:
    a = input('Input : ')
    n = range (1,a+1,1)
    y = len(n)
    z = len(x)
    if y > z:
        x[z:y] = [0]*(y-z)
    x[:y] = [x[i]+n[i] for i in range(len(n)) ]
    print x
