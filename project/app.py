from flask import Flask, render_template
from models import db, Student

app = Flask(__name__)

# For development: SQLite is easiest
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/students')
def list_students():
    students = Student.query.all()
    return {
        "students": [
            {"id": s.id, "first_name": s.first_name, "last_name": s.last_name}
            for s in students
        ]
    }

if __name__ == '__main__':
    with app.app_context():
        db.create_all()   # Creates tables on first run
    app.run(debug=True)
