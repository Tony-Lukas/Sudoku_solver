def snail(R=9,C=9):
    r,c = R//2,C//2
    d = 0# R:0  D:1 L:2 U:3
    step = 1
    #matrix = [[-1]*C for _ in range(R)]
    #num = 0
    step_count = 0
    
    for _ in range(R*C):
        #print(f"{num} ({r},{c}), direction {d} ,step {step} step_count {step_count}")
        #matrix[r][c] = num
        yield r,c,d
        #num +=1
        step_count +=1
        if d == 0:
            c += 1
        elif d==1:
            r += 1
        elif d==2:
            c -= 1
        elif d == 3:
            r -= 1
        # change direction
        if step_count == step:
            step_count = 0
            if d == 1 or d == 3:
                step +=1
            d =(d+1)%4 
    #return matrix

if __name__ == '__main__':
    #matrix = snail(5,5)
    #for row in matrix:
    #    print(" ".join(map(str,row)))
    for i,(r,c,d) in enumerate(snail()):
        print(i,r,c,d)
