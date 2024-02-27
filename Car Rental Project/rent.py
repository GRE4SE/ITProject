import sys


def rent():
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

    username = input("What would you like us to call you: ")

    file = open("%s %s.txt" %("Rented by ", username), "w")
    file.write("%s %s" %("Name: ", username))

    p = 0

    quantity = False
    while quantity == False:
        quan = False
        try:
            while quan == False:
                q = int(input("Enter the number of cars you want to rent: "))
                if q <= 0:
                    print("Please enter a valid command")
                else:
                    quan = True
            quantity = True
        except:
            print("Please enter a valid command")

    for i in range(1):
        car = 0
        name = False
        while name == False:
            carname = False
            try:
                while carname == False:
                    car = int(input("Which car you want to rent? Please specify id of the car: "))
                    if car <= 0 or car > 10:
                        print("Please choose again and choose valid number")
                    else:
                        carname = True
                name = True
            except:
                print("Please choose again and choose valid number")
                car = int(input("Which car you want to rent? Please specify id of the car"))

        if car == 1:
            p = p + 5000
            if q < sn_RS6:
                sn_RS6 = sn_RS6 - q
                print("Thank you for renting. I hope you will enjoy!")
                print("Total number of 'Audi RS6' remaining to rent is: ", sn_RS6)
                file.write("%s %s\n" %("\nCar rented is: ", l[0][0]))
                file.write("%s %d\n" %("Price per car: ", int(l[0][1])))
                file.write("%s %d\n" %("Total number of cars you rented: ", q))



            else:
                print("We are sorry to say that the total amount of cars available is: ", l[0][2])
                print("Let's start over.")
                Yes = input("If you want to borrow again, press Y for YES and any other keys for NO: ")
                if Yes == "Y":
                    rent()
                else:
                    sys.exit()



        elif car == 2:
            p = p + 2000
            if q < sn_W223:
                sn_W223 = sn_W223 - q
                print("Thank you for renting. I hope you will enjoy!")
                print("Total number of 'Mercedes S-class W223' remaining to rent is: ", sn_W223)
                file.write("%s %s\n" %("\nCar rented is: ", l[1][0]))
                file.write("%s %d\n" %("Price per car: ", int(l[1][1])))
                file.write("%s %d\n" %("Total number of cars you rented: ", q))



            else:
                print("We are sorry to say that the total amount of cars available is: ", l[0][2])
                print("Let's start over.")
                Yes = input("If you want to borrow again, press Y for YES and any other keys for NO: ")
                if Yes == "Y":
                    rent()
                else:
                    sys.exit()


        elif car == 3:
            p = p + 4000
            if q < sn_G:
                sn_G = sn_G - q
                print("Thank you for renting. I hope you will enjoy!")
                print("Total number of 'Mercedes G-class' remaining to rent is: ", sn_G)
                file.write("%s %s\n" %("\nCar rented is:", l[2][0]))
                file.write("%s %d\n" %("Price per car:", int(l[2][1])))
                file.write("%s %d\n" %("Total number of cars you rented: ", q))
            else:
                print("We are sorry to say that the total amount of cars available is: ", l[0][2])
                print("Let's start over.")
                Yes = input("If you want to borrow again, press Y for YES and any other keys for NO: ")
                if Yes == "Y":
                    rent()
                else:
                    sys.exit()



        elif car == 4:
            p = p + 5000
            if q < sn_M5:
                sn_M5 = sn_M5 - q
                print("Thank you for renting. I hope you will enjoy!")
                print("Total number of 'BMW M5' remaining to rent is: ", sn_M5)
                file.write("%s %s\n" %("\nCar rented is:", l[3][0]))
                file.write("%s %d\n" %("Price per car:", int(l[3][1])))
                file.write("%s %d\n" %("Total number of cars you rented: ", q))
            else:
                print("We are sorry to say that the total amount of cars available is: ", l[0][2])
                print("Let's start over.")
                Yes = input("If you want to borrow again, press Y for YES and any other keys for NO: ")
                if Yes == "Y":
                    rent()
                else:
                    sys.exit()



        elif car == 5:
            p = p + 4000
            if q < sn_P1:
                sn_P1 = sn_P1 - q
                print("Thank you for renting. I hope you will enjoy!")
                print("Total number of 'Mclaren P1' remaining to rent is: ", sn_P1)
                file.write("%s %s\n" %("\nCar rented is:", l[4][0]))
                file.write("%s %d\n" %("Price per car:", int(l[4][1])))
                file.write("%s %d\n" %("Total number of cars you rented: ", q))
            else:
                print("We are sorry to say that the total amount of cars available is: ", l[0][2])
                print("Let's start over.")
                Yes = input("If you want to borrow again, press Y for YES and any other keys for NO: ")
                if Yes == "Y":
                    rent()
                else:
                    sys.exit()



        elif car == 6:
            p = p + 4000
            if q < sn_918:
                sn_918 = sn_918 - q
                print("Thank you for renting. I hope you will enjoy!")
                print("Total number of 'Porsche 918 Spyder' remaining to rent is: ", sn_918)
                file.write("%s %s\n" %("\nCar rented is:", l[5][0]))
                file.write("%s %d\n" %("Price per car:", int(l[5][1])))
                file.write("%s %d\n" %("Total number of cars you rented: ", q))
            else:
                print("We are sorry to say that the total amount of cars available is: ", l[0][2])
                print("Let's start over.")
                Yes = input("If you want to borrow again, press Y for YES and any other keys for NO: ")
                if Yes == "Y":
                    rent()
                else:
                    sys.exit()



        elif car == 7:
            p = p + 4000
            if q < sn_M3:
                sn_M3 = sn_M3 - q
                print("Thank you for renting. I hope you will enjoy!")
                print("Total number of 'BMW M3' remaining to rent is: ", sn_M3)
                file.write("%s %s\n" %("\nCar rented is:", l[6][0]))
                file.write("%s %d\n" %("Price per car:", int(l[6][1])))
                file.write("%s %d\n" %("Total number of cars you rented: ", q))
            else:
                print("We are sorry to say that the total amount of cars available is: ", l[0][2])
                print("Let's start over.")
                Yes = input("If you want to borrow again, press Y for YES and any other keys for NO: ")
                if Yes == "Y":
                    rent()
                else:
                    sys.exit()



        elif car == 8:
            p = p + 3000
            if q < sn_EVOX:
                sn_EVOX = sn_EVOX - q
                print("Thank you for renting. I hope you will enjoy!")
                print("Total number of 'Mitsubishi Lancer EVO X' remaining to rent is: ", sn_EVOX)
                file.write("%s %s\n" %("\nCar rented is:", (l[7][0])))
                file.write("%s %d\n" %("Price per car:", int(l[7][1])))
                file.write("%s %d\n" %("Total number of cars you rented: ", q))
            else:
                print("We are sorry to say that the total amount of cars available is: ", l[0][2])
                print("Let's start over.")
                Yes = input("If you want to borrow again, press Y for YES and any other keys for NO: ")
                if Yes == "Y":
                    rent()
                else:
                    sys.exit()



        elif car == 9:
            p = p + 2000
            if q < sn_RX7:
                sn_RX7 = sn_RX7 - q
                print("Thank you for renting. I hope you will  enjoy!")
                print("Total number of 'Mazda RX7' remaining to rent is: ", sn_RX7)
                file.write("%s %s\n" %("\nCar rented is:", l[8][0]))
                file.write("%s %d\n" %("Price per car:", int(l[8][1])))
                file.write("%s %d\n" %("Total number of cars you rented: ", q))
            else:
                print("We are sorry to say that the total amount of cars available is: ", l[0][2])
                print("Let's start over.")
                Yes = input("If you want to borrow again, press Y for YES and any other keys for NO: ")
                if Yes == "Y":
                    rent()
                else:
                    sys.exit()



        elif car == 10:
            p = p + 4000
            if q < sn_R34:
                sn_R34 = sn_R34 - q
                print("Thank you for renting. I hope you will  enjoy!")
                print("Total number of 'Nissan Skyline GTR R34' remaining to rent is: ", sn_R34)
                file.write("%s %s\n" %("\nCar rented is:", l[9][0]))
                file.write("%s %d\n" %("Price per car:", int(l[9][1])))
                file.write("%s %d\n" %("Total number of cars you rented: ", q))
            else:
                print("We are sorry to say that the total amount of cars available is: ", l[0][2])
                print("Let's start over.")
                Yes = input("If you want to borrow again, press Y for YES and any other keys for NO: ")
                if Yes == "Y":
                    rent()
                else:
                    sys.exit()


        elif car == 11:
            p = p + 4000
            if q < sn_SUPRA:
                sn_SUPRA = sn_SUPRA - q
                print("Thank you for renting. I hope you will  enjoy!")
                print("Total number of 'Toyota Supra MK2' remaining to rent is: ", sn_SUPRA)
                file.write("%s %s\n" %("\nCar rented is:", l[10][0]))
                file.write("%s %d\n" %("Price per car:", int(l[10][1])))
                file.write("%s %d\n" %("Total number of cars you rented: ", q))
            else:
                print("We are sorry to say that the total amount of cars available is: ", l[0][2])
                print("Let's start over.")
                Yes = input("If you want to borrow again, press Y for YES and any other keys for NO: ")
                if Yes == "Y":
                    rent()
                else:
                    sys.exit()


        elif car < 1 or car > 11:
            print("Please choose again and choose valid number")
            car = int(input("Which car you want to rent? Please specify id of the car:"))

        file.write("%s %5.1f %s\n" %("Your total amount is :", q * p, "tenge"))
        from datetime import date
        file.write("%s" % ("Renting Date"))
        file.write(str(date.today()))
        file.close()

    print("************************************************************************************************")

    file = open("%s %s.txt" % ("Rented by ", username), "r")
    for line in file:
        print(line)
    print("************************************************************************************************")

    again = open("movielist.txt", "w")
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


rent()