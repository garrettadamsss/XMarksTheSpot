#!/usr/bin/env python

#-----------------------------------------------------------------------
# database.py
# Author: Bob Dondero
#-----------------------------------------------------------------------

from sqlite3 import connect
from sys import stderr
from os import path
from entry import Entry
import sqlite3

#-----------------------------------------------------------------------

class Database:
    
    def __init__(self):
        self._connection = None

    def connect(self):      
        self._connection = sqlite3.connect('entries.db')

                    
    def disconnect(self):
        self._connection.close()

    # enty is Entry object from entry.py
    def insertEntry(self, entry):
        try:
            cursor = self._connection.cursor()


            values = (entry.placename, entry.location, entry.description)


            QUERY_STRING = ''' INSERT INTO entries(placename,location,description)
              VALUES(?,?,?) '''
            cursor.execute(QUERY_STRING, (values))   
            self._connection.commit()              
            return cursor.lastrowid
        except Exception as e:
            print(e)

    # searchEntry returns all rows, fields that contain nameQuery or locQuery (name or location)
    # returns list of Entry objects
    def searchEntry(self, nameQuery='', locQuery=''):

        cursor = self._connection.cursor()
        
        # uppercase everything to make search case insensitive

        if (nameQuery == ''):
            name = '%'
        else:
            name = '%' + nameQuery.upper() + '%'


        if (locQuery== ''):
            location = '%'
        else:
            location = '%' + locQuery.upper() + '%'

        QUERY_STRING = """ SELECT placename, location, description, imagelocation from entries
                           WHERE UPPER(placename) like ? AND
                           UPPER(location) like ?
                        """
        cursor.execute(QUERY_STRING, (name, location))

        rows = cursor.fetchall()


        def makeEntry(row):
            return Entry(placename=row[0], location=row[1], description=row[2], image=row[3])

        entries = map(makeEntry, rows)
        return list(entries)






# dont' call this again, i already made a table
def createTable():
    con = sqlite3.connect('entries.db')
    cur = con.cursor()

    # Create table
    cur.execute(""" CREATE TABLE IF NOT EXISTS entries (
                                        id integer PRIMARY KEY,
                                        placename text NOT NULL,
                                        location text,
                                        description text,
                                        imagelocation text,
                                        latitude float,
                                        longitude float
                                    ); """)




    # Save (commit) the changes
    con.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    con.close()


def main():
    # inserted this entry already
    entry1 = Entry(placename='Ho Family', location='Garden Grove', description='cool stuff')


    database = Database()
    database.connect()
    for ele in database.searchEntry(nameQuery='ho'):
        print(ele)
    database.disconnect()

#-----------------------------------------------------------------------

# For testing:

if __name__ == '__main__':
    main()
    

