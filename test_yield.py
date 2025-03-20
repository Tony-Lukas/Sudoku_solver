def gen(n):
    d = 0
    for i in range(n*n):
        yield i,d
        d = (d+1)%4
for i,d in gen(3):
    print(i,d)
