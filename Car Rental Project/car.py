def car():
    sn = 1
    l = []
    print("Hello!\nWe have following cars available for you to rent:\n ")
    print("************************************************************************************")
    print("S/N       Movies             Rental Charge(in tenge)           Available quantity")
    print("____________________________________________________________________________________")

    file = open("carlist.txt", "r")

    for line in file:
        line = line.replace("\sn", "")
        line = line.replace(",", "\t\t")
        print("", sn, "\t" + line)
        line = line.replace("\t\t", ",")
        b = line.split(",")
        l.append(b)
        sn = sn + 1
    print("____________________________________________________________________________________\n")