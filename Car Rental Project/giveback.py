import sys


def giveback():
    file = open("carlist.txt", "r")
    l = []
    for line in file:
        line = line.replace("\n", "")
        a = line.split(",")
        l.append(a)
    sn_RS6 = int(l[0][2])
    sn_W223 = int(l[1][1])
    sn_G = int(l[2][2])
    sn_M5 = int(l[3][1])
    sn_P1 = int(l[4][1])
    sn_918 = int(l[5][1])
    sn_M3 = int(l[6][1])
    sn_EVOX = int(l[7][1])
    sn_RX7 = int(l[8][1])
    sn_R34 = int(l[9][1])
    sn_SUPRA = int(l[10][1])

    username = input("Can I know your name again: ")

    file = open("%s %s.txt" %("Returned by ", username), "w")
    file.write("%s %s\n" %("Name: ", username))

    p = 0
    f = 0

    quantity = False
    while quantity == False:
        quan = False
        try:
            while quan == False:
                q = int(input("Enter the number of cars you want to return: "))
                if q <= 0:
                    print("Please enter a valid number")
                else:
                    quan = True
            quantity = True
        except:
            print("Please enter a valid number")

    for i in range(1):
        car = 0
        name = False
        while name == False:
            carname = False
            try:
                while carname == False:
                    car = int(input("Which car you want to return? Please specify an id of a car:"))
                    if car <= 0 or car > 10:
                        print("Please choose again and choose valid number")
                    else:
                        carname = True
                name = True
            except:
                print("Please choose again and choose valid number")
                car = int(input("Which car you want to return? Please specify an id of a car:"))
        if car == 1:
            time = int(input("How many days did you enjoy this car:"))

            if sn_RS6 < 31 and q < (31 - (sn_RS6)):
                sn_RS6 = sn_RS6 + q
                if time <= 10:
                    print("Thank you for returning this car!")
                    print("Number of Audi RS6 available are:", sn_RS6)
                    file.write("%s\n" %("Car Returned: Audi RS6"))
                    file.write("%s\n" %("Thank you for returning this car. We will be grateful to see you again"))

                if time > 10:
                    p = time - 10
                    print("Thank you for returning this car, but you are late so you will be fined.")
                    print("Number of Audi RS6 available are:", sn_RS6)
                    file.write("%s\n" %("Car Returned: Audi RS6"))
                    file.write("%s %5.0f %s\n" %("You are late, your fine is:", p, "tenge"))
                f = f + p


            else:
                print("I think you have mistaken other cars with Audi RS6 because all", l[0][0],
                      "cars are already present in our store. Thank you!")
                print("Let's start over.")
                Yes = input("If you want to borrow again, press Y for YES and N for No: ")
                if Yes == "Y":
                    giveback()
                elif Yes == "N":
                    sys.exit()

        if car == 2:
            time = int(input("How many days did you enjoy this car:"))

            if sn_W223 < 26 and q < (26 - (sn_W223)):
                sn_W223 = sn_W223 + q
                if time <= 10:
                    print("Thank you for returning this car!")
                    print("Number of Mercedes S-class W223 available are:", sn_W223)
                    file.write("%s\n" %("Car Returned: Mercedes S-class W223"))
                    file.write("%s\n" %("Thank you for returning this car. We will be grateful to see you again"))

                if time > 10:
                    p = time - 10
                    print("Thank you for returning this car, but you are late so you will be fined.")
                    print("Number of Mercedes S-class W223 available are:", sn_W223)
                    file.write("%s\n" %("Car Returned: Mercedes S-class W223"))
                    file.write("%s %5.0f %s\n" %("You are late, your fine is:", p, "tenge"))
                f = f + p


            else:
                print("I think you have mistaken other car with Mercedes S-class W223 because all", l[1][0],
                      "cars are already present in our store. Thank you!")
                print("Let's start over.")
                Yes = input("If you want to borrow again, press Y for YES and N for No: ")
                if Yes == "Y":
                    giveback()
                elif Yes == "N":
                    sys.exit()

        if car == 3:
            time = int(input("How many days did you enjoy this car:"))

            if sn_G < 23 and q < (23 - (sn_G)):
                sn_G = sn_G + q
                if time <= 10:
                    print("Thank you for returning this car!")
                    print("Number of 'Mercedes G-class' available are:", sn_G)
                    file.write("%s\n" %("Car Returned: Mercedes G-class"))
                    file.write("%s\n" %("Thank you for returning this car. We will be grateful to see you again"))

                if time > 10:
                    p = time - 10
                    print("Thank you for returning this car, but you are late so you will be fined.")
                    print("Number of Mercedes G-class available are:", sn_G)
                    file.write("%s\n" %("Car Returned: Mercedes G-class"))
                    file.write("%s %5.0f %s\n" %("You are late, your fine is:", p, "tenge"))
                f = f + p


            else:
                print("I think you have mistaken other car with Mercedes G-class because all", l[2][0],
                      "cars are already present in our store. Thank you!")
                print("Let's start over.")
                Yes = input("If you want to borrow again, press Y for YES and N for No: ")
                if Yes == "Y":
                    giveback()
                elif Yes == "N":
                    sys.exit()

        if car == 4:
            time = int(input("How many days did you enjoy this car:"))

            if sn_M5 < 17 and q < (17 - (sn_M5)):
                sn_M5 = sn_M5 + q
                if time <= 10:
                    print("Thank you for returning this car!")
                    print("Number of BMW M5 available are:", sn_M5)
                    file.write("%s\n" %("Car Returned: BMW M5"))
                    file.write("%s\n" %("Thank you for returning this car. We will be grateful to see you again"))

                if time > 10:
                    p = time - 10
                    print("Thank you for returning this car, but you are late so you will be fined.")
                    print("Number of BMW M5 available are:", sn_M5)
                    file.write("%s\n" %("Car Returned: BMW M5"))
                    file.write("%s %5.0f %s\n" %("You are late, your fine is:", p, "tenge"))
                f = f + p


            else:
                print("I think you have mistaken other car with BMW M5 because all", l[3][0],
                      "cars are already present in our store. Thank you!")
                print("Let's start over.")
                Yes = input("If you want to borrow again, press Y for YES and N for No: ")
                if Yes == "Y":
                    giveback()
                elif Yes == "N":
                    sys.exit()

        if car == 5:
            time = int(input("How many days did you enjoy this car:"))

            if sn_P1 < 36 and q < (36 - (sn_P1)):
                sn_P1 = sn_P1 + q
                if time <= 10:
                    print("Thank you for returning this car!")
                    print("Number of Mclaren P1 available are:", sn_P1)
                    file.write("%s\n" %("Car Returned: Mclaren P1"))
                    file.write("%s\n" %("Thank you for returning this car. We will be grateful to see you again"))

                if time > 10:
                    p = time - 10
                    print("Thank you for returning this car, but you are late so you will be fined.")
                    print("Number of Mclaren P1 available are:", sn_P1)
                    file.write("%s\n" %("Car Returned: Mclaren P1"))
                    file.write("%s %5.0f %s\n" %("You are late, your fine is:", p, "tenge"))
                f = f + p


            else:
                print("I think you have mistaken other car with Mclaren P1 because all", l[4][0],
                      "cars are already present in our store. Thank you!")
                print("Let's start over.")
                Yes = input("If you want to borrow again, press Y for YES and N for No: ")
                if Yes == "Y":
                    giveback()
                elif Yes == "N":
                    sys.exit()

        if car == 6:
            time = int(input("How many days did you enjoy this car:"))

            if sn_918 < 16 and q < (16 - (sn_918)):
                sn_918 = sn_918 + q
                if time <= 10:
                    print("Thank you for returning this car!")
                    print("Number of Porsche 918 Spyder available are:", sn_918)
                    file.write("%s\n" %("Car Returned: Porsche 918 Spyder"))
                    file.write("%s\n" %("Thank you for returning this car. We will be grateful to see you again"))

                if time > 10:
                    p = time - 10
                    print("Thank you for returning this car, but you are late so you will be fined.")
                    print("Number of Porsche 918 Spyder available are:", sn_918)
                    file.write("%s\n" %("Car Returned: Porsche 918 Spyder"))
                    file.write("%s %5.0f %s\n" %("You are late, your fine is:", p, "tenge"))
                f = f + p


            else:
                print("I think you have mistaken other car with Porsche 918 Spyder because all", l[5][0],
                      "cars are already present in our store. Thank you!")
                print("Let's start over.")
                Yes = input("If you want to borrow again, press Y for YES and N for No: ")
                if Yes == "Y":
                    giveback()
                elif Yes == "N":
                    sys.exit()

        if car == 7:
            time = int(input("How many days did you enjoy this car:"))
            p = time - 10
            if sn_M3 < 20 and q < (20 - (sn_M3)):
                sn_M3 = sn_M3 + q
                if time <= 10:
                    print("Thank you for returning this car!")
                    print("Number of BMW M3 available are:", sn_M3)
                    file.write("%s\n" %("Car Returned: BMW M3"))
                    file.write("%s\n" %("Thank you for returning this car. We will be grateful to see you again"))

                if time > 10:
                    p = time - 10
                    print("Thank you for returning this car, but you are late so you will be fined.")
                    print("Number of BMW M3 available are:", sn_M3)
                    file.write("%s\n" %("Car Returned: BMW M3"))
                    file.write("%s %5.0f %s\n" %("You are late, your fine is:", p, "tenge"))
                f = f + p


            else:
                print("I think you have mistaken other car with BMW M3 because all", l[6][0],
                      "cars are already present in our store. Thank you!")
                Yes = input("If you want to return any other car, press Y for YES and N for No: ")
                if Yes == "Y":
                    giveback()


                elif Yes == "N":
                    sys.exit()

        if car == 8:
            time = int(input("How many days did you enjoy this car:"))
            p = time - 10
            if sn_EVOX < 14 and q < (14 - (sn_EVOX)):
                sn_EVOX = sn_EVOX + q
                if time <= 10:
                    print("Thank you for returning this car!")
                    print("Number of Mitsubishi Lancer EVO X available are:", sn_EVOX)
                    file.write("%s\n" %("Car Returned: Mitsubishi Lancer EVO X"))
                    file.write("%s\n" %("Thank you for returning this car. We will be grateful to see you again"))

                if time > 10:
                    p = time - 10
                    print("Thank you for returning this car, but you are late so you will be fined.")
                    print("Number of Mitsubishi Lancer EVO X available are:", sn_EVOX)
                    file.write("%s\n" %("Car Returned: Mitsubishi Lancer EVO X"))
                    file.write("%s %5.0f %s\n" %("You are late, your fine is:", p, "tenge"))
                f = f + p


            else:
                print("I think you have mistaken other car with Mitsubishi Lancer EVO X because all", l[7][0],
                      "cars are already present in our store. Thank you!")
                Yes = input("If you want to return any other car, press Y for YES and N for No: ")
                if Yes == "Y":
                    giveback()


                elif Yes == "N":
                    sys.exit()

        if car == 9:
            time = int(input("How many days did you enjoy this car:"))
            p = time - 10
            if sn_RX7 < 10 and q < (10 - (sn_RX7)):
                sn_RX7 = sn_RX7 + q
                if time <= 10:
                    print("Thank you for returning this car!")
                    print("Number of Mazda RX7 available are:", sn_RX7)
                    file.write("%s\n" %("Car Returned: Mazda RX7"))
                    file.write("%s\n" %("Thank you for returning this car. We will be grateful to see you again"))

                if time > 10:
                    p = time - 10
                    print("Thank you for returning this car, but you are late so you will be fined.")
                    print("Number of Mazda RX7 available are:", sn_RX7)
                    file.write("%s\n" %("Car Returned: Mazda RX7"))
                    file.write("%s %5.0f %s\n" %("You are late, your fine is:", p, "tenge"))
                f = f + p


            else:
                print("I think you have mistaken other car with Mazda RX7 because all", l[8][0],
                      "cars are already present in our store. Thank you!")
                print("Let's start over.")
                Yes = input("If you want to borrow again, press Y for YES and N for No: ")
                if Yes == "Y":
                    giveback()
                elif Yes == "N":
                    sys.exit()

        if car == 10:
            time = int(input("How many days did you enjoy car:"))
            p = time - 10
            if sn_R34 < 16 and q < (16 - (sn_R34)):
                sn_R34 = sn_R34 + q
                if time <= 10:
                    print("Thank you for returning this car!")
                    print("Number of Nissan Skyline GTR R34 available are:", sn_R34)
                    file.write("%s\n" %("Car Returned: Nissan Skyline GTR R34"))
                    file.write("%s\n" %("Thank you for returning this car. We will be grateful to see you again"))

                if time > 10:
                    p = time - 10
                    print("Thank you for returning this car, but you are late so you will be fined.")
                    print("Number of Nissan Skyline GTR R34 available are:", sn_R34)
                    file.write("%s\n" %("Car Returned: Nissan Skyline GTR R34"))
                    file.write("%s %5.0f %s\n" %("You are late, your fine is:", p, "tenge"))
                f = f + p


            else:
                print("I think you have mistaken other car with Nissan Skyline GTR R34 because all", l[9][0],
                      "cars are already present in our store. Thank you!")
                print("Let's start over.")
                Yes = input("If you want to borrow again, press Y for YES and N for No: ")
                if Yes == "Y":
                    giveback()
                elif Yes == "N":
                    sys.exit()

        if car == 11:
            time = int(input("How many days did you enjoy this car:"))
            p = time - 10
            if sn_SUPRA < 15 and q < (15 - (sn_SUPRA)):
                sn_SUPRA = sn_SUPRA + q
                if time <= 10:
                    print("Thank you for returning this car!")
                    print("Number of Toyota Supra Mk2 available are:", sn_SUPRA)
                    file.write("%s\n" %("Car Returned: Toyota Supra Mk2"))
                    file.write("%s\n" %("Thank you for returning this car. We will be grateful to see you again"))

                if time > 10:
                    p = time - 10
                    print("Thank you for returning this car, but you are late so you will be fined.")
                    print("Number of Toyota Supra Mk2 available are:", sn_SUPRA)
                    file.write("%s\n" %("Car Returned: Toyota Supra Mk2"))
                    file.write("%s %5.0f %s\n" %("You are late, your fine is:", p, "tenge"))
                f = f + p


            else:
                print("I think you have mistaken other car with Toyota Supra Mk2 because all", l[10][0],
                      "cars are already present in our store. Thank you!")
                Yes = input("If you want to return any other car, press Y for YES and N for No: ")
                if Yes == "Y":
                    giveback()


                elif Yes == "N":
                    sys.exit()








        elif car < 1 or car > 11:
            print("Please choose again and choose valid number")
            car = int(input("Which movie you want to return? Please specify SN of the movie:"))

        file.write("%s %5.1f %s\n" %("Your total fine is :", f, "tenge"))
        from datetime import date
        file.write("%s" %("Returning Date"))
        file.write(str(date.today()))
        file.close()

    print("************************************************************************************************")

    file = open("%s %s.txt" % ("Returned by ", username), "r")
    for line in file:
        print(line)
    print("************************************************************************************************")

    again = open("carlist.txt", "w")
    again.write("%s %s %s %d\n" %("Audi RS6,                ", "5", ", ", sn_RS6))
    again.write("%s %s %s %d\n" %("Mercedes S-class W223,        ", "2", ", ", sn_W223))
    again.write("%s %s %s %d\n" %("Mercedes G-class,                ", "4", ", ", sn_G))
    again.write("%s %s %s %d\n" %("BMW M5,        ", "5", ", ", sn_M5))
    again.write("%s %s %s %d\n" %("Mclaren P1,        ", "4", ", ", sn_P1))
    again.write("%s %s %s %d\n" %("Porsche 918 Spyder,                ", "3", ", ", sn_918))
    again.write("%s %s %s %d\n" %("BMW M3,                        ", "4", ", ", sn_M3))
    again.write("%s %s %s %d\n" %("Mitsubishi Lancer EVO X,        ", "3", ", ", sn_EVOX))
    again.write("%s %s %s %d\n" %("Mazda RX7,                ", "2", ", ", sn_RX7))
    again.write("%s %s %s %d\n" %("Nissan Skyline GTR R34,", "4", ", ", sn_R34))
    again.write("%s %s %s %d\n" %("Toyota Supra Mk2,                ", "4", ", ", sn_SUPRA))

    file.close()


giveback()
