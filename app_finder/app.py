from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)   

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Ivanovichleo:FinderCard59:@Ivanovichleo.mysql.pythonanywhere-services.com/Finderbd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# modelos de usuarios
class Room(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(80), unique=True, nullable=False)
    
    def __repr__(self):
        return f'<User {self.username}>'



# enroutamiento
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        room_code = request.form['room_code']
        create_room = 'create_room' in request.form
        join_room = 'join_room' in request.form

        # Aquí puedes agregar la lógica para crear o unirse a una sala
        # Por ejemplo, podrías redirigir a diferentes páginas dependiendo de la acción seleccionada

        if create_room:
            New_room=Room(code=room_code)
            db.session.add(New_room)
            db.session.commit()
            # db.session.add(,)
            return f'Crear sala para {username} con el código {room_code}'
        elif join_room:
            return f'{username} se unirá a la sala con el código {room_code}'
        else:
            return 'Seleccione una opción válida.'

    return render_template('login.html')

@app.route('/Room', methods=['GET', 'POST'])
def room():

    return 'hola'

if __name__ == '__main__':
    app.run(debug=True)
