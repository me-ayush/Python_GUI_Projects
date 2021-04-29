from tkinter import *
import sqlite3

root = Tk()
root.title("Connecting Database")
root.geometry("500x400")

conn = sqlite3.connect('address_book.db')

# Create Cursor
c = conn.cursor()

# Create Tables
c.execute("""CREATE TABLE addresses (
	first_name text, 
	last_name text, 
	address text,
	city text,
	state text,
	zipcode integer
	)""")

# Commit Changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()