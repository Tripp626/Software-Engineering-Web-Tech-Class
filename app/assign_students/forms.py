from flask_wtf import *
from wtforms import *
from wtforms.validators import *
from app.student.models import Student
from app.group.models import Group

class AssignStudentForm(FlaskForm):
    id = HiddenField("id")
    student_id = SelectField("Select Student")
    group_id = SelectField("Select Group")
    submit = SubmitField("Save Changes")

    def __init__(self, *args, **kwargs):
        super(AssignStudentForm, self).__init__(*args, **kwargs)
        self.student_id.choices = [(student.id, student.name)for student in Student.query.all()]
        self.group_id.choices = [(group.id, group.name)for group in Group.query.all()]