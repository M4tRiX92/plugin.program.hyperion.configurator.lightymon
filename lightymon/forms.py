"""Form object declaration."""
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    DateField,
    PasswordField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import URL, DataRequired, Email, EqualTo, Length

class SetLEDForm(FlaskForm):
    """Set LEDs for a Lightymon instance."""
    hled = StringField(
        "hled",
        [DataRequired()]
    )
    vled = StringField(
        "vled",
        [DataRequired()]
    )
    options = SelectField(
        "Options",
        [DataRequired()],
         choices=[
            ('Left', 'left'),
            ('Right', 'right'),
            ('Center to left', 'center_left'),
            ('Center to right', 'center_right')
        ],
    )
    submit = SubmitField("Submit")
