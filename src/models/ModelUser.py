from .entities.UserCuenta import UserCuenta

class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, username, password, fullname, nrocuenta, nrocedula, tipocuenta, saldocuenta FROM tbl_cuenta
                    WHERE username = '{}'""".format(user.username)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = UserCuenta(row[0], row[1], UserCuenta.check_password(row[2], user.password), row[3], row[4], row[5], row[6], row[7])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, username, fullname, nrocuenta, nrocedula, tipocuenta, saldocuenta FROM tbl_cuenta WHERE id = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return UserCuenta(row[0], row[1], None, row[2],row[3],row[4],row[5], row [6])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
