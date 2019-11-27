# database,exeptional handling,module,tinkter
# creating database
import sqlite3

connection = sqlite3.connect('movies.db')
print("Database opened successfully")

TABLE_NAME ="movies_table"
MOVIES_ID = "movies_id"
MOVIES_NAME = "movies_name"
MOVIES_DURATION = "movies_duration"
MOVIES_RATING = "movies_rating"
MOVIES_GENRE = "movies_genre"
RELEASE_YEAR = "release_year"

connection.execute("CREATE TABLE IF NOT EXISTS "
                   + TABLE_NAME
                   + "( " + MOVIES_ID +
                   " INTEGER PRIMARY KEY " +
                   "AUTOINCREMENT," + MOVIES_NAME +
                   " TEXT, " + MOVIES_DURATION + " TEXT, "
                   + MOVIES_RATING + " REAL, " + MOVIES_GENRE + " TEXT, " + RELEASE_YEAR + " INTEGER); ")

print("Table created sucessfully.")

def insert_record(name,duration,ratings,genre,release_year):
    connection.execute( "INSERT INTO " + TABLE_NAME
                + " ( " + MOVIES_NAME + " , "
                     + MOVIES_DURATION + " , "
                     + MOVIES_RATING + " , "
                     + MOVIES_GENRE + ", "
                     + RELEASE_YEAR + ") VALUES ( ?,?,?,?,? ) ; " ,
                     (name,duration,ratings,genre ,release_year))
    connection.commit()
    print("inserted successfully")

def retreive_record():
    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + ";")
    return cursor

