import sys
def main():
    sorted_ = True
    while sorted_ == True:

        option = int(input(''' How would we help you?
        1: Show the list of available car for renting
        2: Press 2 to rent a car
        3: Press 3 if you want to return a rented car
        4: Press 4 if you want to leave: \n'''))
        if option == 1:
            import car
            car.car()
        elif option == 2:
            import rent
            rent.rent()


        elif option == 3:
            import giveback
            giveback.giveback()
        elif option == 4:
            sys.exit()
        else:
            print("Please enter valid option")
            main()
        option = input("Press Y to continue or any other key to exit:")
        if option == "Y":
            sorted_ = True
        else:
            sorted_ = False
            print("Thank you. We hope we could serve you again. Have a nice day.")
main()