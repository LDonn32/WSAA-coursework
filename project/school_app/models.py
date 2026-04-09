import flask 
import flask_sqlalchemy

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Student model with additional fields and relationships

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    date_of_birth = db.Column(db.Date)
    qualifications = db.relationship('Qualification', backref='student')
    exam_results = db.relationship('ExamResult', backref='student')

class Qualification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

class ExamResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100))
    grade = db.Column(db.String(5))
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))



# Teacher model with relationship to Class model

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    classes = db.relationship('Class', backref='teacher')

class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(50))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))
