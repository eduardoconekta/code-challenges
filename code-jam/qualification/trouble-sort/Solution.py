import fileinput, sys

def check_order(n, arr):
    result = False
    for i in xrange(0, n - 1):
        if arr[i] > arr[i + 1]:
            result = True

    return result

def sort(n,v):
    sort_tries = 0
    done = False
    while not done:
        done = True
        for i in xrange(0,n -2):
            if v[ i ] > v[ i + 2 ]:
                done = False
                v[ i : i + 3 ]  = v[ i : i + 3 ][ ::-1 ]
                sort_tries += 1
    if check_order(n,v):
        return sort_tries
    else:
        return "OK"

def solution(t):
    for i in xrange(1, t +1 ):
        N = int(f.readline().strip())
        V = f.readline().strip().split(' ')
        print "Case #{} {}".format(i,sort(N,V))
    return

f = fileinput.input()
t = int(f.readline())
if  1 <= t <= 100:
    solution(t)
else:
    print >>sys.stderr