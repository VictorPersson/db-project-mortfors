import psycopg2
from random import randint

global conn
conn = psycopg2.connect(dbname="mortfors_fv", user="ai0377", password="pw6qvfi9", host="pgserver.mah.se")

global cursor
cursor = conn.cursor


def admin_panel():
    conn = psycopg2.connect(dbname="mortfors_fv", user="ai0377", password="pw6qvfi9", host="pgserver.mah.se")
    cursor = conn.cursor
    while True:
        welcome()
        menu()
        user_choice = input("Your choice, enter 1, 2, 3 or 4: ")
        if user_choice == "1":
            register_driver()
        elif user_choice == "2":
            add_route()
        elif user_choice == "3":
            add_driver_later()
        elif user_choice == "4":
            print("Exiting Mortfors Admin panel")
            break
        else:
            print("Please choose 1, 2, 3 or 4!")


def welcome():
    print("≡"*45)
    print("Welcome to Admin panel, powered by Mortfors!")



def menu():
    print("≡"*45)
    print("Menu")
    print("≡"*45)
    print("1.Register a new driver.")
    print("2.Add bus route.")
    print("3.Add/change bus driver.")
    print("4.Exit")
    spacer()


def register_driver():
    conn = psycopg2.connect(dbname="mortfors_fv", user="ai0377", password="pw6qvfi9", host="pgserver.mah.se")
    cursor = conn.cursor()

    ssn = input("SSN: ")
    c_id = input("Give this driver an unique ID")
    name = input("Your name (Firstname Lastname): ")
    adress = input("Adress: ")
    number = input("Phonenumber: ")
    cursor.execute("insert into Chaufför values (%s, %s, %s, %s, %s)", (ssn, c_id, name, adress, number))
    conn.commit()


def add_route():
    conn = psycopg2.connect(dbname="mortfors_fv", user="ai0377", password="pw6qvfi9", host="pgserver.mah.se")
    cursor = conn.cursor()

    tour_id = randint(1,100000000)
    c_id = "null"
    date = input("Trip date: ")
    departure = input("Departure time: ")
    arrival = input("Arrival time: ")
    price = input("Price: ")
    seats = input("Max seats: ")
    start = input("Start location: ")
    destination = input("End destination: ")
    cursor.execute("insert into Tur values (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (tour_id, c_id, date, departure, arrival, price, seats, start, destination))
    conn.commit()


def add_driver_later():
    conn = psycopg2.connect(dbname="mortfors_fv", user="ai0377", password="pw6qvfi9", host="pgserver.mah.se")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Tur;")
    all_trips = cursor.fetchall()
    for trip in all_trips:
        print(trip)

    changed_route = input("Which route (routeID) would you like to update the driver for: ")
    route_list = []
    route_list.append(changed_route)
    for i in range(len(route_list)):
        route_list[i] = int(route_list[i])

    cursor.execute("SELECT ReseID FROM Tur where ReseID =" + changed_route)
    routeID = cursor.fetchone()
    routeID_list = []
    routeID_list.append(routeID[0])

    c_id = input("Enter drivers SSN: ")
    if routeID_list == route_list:
        cursor.execute("update Tur set Personnummer =" + c_id + " where reseID =" + changed_route)
        conn.commit()
    else:
        print("That is not a valid routeID or driver!")
        conn.commit()


def spacer():
    print("═"*45)


admin_panel()
