class Metodos:
    def __init__(self,mysql):
        self.mysql=mysql
        self.conexion=self.mysql.connect()
        self.cursor=self.conexion.cursor()
        self.close=self.conexion.close()

    def crear(self,var):
        sql=f"INSERT INTO categoria_productos (nombre,estado) VALUES ('{var[0]}','{var[1]}')"
        self.cursor.execute(sql)
        self.conexion.commit()
        self.close
    def buscar(self,var):
        sql=f"SELECT id_categoria,nombre,estado FROM categoria_productos WHERE  	"
        
        