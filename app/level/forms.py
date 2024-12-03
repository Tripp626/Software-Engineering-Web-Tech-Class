from flask_wtf import *
from wtforms import *
from wtforms.validators import *

class LevelForm(FlaskForm):
    id = HiddenField("id")
    name  = StringField("Level Name:", validators = [DataRequired()])
    code  = StringField("Level Code:", validators = [DataRequired()])
    submit = SubmitField("Save Changes")