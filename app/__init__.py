from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from password import get_password

db = SQLAlchemy()
migrate = Migrate()

DB_USER = "root"
DB_PASSWORD = get_password()
DB_HOST = "localhost"
DB_NAME = "student_course_group"

def create_app():
    app = Flask(__name__)
    app.secret_key = "OmoItsAlreadyOneOClock"

    @app.route('/')
    def index():
        return render_template("index.html")

    DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    
    from app.faculty import faculty_bp
    app.register_blueprint(faculty_bp)

    from app.department import department_bp
    app.register_blueprint(department_bp)

    from app.program import program_bp
    app.register_blueprint(program_bp)
    
    from app.level import level_bp
    app.register_blueprint(level_bp)

    from app.course import course_bp
    app.register_blueprint(course_bp)

    from app.group import group_bp
    app.register_blueprint(group_bp)

    from app.student import student_bp
    app.register_blueprint(student_bp)

    from app.assign_students import assign_students_bp
    app.register_blueprint(assign_students_bp)

    from app.faculty.models import Faculty
    from app.department.models import Department
    from app.assign_students.models import Assign_Students
    from app.course.models import Course
    from app.group.models import Group
    from app.level.models import Level
    from app.program.models import Program
    from app.student.models import Student

    with app.app_context():
        db.create_all()




    return app