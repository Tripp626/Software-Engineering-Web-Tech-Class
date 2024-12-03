from flask import *
from app.assign_students import assign_students_bp
from app.assign_students.models import Assign_Students
from app.assign_students.forms import AssignStudentForm
from app import db

@assign_students_bp.route("/assign_students_list")
def get_assign_students_to_group_list():
    assign_student = Assign_Students.query.all()
    return render_template("list_assign_students.html", ass = assign_student)

@assign_students_bp.route("/add_assign_student", methods = ["GET", "POST"])
def add_assign_student():
    forms = AssignStudentForm()
    if forms.validate_on_submit():
        student_id = forms.student_id.data
        group_id = forms.group_id.data

        new_assign_student = Assign_Students(student_id = student_id, group_id = group_id)
        db.session.add(new_assign_student)
        db.session.commit()
        return redirect(url_for("assign_students.get_assign_students_to_group_list"))

    return render_template("add_assign_student.html", form = forms)

@assign_students_bp.route("/update_assign_student/<int:id>", methods = ["GET", "POST"])
def update_assign_student(id):
    assign_student = Assign_Students.query.get_or_404(id)
    form = AssignStudentForm(obj = assign_student)
    if form.validate_on_submit():
        form.populate_obj(assign_student)
        db.session.commit()
        return redirect(url_for("assign_students.get_assign_students_to_group_list"))
    return render_template("add_assign_student.html", form = form)

@assign_students_bp.route("/delete_assign_student/<int:id>", methods = ["POST"])
def delete_assign_student(id):
    assign_student = Assign_Students.query.get_or_404(id)
    db.session.delete(assign_student)
    db.session.commit()
    return redirect(url_for("assign_students.get_assign_students_to_group_list"))

@assign_students_bp.route("/delete_all_assign_students", methods = ["POST"])
def delete_all_assign_students():
    Assign_Students.query.delete()
    db.session.commit()
    return redirect(url_for("assign_students.get_assign_students_to_group_list"))