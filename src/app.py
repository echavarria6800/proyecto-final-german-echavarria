from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required

from config import config

# Models:
from models.ModelUser import ModelUser

# Entities:
from models.entities.UserCuenta import UserCuenta

app = Flask(__name__)

csrf = CSRFProtect()
db = MySQL(app) #Conexión a la base de datos 
login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)


@app.route('/') #  ruta inicial
def index():#nombre de la vista
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST']) #ruta para los dos metodos
def login():
    if request.method == 'POST': 
        print(request.form['username'])
        print(request.form['password'])
        user = UserCuenta(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                print(logged_user)
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Contraseña incorrecta")
                return render_template('auth/login.html') #Acciones por GET
        else:
            flash("Este usuario no existe")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/home')
def home():
    return render_template('home.html')





def status_401(error):
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)

    app.run()
    


