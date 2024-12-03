from flask import *
from app.student import student_bp
from app.student.models import Student
from app.student.forms import StudentForm
from app import db

@student_bp.route("/student_list", methods = ["GET"])
def get_student_list():
    student = Student.query.all()
    return render_template("list_student.html", st = student)

@student_bp.route("/add_student", methods = ["GET", "POST"])
def add_student():
    forms = StudentForm()
    if forms.validate_on_submit():
        program_id = forms.program_id.data
        student_name = forms.name.data
        student_code = forms.code.data

        new_student = Student(program_id = program_id, name = student_name, code = student_code)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for("student.get_student_list"))

    return render_template("add_student.html", form = forms)

@student_bp.route("/update_student/<int:id>", methods = ["GET", "POST"])
def update_student(id):
    student = Student.query.get_or_404(id)
    form = StudentForm(obj = student)
    if form.validate_on_submit():
        form.populate_obj(student)
        db.session.commit()
        return redirect(url_for("student.get_student_list"))
    return render_template("add_student.html", form = form)

@student_bp.route("/delete_student/<int:id>", methods = ["POST"])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for("student.get_student_list"))

@student_bp.route("/delete_all_students", methods = ["POST"])
def delete_all_students():
    Student.query.delete()
    db.session.commit()
    return redirect(url_for("student.get_student_list"))