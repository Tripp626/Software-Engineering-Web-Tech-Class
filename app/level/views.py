from flask import *
from app.level import level_bp
from app.level.forms import LevelForm
from app.level.models import Level
from app import db

@level_bp.route("/level_list", methods = ["GET"])
def get_level_list():
    level = Level.query.all()
    return render_template("list_level.html", lv = level)

@level_bp.route("/add_level", methods = ["GET", "POST"])
def add_level():
    forms = LevelForm()
    if forms.validate_on_submit():
        level_name = forms.name.data
        level_code = forms.code.data

        new_level = Level(name = level_name, code = level_code)
        db.session.add(new_level)
        db.session.commit()
        return redirect(url_for("level.get_level_list"))

    return render_template("add_level.html", form = forms)


@level_bp.route("/delete_level/<int:id>", methods = ["POST"])
def delete_level(id):
    level = Level.query.get_or_404(id)
    db.session.delete(level)
    db.session.commit()
    return redirect(url_for("level.get_level_list"))

@level_bp.route("/edit_level/<int:id>", methods = ["GET", "POST"])
def update_level(id):
    level = Level.query.get_or_404(id)
    form = LevelForm(obj = level)
    if form.validate_on_submit():
        form.populate_obj(level)
        db.session.commit()
        return redirect(url_for("level.get_level_list"))
    return render_template("add_level.html", form = form)

@level_bp.route("/delete_all_level", methods = ["POST"])
def delete_all_level():
    Level.query.delete()
    db.session.commit()
    return redirect(url_for("level.get_level_list"))