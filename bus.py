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


def register_driver():
    conn = psycopg2.connect(dbname="mortfors_fv", user="ai0377", password="pw6qvfi9", host="pgserver.mah.se")
    cursor = conn.cursor()

    personnr = input("SSN:")
    name = input("Your name (Firstname Lastname): ")
    adress = input("Adress: ")
    number = input("Phonenumber: ")
    cursor.execute("insert into Chaufför values (%s, %s, %s, %s)", (personnr, name, adress, number))
    conn.commit()

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
    print(personID)
    print(p_id, what_trip, what_seat)
    cursor.execute("SELECT Platser FROM Tur WHERE reseid =" + what_trip)
    current_seats = cursor.fetchone()
    print(current_seats[0])
    cursor.execute("insert into bokning values (%s, %s, %s)", (what_trip, p_id, what_seat))
    cursor.execute("UPDATE Tur SET platser=" + (int(current_seats[0]) - int(what_seat)) + " where reseid =" + what_trip)
    conn.commit()


def search_trips():
    conn = psycopg2.connect(dbname="mortfors_fv", user="ai0377", password="pw6qvfi9", host="pgserver.mah.se")
    cursor = conn.cursor()
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("Trip ID", "Date", "Departure", "Arrival", "From", "To"))
    cursor.execute("SELECT ReseID, Datum, Avång, Ankomst, Från, Till FROM Tur;")
    res = cursor.fetchall()
    for row in res:
        print(row)
    conn.commit()

def spacer():
    print("═"*45)

busbooking()
