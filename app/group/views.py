from flask import *
from app.group import group_bp
from app.group.forms import GroupForm
from app.group.models import Group
from app import db

@group_bp.route("/group_list", methods = ["GET"])
def get_group_list():
    group = Group.query.all()
    return render_template("list_group.html", gp = group)

@group_bp.route("/add_group", methods = ["GET", "POST"])
def add_group():
    forms = GroupForm()
    if forms.validate_on_submit():
        group_name = forms.name.data
        group_code = forms.code.data

        new_group = Group(name = group_name, code = group_code)
        db.session.add(new_group)
        db.session.commit()
        return redirect(url_for("group.get_group_list"))

    return render_template("add_group.html", form = forms)

@group_bp.route("/delete_group/<int:id>", methods = ["POST"])
def delete_group(id):
    group = Group.query.get_or_404(id)
    db.session.delete(group)
    db.session.commit()
    return redirect(url_for("group.get_group_list"))

@group_bp.route("/edit_group/<int:id>", methods = ["GET", "POST"])
def update_group(id):
    group = Group.query.get_or_404(id)
    form = GroupForm(obj = group)
    if form.validate_on_submit():
        form.populate_obj(group)
        db.session.commit()
        return redirect(url_for("group.get_group_list"))
    return render_template("add_group.html", form = form)

@group_bp.route("/delete_all_group", methods = ["POST"])
def delete_all_group():
    Group.query.delete()
    db.session.commit()
    return redirect(url_for("group.get_group_list"))