
conexion=mysql.connect()
cursor=conexion.cursor()

metodos = Principal (mysql)
class Principal:
    def __init__(self,mysql):
        self.mysql =mysql
        self.conexion=self.mysql.connect()
        self.cursor=self.conexion.cursor()

    def crear(self,nom):
        sql=f"INSERT INTO categoria_productos(nombre,estado) VALUES ('{nom[0]}','{nom[1]}')"
        self.cursor.execute(sql)
        self.conexion.commit()
        metodos.crear([nombre,estado])

            

