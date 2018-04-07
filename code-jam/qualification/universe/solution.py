import fileinput, sys
from time import sleep

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

def solution(t):
    for i in range(0, t ):
        content = f.readline().strip()
        d = int(content.split(' ')[0])
        p = content.split(' ')[1]
        if not 1 <= d <= 10**9:
            continue
        if  not 2 <= len(p) <= 30:
            continue
        print("Case #{}: {}").format(i+1, getDamageSwaped(d, p))
    return sys.exit()

f = fileinput.input()
t = int(f.readline())
if  1 <= t <= 100:
    solution(t)

