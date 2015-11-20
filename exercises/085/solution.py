def sort_a_list(l):
    OK = False
    while OK == False:
        OK = True
        for i in range(len(l) - 1):
            if l[i] < l[i + 1]:
                K = l[i]
                l[i] = l[i + 1]
                l[i + 1] = K
                OK = False
    return(l)
def sort_by_mark(my_class):
    sorted(my_class, reverse=True)
    return(my_class)
from operator import itemgetter
def sort_by_name(my_class):
    getcount = itemgetter(1)
    return(sorted(my_class, key=getcount))
