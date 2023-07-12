# Address Book Application

## Description

This is a simple address book application built with Python and Tkinter. It allows users to:

- Add new contacts (first name, last name, address, city, state, zip code)
- View all contacts
- Delete contacts
- Update/edit existing contacts

The application uses SQLite to store contact information in a database file `address_book.db`. 

## Usage

To use the application:

1. Run `main.py`
2. The main window allows you to:
   - Enter a new contact by filling out the fields and clicking `Add Record`
   - View all contacts by clicking `View Records`
   - Delete a contact by entering the ID and clicking `Delete Record` 
   - Update a contact by entering the ID, clicking `Update Record`, updating the fields, and clicking `Save Changes`
3. The `Show Records` window displays all contacts
4. `Submit` inserts new records, `Delete` removes records based on ID, `Update` opens the edit window to modify existing records

The database is automatically created on first run with a table called `addresses`.

## Files

- `main.py`: Main application code 
- `address_book.db`: SQLite database file storing contacts

## Requirements

- Python 3
- Tkinter (`sudo apt install python3-tk` on Linux)
- SQLite 3

