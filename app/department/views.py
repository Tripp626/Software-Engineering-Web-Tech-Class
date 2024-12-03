from flask import *
from app.department import department_bp
from app.department.models import Department
from app.department.forms import DepartmentForm
from app import db

@department_bp.route("/department_list", methods = ["GET"])
def get_department_list():
    department = Department.query.all()
    return render_template("list_department.html" ,dp = department)

@department_bp.route("/add_department", methods = ["GET", "POST"])
def add_departments():
    forms = DepartmentForm()
    if forms.validate_on_submit():
        faculty_id = forms.faculty_id.data
        department_name = forms.name.data
        department_code = forms.code.data

        new_department = Department(faculty_id = faculty_id, name = department_name, code = department_code)
        db.session.add(new_department)
        db.session.commit()
        return redirect(url_for("department.get_department_list"))

    return render_template("add_department.html", form = forms)

@department_bp.route("/update_department/<int:id>", methods = ["GET", "POST"])
def update_department(id):
    department = Department.query.get_or_404(id)
    form = DepartmentForm(obj = department)
    if form.validate_on_submit():
        form.populate_obj(department)
        db.session.commit()
        return redirect(url_for("department.get_department_list"))
    return render_template("add_department.html", form = form)

@department_bp.route("/delete_department/<int:id>", methods = ["POST"])
def delete_department(id):
    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    return redirect(url_for("department.get_department_list"))

@department_bp.route("/delete_all_departments", methods = ["POST"])
def delete_all_departments():
    Department.query.delete()
    db.session.commit()
    return redirect(url_for("department.get_department_list"))