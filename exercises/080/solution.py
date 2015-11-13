T = "abcdefghijklmnopqrstuvwxyz"
for i in range(26):
    for j in range(i, 26):
        if T[i] != T[j]:
            print(T[i]+T[j])
