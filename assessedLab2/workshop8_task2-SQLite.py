# workshop8 task2 - SQLite, 17/09/21, Cordelia Jiang
# import the sqlite3 module, connecting to the hotel.db
import sqlite3
connection = sqlite3.connect("hotel.db")

# all access to the database is via the cursor object.
cursor = connection.cursor()

# list full details of all hotels in Brisbane
# go through items in cursor.execute, and put them in a list
# cursor.execute allows Python code to execute sql command.
hotel_detailList = [x for x in cursor.execute("SELECT hotelNo, hotelName, city FROM Hotel WHERE city = 'Brisbane'")]
print("hotel detail list: ", hotel_detailList)

# list the names and addresses of all guests in ascending order of guest names.
# go through items in cursor.execute, and put them in a list
guest_list = [x for x in cursor.execute("SELECT guestName, guestAddress FROM Guest ORDER BY guestName ASC")]
print("guest list: ", guest_list)

# list the price and type of all rooms at the Grosvenor Hotel
# go through items in cursor.execute, and put them in a list
room_list = [x for x in cursor.execute("SELECT price, roomtype FROM Room, Hotel WHERE Room.hotelNo = Hotel.hotelNo AND "
                                       "hotelName = 'Grosvenor Hotel'")]
print("room list: ", room_list)

# find the maximum, minimum, and average room prices of all hotels
# go through items in cursor.execute, and put them in a list
room_priceList = [x for x in cursor.execute("SELECT max(price), min(price), avg(price) FROM Room, Hotel "
                                            "WHERE Room.hotelNo = Hotel.hotelNo")]
print("hotel price list: ", room_priceList)

# close the connection to save changes
connection.close()
