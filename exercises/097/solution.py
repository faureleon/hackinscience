def love_meet(bob, alice):
    A = set(alice)
    B = set(bob)
    b = set(A).intersection(B)
    return(b)


def affair_meet(bob, alice, sylvester):
    A = set(alice)
    B = set(bob)
    S = set(silvester)
    b = set(A).intersection(S)
    d = [val for val in b if val not in B]
    D = set(d)
    return(D)
