from flask import url_for, render_template, redirect, flash, request
from tutoriales import db, app
from tutoriales.forms import EstudianteForm, CarreraForm

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/crearCarrera', methods=['GET', 'POST'])
def crearCarrera():
    form = CarreraForm()
    if request.method == 'POST' and form.validate_on_submit():
        try:
            identificacion = form.identificacion.data
            nombre = form.nombre.data
            extension = form.extension.data

            args = (identificacion, nombre, extension)
            cursor = db.connection.cursor()
            cursor.callproc('crearCarrera', args)
            db.connection.commit()
            cursor.close()

            flash(f'Ha creado de manera correcta la carrera de {form.nombre.data}!', 'success')
            return redirect(url_for('verCarreras'))
        except:
            flash(f'No ha creado la carrera de manera correcta', 'danger')
            return redirect(url_for('verCarreras'))

    return render_template('crearCarrera.html', form = form)

@app.route('/carreras', methods=['GET', 'POST'])
def verCarreras():
    cursor = db.connection.cursor()
    cursor.callproc('verCarreras')
    data = cursor.fetchall()
    return render_template('carreras.html', carreras = data)

@app.route('/carrera/<int:id_carrera>', methods=['GET', 'POST'])
def verCarrera(id_carrera):
    cursor = db.connection.cursor()
    cursor.callproc('verCarrera', [id_carrera])
    datos = cursor.fetchone()
    return render_template('verCarrera.html', carrera = datos)

def modificar():
    pass

@app.route('/carrera/<int:id_carrera>/eliminar', methods=['GET', 'POST'])
def eliminarCarrera(id_carrera):
    cursor = db.connection.cursor()
    cursor.callproc('eliminarCarrera', [id_carrera])
    db.connection.commit()
    return redirect(url_for('verCarreras'))