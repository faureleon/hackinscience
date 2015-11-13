T = "abcdefghijklmnopqrstuvwxyz"
for i in range(26):
    for j in range(26):
        if T[i] != T[j]:
            print(T[i]+T[j])
