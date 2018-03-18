import psycopg2
import random

global conn
conn = psycopg2.connect(dbname="mortfors_fv", user="ah8301", password="n1ry5adj", host="pgserver.mah.se")
global cursor
cursor = conn.cursor

def busbooking():
    conn = psycopg2.connect(dbname="mortfors_fv", user="ah8301", password="n1ry5adj", host="pgserver.mah.se")
    cursor = conn.cursor
    while True:
        welcome()
        menu()
        user_choice = input("Your choice, choose between 1, 2, 3 or 4!")
        if user_choice == "1":
            register_traveller()
        elif user_choice == "2":
            book_trip()
        elif user_choice == "3":
            search()
        elif user_choice == "4":
            print("Thanks for choosing Mortfors!")
            break
        else:
            print("Please choose 1, 2, 3 or 4.")

def welcome():
    print("*"*40)
    print("Welcome to the booking system used by Mortfors!")
    print("*"*40)

def menu():
    print("*"*40)
    print("Menu")
    print("*"*40)
    print("1.Sign up")
    print("2.Book trip")
    print("3.Search for trips.")
    print("4.Exit")

def register_traveller():

    conn = psycopg2.connect(dbname="mortfors_fv", user="ah8301", password="n1ry5adj", host="pgserver.mah.se")
    cursor = conn.cursor()
    
    personid = random.randint(1,100000000)
    name = input("Your name (Firstname Lastname): ")
    email = input("Email: ")
    number = input("Phonenumber: ")
    cursor.execute("insert into Resenär values (%s, %s, %s, %s)", (personid, name, email, number))
    conn.commit()

def book_trip():
	pass

def search_trips():
    print("Current planned trips:")
    cursor.execute("SELECT Datum, Avgång, Ankomst FROM Tur ")

busbooking()
