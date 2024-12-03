from flask import *
from app.program import program_bp
from app.program.models import Program
from app.program.forms import ProgramForm
from app import db

@program_bp.route("/program_list")
def get_program_list():
    program =Program.query.all()
    return render_template("list_program.html" ,pg = program)

@program_bp.route("/add_program", methods = ["GET", "POST"])
def add_programs():
    forms = ProgramForm()
    if forms.validate_on_submit():
        department_id = forms.department_id.data
        program_name = forms.name.data
        program_code = forms.code.data

        new_program = Program(department_id = department_id, name = program_name, code = program_code)
        db.session.add(new_program)
        db.session.commit()
        return redirect(url_for("program.get_program_list"))

    return render_template("add_program.html", form = forms)


@program_bp.route("/update_program/<int:id>", methods = ["GET", "POST"])
def update_program(id):
    program = Program.query.get_or_404(id)
    form = ProgramForm(obj = program)
    if form.validate_on_submit():
        form.populate_obj(program)
        db.session.commit()
        return redirect(url_for("program.get_program_list"))
    return render_template("add_program.html", form = form)

@program_bp.route("/delete_program/<int:id>", methods = ["POST"])
def delete_program(id):
    program = Program.query.get_or_404(id)
    db.session.delete(program)
    db.session.commit()
    return redirect(url_for("program.get_program_list"))

@program_bp.route("/delete_all_program", methods = ["POST"])
def delete_all_program():
    Program.query.delete()
    db.session.commit()
    return redirect(url_for("program.get_program_list"))