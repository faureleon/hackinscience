station = {
    'address': 'RUE DES CHAMPEAUX (PRES DE LA GARE ROUTIERE) - 93170 BAGNOLET',
    'number': 31705,
    'latitude': 48.8645278209514,
    'name': 'CHAMPEAUX (BAGNOLET)',
    'longitude': 2.416170724425901
}
H = list(station.keys())
L = list(station.values())
T = len(H)
S = len(L)
for i in range(S):
    print(H[i], L[i])
