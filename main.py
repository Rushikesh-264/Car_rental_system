# PROGRAM TO CREATE A CAR RENTAL MANAGEMENT SYSTEM

import sqlite3
from datetime import date

connect = sqlite3.connect("Car_rental_database.db")             # Opens a connection to the Car_rental_database


# connect.execute('''Create table Cars_info (Car_id INT (100,1) PRIMARY KEY, Car_no VARCHAR(9),
# Car_name VARCHAR(15), Seats_capacity VARCHAR(8), luggage_capacity VARCHAR(8), vehicle_rent VARCHAR(9))''')
# connect.execute('''Create table Customer_details (Customer_name VARCHAR (20), Customer_contact_number INT(10),
#                Customer_id_number VARCHAR(15), Customer_age INT(2), Customer_Gender Varchar (1))''')
# connect.execute('''CREATE TABLE Rented_cars (Car_id INT(4), Car_no VARCHAR(9), Car_name VARCHAR(15),
#    Customer_name VARCHAR(20), Customer_contact_number INT(10), Departure_date TIMESTAMP, Arrival_date TIMESTAMP)'''
# connect.execute('''Create table Rented_car_list (Car_id INT(4), Car_no VARCHAR(9), Car_name VARCHAR(15),
# Seats_capacity VARCHAR(8), luggage_capacity VARCHAR(8), vehicle_rent VARCHAR(9))''')
# connect.execute('''CREATE TABLE Car_history (Car_id INT(3), Car_name VARCHAR(15), Customer_name VARCHAR(25),
#                 Departure_date TIMESTAMP, Arrival_date TIMESTAMP, Revenue_generated INT(8))''')


def add_new_car():                                                    # function to add new car to the system
    print("\n\nADD NEW VEHICLE\n-------------------")
    vehicle_id = input("ENTER THE VEHICLE ID : ")                         # to take new car details from the user
    vehicle_number = input("ENTER THE VEHICLE NUMBER : ")
    vehicle_name = input("ENTER THE VEHICLE NAME : ")
    seat_capacity = input("ENTER THE SEAT CAPACITY : ")
    luggage_capacity = input("ENTER THE LUGGAGE CAPACITY : ")
    vehicle_rent = input("ENTER THE VEHICLE RENT : ")
    con = sqlite3.connect("Car_rental_database.db")
    add = ("INSERT INTO Cars_info (Car_id, Car_no, Car_name, Seats_capacity, luggage_capacity,"
           " vehicle_rent) values (" + vehicle_id + ",'" + vehicle_number + "','" + vehicle_name +
           "','" + seat_capacity + "','" + luggage_capacity + "','" + vehicle_rent + "'" ")")
    con.execute(add)                                                    # to insert the new car to the Cars_info table
    con.commit()
    con.commit()
    print("\n!!NEW VEHICLE", vehicle_name, "IS ADDED!!\n")        # displays message that new car is added to the system
    input()


def remove_car():                                               # function to remove an existing car from the table
    con = sqlite3.connect("Car_rental_database.db")
    show_all_cars()                                             # displays the list of all cars in the system
    remove_car_id = input("\nENTER THE CAR_ID THAT YOU WANT TO REMOVE: ")
    # to enter the car_id to remove from the system
    con.execute("DELETE FROM Cars_info WHERE car_id = ?", (remove_car_id,))   # removes the car from the
    # system on the basis of user's car_id input
    con.commit()
    con.close()
    print("\n!!", remove_car_id, "HAS BEEN SUCCESSFULLY REMOVED !!\n")


def receive_back_car():                      # function to recieve back car that has been rented to the customer
    show_rented_cars()                       # displays the list of all rented cars
    car_id = input("\nENTER THE CAR_ID TO RECIEVE BACK : ")     # to input the car_id that user wants to recieve back
    connnection = sqlite3.connect("Car_rental_database.db")
    cur = connnection.cursor()
    cur.execute("SELECT * FROM Rented_car_list WHERE Car_id = ?", (car_id,))
    car_selected = cur.fetchall()
    if car_selected:
        connnection.execute("INSERT INTO Cars_info (Car_id, Car_no, Car_name, Seats_capacity, luggage_capacity,"
                            " vehicle_rent) values (" + str(car_selected[0][0]) + ",'" + car_selected[0][1] + "','" +
                            car_selected[0][2] + "','" + car_selected[0][3] + "','" + car_selected[0][4] + "','" +
                            car_selected[0][5] + "'" ")")       #
        connnection.execute("DELETE FROM Rented_cars WHERE Car_id = ?", (car_id,))
        connnection.execute("DELETE FROM Rented_car_list WHERE Car_id = ?", (car_id,))
        connnection.commit()
        connnection.close()
        print("\n!!", car_selected[0][2], "RECIEVED BACK SUCCESSFULLY!!\n")
    else:
        print("\n!! CAR IS NOT RENTED !!")         # displays message if the car has not been rented or incorrect car_id
        input("\n\n||PRESS ENTER TO CONTINUE||")


def add_rented_car(car_info, customer_details):
    connection = sqlite3.connect("Car_rental_database.db")
    connection.execute("INSERT INTO Rented_cars (Car_id, Car_no, Car_name, Customer_name, Customer_contact_number,"
                       "Departure_date, Arrival_date) values (" + str(car_info[0][0]) + ",'" + car_info[0][1] + "','" +
                       car_info[0][2] + "','" + customer_details[0] + "','" + customer_details[1] + "','" +
                       customer_details[2] + "','" + customer_details[3] + "'" ")")  # insert query to add the rented
    # car to the Rented_cars table
    connection.commit()
    connection.close()


def show_rented_cars():                                 # function to display the list of rented cars
    connection = sqlite3.connect("Car_rental_database.db")      # connects to the Car_rental_database
    cur = connection.cursor()
    cur.execute("SELECT * FROM Rented_Cars")
    all_cars_list = cur.fetchall()                # fetches the details of all rented cars from the Rental_Cars database
    print("\n\n\t\t\t\t\t\t\t\t\t\t\t\t||RENTED CAR DETAILS||\n\t\t\t\t\t\t\t\t\t\t\t --------------------------")
    print("\n\n==================================================================================================="
          "=====================================")
    print("||CAR_ID||\t||CAR_NUMBER||\t||CAR_NAME||\t\t||CUSTOMER_NAME||\t||CUSTOMER_CONTACT_NO.||\t\t||DEPARTURE_DATE"
          "||\t||ARRIVAL_DATE||\n======================================================================================"
          "==================================================\n")
    for a, b, c, d, e, f, g in all_cars_list:               # displays the list of all rented cars
        print("  ", a, "\t\t", b, "\t", c, "\t\t\t", d, "\t\t\t", e, "\t\t\t\t", f, "\t\t", g)
        print()
    input("\n\n||PRESS ENTER TO CONTINUE||\n")


def show_all_cars():                                        # function to display all available cars in the system
    connection = sqlite3.connect("Car_rental_database.db")
    cur = connection.cursor()
    cur.execute("SELECT * FROM Cars_info")
    all_cars_list = cur.fetchall()                      # fetches the details of available cars from the Cars_info table
    print("\n\n==============================================================================="
          "====================================")
    print("||CAR_ID||\t||CAR_NUMBER||\t  ||CAR_NAME||\t\t||SEATS_CAPACITY||\t||LUGGAGE_CAPACITY||\t\t||RENTAL_PRICE||\n"
          "============================================================================================================"
          "=======\n")
    for a, b, c, d, e, f in all_cars_list:                                   # displays the details of available cars
        print("  ", a, " \t\t ", b, " \t  ", c, " \t\t ", d, " \t\t\t\t ", e, " \t\t\t\tRS ", f, "/DAY", sep='')
        print()
    input("\n\n||PRESS ENTER TO CONTINUE||\n")


def car_history():      # function to display the vehicle history (pick/drop date, customer name, revenue generated)
    con = sqlite3.connect("Car_rental_database.db")
    cursor = con.cursor()
    vehicle_id = input("\nENTER THE CAR ID OF WHICH YOU WANT TO SEE HISTORY : ")  # to enter the car_id of which the
    # user wants to see history
    cursor.execute("SELECT * FROM Car_history WHERE Car_id = ?", (vehicle_id, ))
    selected_car_history = cursor.fetchall()    # fetches the details of car of which the user wants to see history
    if selected_car_history:         # displays the car_name, customer_name,pick-up and drop-off date and revenue
        # generated of the car if the car_id is valid or the car has been rented
        print("\n====================================================================================================="
              "================")
        print("||CAR_ID||\t||CAR_NAME||\t\t||CUSTOMER_NAME||\t\t||PICK-UP_DATE||\t||DROP-OFF_DATE||\t"
              "||REVENUE_GENERATED||\n================================================================================="
              "=================================\n")
        for a, b, c, d, e, f in selected_car_history:
            print(" ", a, "\t\t", b, "\t\t\t", c, "\t\t", d, "\t\t", e, "\t\t", "  RS", f)
    else:
        print("\n!! VEHICLE HAS NOT BEEN RENTED YET!!\n")           # displays message if the car is not rented yet
        # or invalid car_id
    input("\n\n||PRESS ENTER TO CONTINUE||")


def rented_car_info(car_list):                              # function to add car details that has been removed from the
    # Cars_info table when the car has been rented
    conn = sqlite3.connect("Car_rental_database.db")
    conn.execute("INSERT INTO Rented_car_list (Car_id, Car_no, Car_name, Seats_capacity, luggage_capacity,vehicle_rent)"
                 "values (" + str(car_list[0][0]) + ",'" + car_list[0][1] + "','" + car_list[0][2] + "','" +
                 car_list[0][3] + "','" + car_list[0][4] + "','" + str(car_list[0][5]) + "'" ")")
    # Insert_query to add car details to Rented_car_list table
    conn.commit()
    conn.close()


def remove_rented_car(car_id):                          # function to remove the rented car from the Car_info table
    # when the customer rented a specfic car
    conn = sqlite3.connect("Car_rental_database.db")
    conn.execute("DELETE FROM Cars_info WHERE Car_id = ? ", (car_id,))      # query to delete the car from
    # the Cars_info table
    conn.commit()
    conn.close()


def generate_car_history(car_details, customer_name, bill_amount, pick_up_date, drop_off_date):
    # function to generate the car history which includes car_name, customer_name, pick-up date, drop-off date, and the
    # revenue made by the car
    conn = sqlite3.connect("Car_rental_database.db")
    conn.execute('''INSERT INTO Car_history(Car_id, Car_name, Customer_name, Departure_date, Arrival_date,
     Revenue_generated) values(''' + str(car_details[0][0]) + ",'" + car_details[0][2] + "','" + customer_name + "','" +
                 pick_up_date + "','" + drop_off_date + "'," + str(bill_amount) + ''')''')
    # insert query to add history of the car to the Car_history table
    conn.commit()
    conn.close()


def rent_car():                                         # function to rent a car to the customer
    con = sqlite3.connect("Car_rental_database.db")
    show_all_cars()                                     # calling show_all_vehicles function to display all
    # available cars to the customer
    car_choice = input("\nENTER THE VEHICLE ID THAT YOU WANT TO RENT : ")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Cars_info WHERE Car_id = ?", (car_choice,))
    selected_car_info = cursor.fetchall()    # fetches the details of the car which has selected by the customer to rent
    rented_car_info(selected_car_info)              # passes the details of the selected car to rented_car_info function
    print("\n\n!! YOU HAVE CHOOSE", selected_car_info[0][2], "TO RENT!!\n")

    departure_date = input("\n(PLEASE ENTER THE DATE IN DAY-MONTH-YEAR FORMAT)\nENTER THE PICK-UP DATE : ")
    arrival_date = input("ENTER THE DROP-OFF DATE : ")
    new_date = [int(departure_date[0]) * 10 + int(departure_date[1]), int(arrival_date[0]) * 10 + int(arrival_date[1]),
                int(departure_date[3]) * 10 + int(departure_date[4]), int(arrival_date[3]) * 10 + int(arrival_date[4]),
                int(departure_date[6]) * 1000 + int(departure_date[7]) * 100 + int(departure_date[8]) * 10 +
                int(departure_date[9]),
                int(arrival_date[6]) * 1000 + int(arrival_date[7]) * 100 + int(arrival_date[8]) * 10 +
                int(arrival_date[9])]       # to convert the pickup and drop-off date into Int

    date1 = date(new_date[4], new_date[2], new_date[0])
    date2 = date(new_date[5], new_date[3], new_date[1])           # to find out the total number of days to rent the car
    total_amount = selected_car_info[0][5] * ((date2 - date1).days + 1)     # calculates the total cost to rent the car
    # for n number of days which has been entered by the user using date

    if date2 > date1:                       # displays the message of total amount to rent a car for n number of dats
        print("\nTOTAL PRICE FOR", (date2 - date1).days + 1, "DAY(S) = Rs", total_amount)
    else:
        print((date1 - date2).days + 1)
        print("\nTOTAL PRICE FOR", (date2 - date1).days + 1, "DAY(S) = Rs", total_amount)
    print("\n\n||PRESS ENTER TO CONFIRM||\n")
    input()
    print("\n---------------------\nCUSTOMER DETAILS\n---------------------")
    cust_name = input("ENTER YOUR NAME : ")                                 # to take the details from the customer
    cust_mobile = input("ENTER YOUR CONTACT NUMBER : ")
    cust_license = input("ENTER YOUR LICENSE NUMBER : ")
    input("ENTER YOUR AGE : ")
    input("ENTER YOUR GENDER : ")
    customer_info = cust_name, cust_mobile, departure_date, arrival_date   # to put the details of the customer
    # into a customer_info list
    pick_up_location = input("\n!! CUSTOMER DETAILS ADDED !!\n\nENTER THE PICK-UP LOCATION"
                             " (PLEASE PROVIDE CITY NAME ONLY) : ")                 # to enter the pick-up location of
    # the rented car
    print("\n\n--------------------------------------------\n\t\t\t\t\tORDER DETAILS\n--------------------------------"
          "--------------\nCUSTOMER NAME =", cust_name, "\nCONTACT NUMBER =", cust_mobile, "\nCUSTOMER LICENSE NUMBER ="
          "", cust_license, "\nRENTED CAR =", selected_car_info[0][2], "\nTOTAL AMOUNT = RS", total_amount,
          "\nPICK-UP LOCATION =", pick_up_location, "\nPICK-UP DATE =", departure_date, "\nDROP-OFF DATE=",
          arrival_date, "\n\n||PRESS ENTER TO CONFIRM||\n")             # to display the order summary of the rented car
    # and the customer details
    input()
    input("ENTER YOUR UPI ID TO MAKE PAYMENT : ")
    print("\n!! CONGRATULATIONS!! YOUR PAYMENT HAS BEEN SUCCESSFULL !!")
    print("\n\n!!YOUR CAR", selected_car_info[0][2], "WITH NUMBER PLATE", selected_car_info[0][1], "WILL BE AT",
          pick_up_location, "AIRPORT ON", departure_date, "AT 5:00 PM!!\n")
    generate_car_history(selected_car_info, cust_name, total_amount, departure_date, arrival_date)
    # passes the details of the rented car, customer_name, bill_amount,pick-up and drop-off date to the
    # generate_car_history function
    add_rented_car(selected_car_info, customer_info)        # passes the details of the rented car and the details of
    # the customer to the add_rented_car function
    remove_rented_car(selected_car_info[0][0])      # passes the car_id as a parameter to the remove_rented_car function
    input("\n||PRESS ENTER TO JUMP INTO MAIN MENU||\n")


def manager_menu():                                 # function to display the operations that can be performed by the
    # manager of the Rent & Drive
    while True:
        print("\n\n=================================================================")
        print("\t\t\t\t\t\t\tRENT & DRIVE\n=================================================================")
        print("\n\nPLEASE SELECT AN OPTION\n---------------------------")
        print("1 - ADD NEW VEHICLE")
        print("2 - REMOVE EXISTING VEHICLE")                    # various operation that can be performed by the manager
        print("3 - RECIEVE BACK VEHICLE")
        print("4 - SHOW RENTED VEHICLES")
        print("5 - SHOW ALL VEHICLE LIST")
        print("6 - VEHICLE HISTORY")
        print("7 - EXIT\n")
        manager_choice = int(input("PLEASE PROVIDE YOUR CHOICE : "))        # to input the choice that the manager
        # wants to perform

        # calling respective functions on the basis of manager's choice
        if manager_choice == 1:
            add_new_car()
        elif manager_choice == 2:
            remove_car()
        elif manager_choice == 3:
            receive_back_car()
        elif manager_choice == 4:
            show_rented_cars()
        elif manager_choice == 5:
            show_all_cars()
        elif manager_choice == 6:
            car_history()
        elif manager_choice == 7:
            exit(0)
        else:               # prints message if the manager enter the invalid option
            print("\n||INVALID OPTION||\nPLEASE PROVIDE VALID CHOICE\n")
            continue


def customer_menu():                # function to display various operations that the customer can perform
    while True:
        print("\n\n=================================================================")
        print("\t\t\t\t\tWELCOME TO RENT & DRIVE\n=================================================================")
        print("\n\nPLEASE SELECT AN OPTION\n------------------------")
        print("1 - RENT A CAR")
        print("2 - SHOW ALL CARS")
        print("3 - EXIT")
        # to take input from the customer that which operation he wants to perform
        customer_choice = int(input("\nPLEASE PROVIDE YOUR CHOICE : "))

        # calls to the respective function based on the customer's choice
        if customer_choice == 1:
            rent_car()
        elif customer_choice == 2:
            show_all_cars()
            car_rent = int(input("\nDO YOU WANT TO RENT A CAR?\n1 - YES\n2 - NO\nPLEASE ENTER YOUR OPTION : "))
            if car_rent == 1:
                rent_car()
            else:
                customer_menu()
        elif customer_choice == 3:
            exit(0)
        else:                           # displays message if the customer enters invalid option
            print("\n||INVALID OPTION||\nPLEASE PROVIDE VALID CHOICE\n")
            continue


while True:                    # starts the program and gives choices to user(manager or customer) to perform operations
    print("\n\n=================================================================")
    print("\t\t\t\t\t\t\tRENT & DRIVE||\n=================================================================")
    print("\n\nPLEASE SELECT AN OPTION\n-------------------------")
    # to take choice from the user whether he/she is manager of customer
    user_choice = int(input("1 - MANAGER\n2 - CUSTOMER\n\nPLEASE PROVIDE YOUR CHOICE : "))
    id_info = ['admin', 'admin@123']           # user_id and password to login as the manager of the RENT & DRIVE System
    # if the user is manager
    if user_choice == 1:
        while True:
            username = input("\nPLEASE ENTER YOUR USERNAME : ")
            password = input("PLEASE ENTER THE PASSWORD : ")
            if username == id_info[0] and password == id_info[1]:
                manager_menu()              # Calls to manager_menu() function if the user is manager
            else:                           # if username and password is incorrect
                print("\n||INCORRECT USERNAME AND PASSWORD||\n||PLEASE TRY AGAIN||")
                continue
    # if the user is customer then it calls to customer_menu() function
    elif user_choice == 2:
        customer_menu()
    else:                                   # displays message if the user enters invalid option
        print("\n||INVALID OPTION||\n||PLEASE ENTER VALID OPTION||")
        continue
