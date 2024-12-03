from flask import *
from app.faculty import faculty_bp
from app.faculty.forms import FacultyForm
from app.faculty.models import Faculty
from app import db

@faculty_bp.route("/faculty_list", methods = ["GET"])
def get_faculty_list():
    faculty = Faculty.query.all()
    return render_template("list_faculty.html", fac = faculty)

@faculty_bp.route("/add_faculty", methods = ["GET", "POST"])
def add_faculty():
    forms = FacultyForm()
    if forms.validate_on_submit():
        faculty_name = forms.name.data
        faculty_code = forms.code.data

        new_faculty = Faculty(name = faculty_name, code = faculty_code)
        db.session.add(new_faculty)
        db.session.commit()
        return redirect(url_for("faculty.get_faculty_list"))

    return render_template("add_faculty.html", form = forms)


@faculty_bp.route("/delete_faculty/<int:id>", methods = ["POST"])
def delete_faculty(id):
    faculty = Faculty.query.get_or_404(id)
    db.session.delete(faculty)
    db.session.commit()
    return redirect(url_for("faculty.get_faculty_list"))

@faculty_bp.route("/edit_faculty/<int:id>", methods = ["GET", "POST"])
def update_faculty(id):
    faculty = Faculty.query.get_or_404(id)
    form = FacultyForm(obj = faculty)
    if form.validate_on_submit():
        form.populate_obj(faculty)
        db.session.commit()
        return redirect(url_for("faculty.get_faculty_list"))
    return render_template("add_faculty.html", form = form)

@faculty_bp.route("/delete_all_faculty", methods = ["POST"])
def delete_all_faculty():
    Faculty.query.delete()
    db.session.commit()
    return redirect(url_for("faculty.get_faculty_list"))
