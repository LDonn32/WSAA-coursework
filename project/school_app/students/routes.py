from flask import Blueprint, jsonify, request
from db import get_student_db

students_bp = Blueprint('students', __name__)

@students_bp.route('/students')
def list_students():
    conn = get_student_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id, first_name, last_name FROM students")
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return jsonify(data)

@students_bp.route('/students/add', methods=['POST'])
def add_student():
    first = request.form['first_name']
    last = request.form['last_name']

    conn = get_student_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (first_name, last_name) VALUES (%s, %s)",
        (first, last)
    )
    conn.commit()

    cursor.close()
    conn.close()
    return "Student added"
