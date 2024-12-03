from flask import *
from app.course import course_bp
from app.course.models import Course
from app.course.forms import CourseForm
from app import db

@course_bp.route("/course_list", methods = ["GET"])
def get_course_list():
    course = Course.query.all()
    return render_template("list_course.html", cs = course)

@course_bp.route("/add_course", methods = ["GET", "POST"])
def add_courses():
    forms = CourseForm()
    if forms.validate_on_submit():
        program_id = forms.program_id.data
        level_id = forms.level_id.data
        course_name = forms.name.data
        course_code = forms.code.data

        new_course = Course(program_id = program_id, level_id = level_id, name = course_name, code = course_code)
        db.session.add(new_course)
        db.session.commit()
        return redirect(url_for("course.get_course_list"))

    return render_template("add_course.html", form = forms)

@course_bp.route("/update_course/<int:id>", methods = ["GET", "POST"])
def update_course(id):
    course = Course.query.get_or_404(id)
    form = CourseForm(obj = course)
    if form.validate_on_submit():
        form.populate_obj(course)
        db.session.commit()
        return redirect(url_for("course.get_course_list"))
    return render_template("add_course.html", form = form)

@course_bp.route("/delete_course/<int:id>", methods = ["POST"])
def delete_course(id):
    course = Course.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()
    return redirect(url_for("course.get_course_list"))

@course_bp.route("/delete_all_courses", methods = ["POST"])
def delete_all_courses():
    Course.query.delete()
    db.session.commit()
    return redirect(url_for("course.get_course_list"))