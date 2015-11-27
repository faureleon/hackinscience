def love_meet(bob, alice):
    A = set(alice)
    B = set(bob)
    b = set(A).intersection(B)
    return(b)


def affair_meet(alice, bob, sylvester):
    A = set(alice)
    B = set(bob)
    S = set(silvester)
    b = set(A).intersection(B)
    c = set(A).intersection(S)
    d = [val for val in b if val not in c]
    D = set(d)
    return(D)
