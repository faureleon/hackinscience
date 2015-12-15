def check_my_city(city_name):
    S = 0
    l = []
    D = {}
    for i in range(len(velib)):
        if city_name == velib[i]['city']:
            S = S + 1
            l.append(velib[i]['zip'])
    if S > 0:
        D['station nb:'] = S
        D['zip_code:'] = l
        D['city'] = city_name
    else:
        D = "Sorry! No station for your city has been found!"
    return(D)

