from flask_wtf import *
from wtforms import *
from wtforms.validators import *
from app.department.models import Department

class ProgramForm(FlaskForm):
    id = HiddenField("id")
    department_id = SelectField("Select Department")
    name  = StringField("Program Name:", validators = [DataRequired()])
    code  = StringField("Program Code:", validators = [DataRequired()])
    submit = SubmitField("Save Changes")

    def __init__(self, *args, **kwargs):
        super(ProgramForm, self).__init__(*args, **kwargs)
        self.department_id.choices = [(department.id, department.name)for department in Department.query.all()]