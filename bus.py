# -*- coding: utf-8 -*-


import psycopg2
import random

global conn
conn = psycopg2.connect(dbname="mortfors_fv", user="ai0377", password="pw6qvfi9", host="pgserver.mah.se")
global cursor
cursor = conn.cursor

def busbooking():
    conn = psycopg2.connect(dbname="mortfors_fv", user="ai0377", password="pw6qvfi9", host="pgserver.mah.se")
    cursor = conn.cursor
    while True:
        welcome()
        menu()
        user_choice = input("Your choice, please enter 1, 2, 3 or 4: ")
        if user_choice == "1":
            register_traveller()
        elif user_choice == "2":
            book_trip()
        elif user_choice == "3":
            search_trips()
        elif user_choice == "4":
            print("Thanks for choosing Mortfors!")
            break
        else:
            print("Please choose 1, 2, 3, 4!")

def welcome():
    print("≡"*45)
    print("Welcome to the booking system used by Mortfors!")

def menu():
    print("≡"*45)
    print("Menu")
    print("≡"*45)
    print("1.Sign up")
    print("2.Book trip")
    print("3.Search for trips.")
    print("4.Exit")
    spacer()
    
def register_traveller():

    conn = psycopg2.connect(dbname="mortfors_fv", user="ai0377", password="pw6qvfi9", host="pgserver.mah.se")
    cursor = conn.cursor()

    personid = random.randint(1,100000000)
    name = input("Your name (Firstname Lastname): ")
    email = input("Email: ")
    number = input("Phonenumber: ")
    cursor.execute("insert into Resenär values (%s, %s, %s, %s)", (personid, name, email, number))
    conn.commit()

def book_trip():
    conn = psycopg2.connect(dbname="mortfors_fv", user="ai0377", password="pw6qvfi9", host="pgserver.mah.se")
    cursor = conn.cursor()
    what_traveller = input("What is your name?: ")
    the_traveller = cursor.execute("SELECT personID FROM Resenär WHERE Namn ='" + what_traveller + "'")
    personID = cursor.fetchone()
    p_id = personID
    spacer()
    search_trips()
    spacer()
    what_trip = input("What trip do you wish to book, please choose the correct Trip ID from the Trip list!: ")
    what_seat = int(input("How many seats do you wish to book?: "))
    cursor.execute("SELECT Platser FROM Tur WHERE reseid =" + what_trip)
    current_seats = cursor.fetchone()
    cursor.execute("Select sum(bokadplats) from bokning where reseid =" + what_trip)
    booked_seats = cursor.fetchone()
    cursor.execute("Select platser from tur where reseid =" + what_trip)
    total_seats = cursor.fetchone()
    available_seats = total_seats[0] - booked_seats[0]
    try:
        if what_seat > available_seats:
            print("There arent that many free spots on this trip!")
        else: 
            cursor.execute("insert into bokning values (%s, %s, %s)", (what_trip, p_id, what_seat))
            conn.commit()
    except:
        spacer()
        print("This person does not exist or is already booked on this trip!")
        spacer()


def search_trips():
    conn = psycopg2.connect(dbname="mortfors_fv", user="ai0377", password="pw6qvfi9", host="pgserver.mah.se")
    cursor = conn.cursor()
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("Trip ID", "Date", "Departure", "Arrival", "From", "To"))
    cursor.execute("SELECT ReseID, Datum, Avång, Ankomst, Från, Till FROM Tur;")
    trips = cursor.fetchall()
    for trip in trips:
        print(trip)
    conn.commit()

def spacer():
    print("═"*45)

busbooking()
