
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
        user_choice = input("Your choice, enter 1, 2 or 3: ")
        if user_choice == "1":
            register_driver()
        elif user_choice == "2":
            add_route()
        elif user_choice == "3":
            print("Exiting Mortfors Admin panel")
            break
        else:
            print("Please choose 1, 2, or 3!")

def welcome():
    print("≡"*45)
    print("Welcome to Admin panel, powerd by Mortfors!")

def menu():
    print("≡"*45)
    print("Menu")
    print("≡"*45)
    print("1.Register driver.")
    print("2.Add bus route.")
    print("3.Exit")
    spacer()


def register_driver():
    conn = psycopg2.connect(dbname="mortfors_fv", user="ai0377", password="pw6qvfi9", host="pgserver.mah.se")
    cursor = conn.cursor()

    personnr = input("SSN: ")
    name = input("Your name (Firstname Lastname): ")
    adress = input("Adress: ")
    number = input("Phonenumber: ")
    cursor.execute("insert into Chaufför values (%s, %s, %s, %s)", (personnr, name, adress, number))
    conn.commit()

def add_route():
    conn = psycopg2.connect(dbname="mortfors_fv", user="ai0377", password="pw6qvfi9", host="pgserver.mah.se")
    cursor = conn.cursor()

    tour_id = randint(1,100000000)
    ssn = input("Driver SSN: ")
    date = input("Trip date: ")
    departure = input("Departure time: ")
    arrival = input("Arrival time: ")
    price = input("Price: ")
    seats = input("Max seats: ")
    start = input("Start location: ")
    destenation = input("End destenation: ")
    cursor.execute("insert into Tur values (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (tour_id, ssn, date, departure, arrival, price, seats, start, destenation))
    conn.commit()




def spacer():
    print("═"*45)

admin_panel()
