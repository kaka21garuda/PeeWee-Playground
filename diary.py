from collections import OrderedDict
import datetime
import sys

from peewee import *

db = SqliteDatabase('diary.db')

class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default = datetime.datetime.now)

    class Meta:
        database = db

def initiliaze():
    """create the database and table if they don't exist."""
    db.connect()
    db.create_tables([Entry], safe = True)


def menu_loop():
    """show the menu"""
    choice = None

    while choice != 'q':
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print("{}) {}".format(key, value.__doc__))
        choice = raw_input('Action: ').lower().strip()

        if choice in menu:
            menu[choice]()

def add_entry():
    """add an entry"""
    print("Enter your entry. Press ctrl+d when finished.")
    data = sys.stdin.read().strip()

    if data:
        if raw_input('Save entry? [Yn] ').lower() != 'n':
            Entry.create(content = data)
            print("Saved successfully!")

def read_entry():
    """view previous entry"""

def delete_entry(entry):
    """delete an entry"""

menu = OrderedDict([
    ('a', add_entry),
    ('r', read_entry)
])

if __name__ == '__main__':
    initiliaze()
    menu_loop()
