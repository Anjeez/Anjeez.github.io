import sys
TAPELEN = 177013

tape = [0 for i in range(TAPELEN)]

def crazy(a, b):
    (a_sub, b_sub) = (a, b)
    dig = 1
    crazy = 0
    for k in range(0, 10):
        (dig_a, dig_b) = (a_sub % 3, b_sub % 3)
        if dig_a == 2:
            crazy += [0,2,1][dig_b] * dig
        else:
            if dig_b == 2:
                crazy += 2 * dig
            else:
                crazy += (not dig_a) * dig
        dig *= 3
        (a_sub, b_sub) = (a_sub // 3, b_sub // 3)
    return crazy

def crypto(x,y):
    i = 0
    while (i*59051 + y) % x != 0:
        i+=1
    if (i*59051 + y) // x >= 59049:
        return 0
    return (i*59051 + y) // x

def dream(code,inp):
    i=list(inp)
    r = 0
    p = 0
    m = 0
    while r < len(code):
        if code[r].lower()=='a':
            tape[p] += m
            tape[p] = tape[p] % 59049
            m = 0
        elif code[r].lower()=='s':
            p-=1
            if p < 0:
                p = 0
        elif code[r].lower()=='d':
            p+=1
            if p >= TAPELEN:
                p = TAPELEN - 1
        elif code[r].lower()=='f':
            tape[p] = m
            m = 0
        elif code[r].lower()=='g':
            tape[p] = ord(i.pop(0))
        elif code[r].lower()=='h':
            tape[p] = crypto(m,tape[p])
            m = 0
        elif code[r].lower()=='j':
            m = tape[p]
        elif code[r].lower()=='k':
            tape[p] = crazy(tape[p],m)
            m = 0
        elif code[r].lower()=='l':
            sys.stdout.write(chr(tape[p]))
        elif code[r].lower()==';':
            if tape[p]==0:
                r-=(m+1)
        r+=1

if __name__ == '__main__':
    with open(sys.argv[1], 'rt') as f:
        code = f.read()
    if len(sys.argv) > 2:
        dream(code,sys.argv[2])
    else:
        dream(code,"")
