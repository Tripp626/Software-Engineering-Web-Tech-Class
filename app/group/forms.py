from flask_wtf import *
from wtforms import *
from wtforms.validators import *

class GroupForm(FlaskForm):
    id = HiddenField("id")
    name  = StringField("Group Name:", validators = [DataRequired()])
    code  = StringField("Group Code:", validators = [DataRequired()])
    submit = SubmitField("Save Changes")