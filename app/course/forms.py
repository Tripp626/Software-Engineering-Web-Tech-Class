from flask_wtf import *
from wtforms import *
from wtforms.validators import *
from app.program.models import Program
from app.level.models import Level

class CourseForm(FlaskForm):
    id = HiddenField("id")
    program_id = SelectField("Select Program")
    level_id = SelectField("Select Level")
    name  = StringField("Course Name:", validators = [DataRequired()])
    code  = StringField("Course Code:", validators = [DataRequired()])
    submit = SubmitField("Save Changes")

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.program_id.choices = [(program.id, program.name)for program in Program.query.all()]
        self.level_id.choices = [(level.id, level.name)for level in Level.query.all()]