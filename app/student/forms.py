from flask_wtf import *
from wtforms import *
from wtforms.validators import *
from app.program.models import Program

class StudentForm(FlaskForm):
    id = HiddenField("id")
    program_id = SelectField("Select Program")
    name  = StringField("Student Name:", validators = [DataRequired()])
    code  = StringField("Student Code:", validators = [DataRequired()])
    submit = SubmitField("Save Changes")

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.program_id.choices = [(program.id, program.name)for program in Program.query.all()]