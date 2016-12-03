import datetime
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

def add_entry():
    """add an entry"""

def read_entry():
    """view previous entry"""

def delete_entry(entry):
    """delete an entry"""

if __name__ == '__main__':
    initiliaze()
    menu_loop()
