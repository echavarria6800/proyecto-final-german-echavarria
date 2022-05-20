from werkzeug.security import check_password_hash , generate_password_hash
from flask_login import UserMixin


class UserCuenta(UserMixin):
   #Clase constructora con init
    def __init__(self, id, username, password, fullname="", cuenta ="" ,cedula="",tipocuenta="",saldo=0) -> None:
        self.id= id
        self.username = username
        self.password = password
        self.fullname = fullname
        self.cuenta = cuenta
        self.cedula = cedula
        self.tipocuenta= tipocuenta
        self.saldo=saldo

    @classmethod 
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

   # print(generate_password_hash("1234"))
# Para generar una nueva clave de tipo hash  python .\src\models\entities\UserCuenta.py