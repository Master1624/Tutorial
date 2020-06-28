from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, FileField, SelectField, validators
from wtforms.validators import DataRequired


class EstudianteForm(FlaskForm):
    identificacion = IntegerField('ID Estudiante', validators=[DataRequired()])
    nombre = StringField('Nombre del Estudiante', [DataRequired()])
    apellidos = StringField('Apellidos del Estudiante', [validators.DataRequired()])
    carrera = SelectField('Carreras', [DataRequired()])
    foto = FileField('Foto del estudiante', [DataRequired()])
    submit = SubmitField('Crear Estudiante')
    
class CarreraForm(FlaskForm):
    identificacion = IntegerField('ID Carrera', [validators.DataRequired(), validators.NumberRange(min=0, max=999999999)])
    nombre = StringField('Nombre de la Carrera', validators=[DataRequired()])
    extension = IntegerField('Extensión', validators=[DataRequired()])
    submit = SubmitField('Crear Carrera')
    modify = SubmitField('Modificar Carrera')