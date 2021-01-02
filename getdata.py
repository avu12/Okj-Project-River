
def min_river(filename):
    folyok = []
    try:
        f = open(filename,"r")
    except OSError as e:
        print(e)
        return -1
   
    for sor in f:
        sor = sor[:-1].split(";")
        sor[1] = int(sor[1])
        folyok.append(sor)
    f.close()

    if len(folyok) == 0 :
        print("Empty file!")
        return 0

    min_name = folyok[0][0]
    min_value = folyok[0][1]
    for f in folyok:
        if f[1] < min_value:
            min_value = f[1]
            min_name  = f[0]

    print("Minimum river name and value:\n" + min_name+ " " + str(min_value) )



def max_river(filename):
    folyok = []
    try:
        f = open(filename,"r")
    except OSError as e:
        print(e)
        return -1
   
    for sor in f:
        sor = sor[:-1].split(";")
        sor[1] = int(sor[1])
        folyok.append(sor)
    f.close()

    if len(folyok) == 0 :
        print("Empty file!")
        return 0

    max_name = folyok[0][0]
    max_value = folyok[0][1]
    for f in folyok:
        if f[1] > max_value:
            max_value = f[1]
            max_name  = f[0]

    print("Maximum river name and value:\n" + max_name+ " " + str(max_value) )



def avg_river(filename):
    folyok = []
    try:
        f = open(filename,"r")
    except OSError as e:
        print(e)
        return -1
   
    for sor in f:
        sor = sor[:-1].split(";")
        sor[1] = int(sor[1])
        folyok.append(sor)
    f.close()

    if len(folyok) == 0 :
        print("Empty file!")
        return 0

    atlag = 0
    osszeg = 0
    for f in folyok:
        osszeg = osszeg + f[1]
    atlag = osszeg / len(folyok)
    print("Average river value:\n" + str(atlag) )
    

#TODO
def river_exist(filename,rivername):
    pass

#TODO
def print_all_data(filename):
    pass
