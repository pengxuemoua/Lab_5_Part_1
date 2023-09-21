"""
A menu - you need to add the database and fill in the functions. 

This program interacts with a database. The database store data for chainsaw jugglers. You can display all records, 
search the data of a juggler by name, add a new record, edit an existin record, delete a record and quit the program.

"""
import sqlite3
from sqlite3 import connect

# TODO create database table OR set up Peewee model to create table
db = 'juggling.db'

def main():
    menu_text = """
    1. Display all records
    2. Search by name
    3. Add new record
    4. Edit existing record
    5. Delete record 
    6. Quit
    """

    while True:
        
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            search_by_name()
        elif choice == '3':
            add_new_record()
        elif choice == '4':
            edit_existing_record()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records(): 
    """Query return all rows from juggling table along with rowid."""
    
    conn = connect(db)
    results = conn.execute('SELECT rowid, * from juggling')
    print()
    for row in results:
        print(row)

    conn.close()

def search_by_name():
    """Asks user for a name which is then title case, and prints the matching record if found. 
    If no such name is found in the database, a please try again message will be displayed.')"""
    
    search_name = input('To view the records of a juggler, please enter their name: ').title()
    conn = connect(db)
    results = conn.execute('SELECT * from juggling where name like ?', (search_name,))
    juggler = results.fetchone()
    if juggler:
        print(f'\nHere are the record for your juggler: {juggler}')
    else:
        print(f'\nSorry, we do not have a juggler by that name, please try again.')
    
    conn.close()


def add_new_record():
    """Adds new record to database."""
    
    new_name = input('Enter a full name: ').title()
    new_country = input('Enter a country: ').title()
    new_juggle_record = int(input('Enter the number of chainsaw juggles: '))

    with connect(db) as conn:
        conn.execute('INSERT INTO juggling values (?, ?, ?)', (new_name, new_country, new_juggle_record))
    
    conn.close()


def edit_existing_record():
    """Edits exisiting record in database."""
 
    update_id = int(input('Please enter the id of the juggler you want to update: '))
    update_juggle_record = int(input('Please enter the updated number of catches for your juggler: '))
    with connect(db) as conn:
        conn.execute('UPDATE juggling SET number_of_catches = ? WHERE rowid = ?', (update_juggle_record, update_id))

    conn.close()

def delete_record():
    """deletes existing record in database"""
     
    delete_record = input('Please enter the full name of the chainsaw juggler you would like to delete: ').title()
    
    with connect(db) as conn:
        conn.execute('DELETE from juggling WHERE name = ?', (delete_record,))
    
    conn.close()


if __name__ == '__main__':
    main()