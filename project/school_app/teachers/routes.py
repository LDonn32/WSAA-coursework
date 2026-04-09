from flask import Blueprint, jsonify
from db import get_teacher_db

teachers_bp = Blueprint('teachers', __name__)

@teachers_bp.route('/teachers')
def list_teachers():
    conn = get_teacher_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id, name FROM teachers")
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return jsonify(data)
