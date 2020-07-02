from wtforms import StringField, SubmitField, SelectField 
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length

class SearchForm(FlaskForm):
    seed = StringField('Seed')
    #'''
    dropdown_choices = [('0','The Picture of Dorian Gray'),
    						('1','Pride and Prejudice'),
    						('2','A Take of Two Cities'),
    						('3','The Brothers Karamazov'),
    						('4','The Souls of Black Folk')]
    #'''
    book = SelectField('Book', choices=dropdown_choices)
    submit = SubmitField('Submit')