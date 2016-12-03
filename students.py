from peewee import *

db = SqliteDatabase('students.db')

class Student(Model):
    #CharField is a field that hold character, in SQL terminology this is varchar
    username = CharField(max_length = 255, unique = True)
    #IntegerField holds integer
    points = IntegerField(default = 0)

    class Meta:
        database = db

students = [
    {
        'username': 'Buka Cakrawala',
        'points': 101
    },
    {
        'username': 'Jeremy Rossman',
        'points': 20
    },
    {
        'username': 'Nikolas Burk',
        'points': 100
    }
]

def add_students():
    for student in students:
        try:
            Student.create(username = student['username'],
                            points = student['points'])
        except IntegrityError:
            student_record = Student.get(username = student['username'])
            student_record.points = student['points']
            student_record.save()

def top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    return student


if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe = True)
    add_students()
    print("Our top student right now is: {0.username}.".format(top_student()))
