from flask import Flask
from students.routes import students_bp
from teachers.routes import teachers_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(students_bp)
app.register_blueprint(teachers_bp)

@app.route('/')
def home():
    return "School Management System Running"

if __name__ == '__main__':
    app.run(debug=True)

