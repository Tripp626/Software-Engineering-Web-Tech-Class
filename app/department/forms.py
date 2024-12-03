from flask_wtf import *
from wtforms import *
from wtforms.validators import *
from app.faculty.models import Faculty

class DepartmentForm(FlaskForm):
    id = HiddenField("id")
    faculty_id = SelectField("Select Faculty")
    name  = StringField("Department Name:", validators = [DataRequired()])
    code  = StringField("Department Code:", validators = [DataRequired()])
    submit = SubmitField("Save Changes")

    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)
        self.faculty_id.choices = [(faculty.id, faculty.name)for faculty in Faculty.query.all()]