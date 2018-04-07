import sys

def read():
    file_name = sys.argv[1]
    fp = open(file_name)
    contents = fp.read()
    return contents

def getDamageWithoutSwap(damage, p):
    strenght = 1
    for j in p:
        if j == 'C':
            strenght = strenght * 2
        if j == 'S':
           damage = damage - strenght
    return damage

def getDamageSwaped(damage, p):
    only_s = True
    hacks = 0
    ll = list(p)
    total_damage = getDamageWithoutSwap(int(damage), p)
    if total_damage < 0:
        while(True):
            if  getDamageWithoutSwap(int(damage), ll) < 0 :
                for i in xrange(0, len( ll ) -1 ):
                    if ( ll[i].upper() == 'C' and ll[i + 1].upper() == 'S') :
                        tmp_letter = ll[i]
                        ll[i] = ll[i + 1]
                        ll[i + 1] = tmp_letter
                        hacks += 1
                        only_s = False
                if only_s:
                    return 'IMPOSSIBLE'
            else:
                break
    else: 
        return 0
    return hacks

def solution(x):
    br = x.split("\n")[1:]
    for i,row in enumerate(br,1):
        d = int(row.split(" ")[0])
        p = row.split(" ")[1]
        if not 1 <= d <= 10**9:
            continue
        if  not 2 <= len(p) <= 30:
            continue
        
        print("Case #{}: {}").format(i, getDamageSwaped(d, p))
    return 

content = read()
t = int(content[0])
if  1 <= t <= 100:
    solution(content[1:])

