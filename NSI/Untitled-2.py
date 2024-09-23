def count (n,v):
    cpt = 0
    for e  in v:
        if  e % n == 0:
            cpt += 1
    return cpt



def count (n, v):
    pass

def count (v1,v2):
    mults = []
    for n in v1:
        m = count (n,v2)
        mults.append (m)
    return  mults

