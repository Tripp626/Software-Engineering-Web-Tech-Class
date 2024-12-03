from flask import Blueprint

assign_students_bp = Blueprint("assign_students", __name__, template_folder = "templates", static_folder = "static")

from app.assign_students import views