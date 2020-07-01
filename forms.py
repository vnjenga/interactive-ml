from wtforms import StringField, SubmitField, SelectField 
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length

class SearchForm(FlaskForm):
    seed = StringField('Seed')
    dropdown_choices = 
    book = SelectField('Book', choices=[(0,"The Picture of Dorian Gray"),(1,"WIP"),(2,"Lol")])
    submit = SubmitField('Submit')