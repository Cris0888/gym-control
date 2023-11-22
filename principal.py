from flask import Flask,render_template,request,redirect,session
from flaskext.mysql import MySQL
aplicacion=Flask(__name__)
mysql=MySQL()
aplicacion.config['MYSQL_DATABASE_HOST']= 'localhost'
aplicacion.config['MYSQL_DATABASE_PORT']=3306
aplicacion.config['MYSQL_DATABASE_USER']= 'root'
aplicacion.config['MYSQL_DATABASE_PASSWORD']= ''
aplicacion.config['MYSQL_DATABASE_DB']= 'gym_control'
mysql.init_app(aplicacion)
@aplicacion.route("/")
def inicio():
    return render_template("principal.html")
@aplicacion.route("/agregar")
def agregar():
    return render_template('/agregar.html')

@aplicacion.route("/principal")
def principal():
    return render_template("/principal.html")

@aplicacion.route("/mostrar")
def mostrar():
    return render_template('/mostrar.html')


@aplicacion.route('/create',methods=['POST'])
def create():
    nombre=request.form['nombre']
    estado=request.form['estado']
    sql=f"INSERT INTO categoria_productos (nombre,estado) VALUES ('{nombre}','{estado}')"
    con=mysql.connect()
    cur=con.cursor()
    cur.execute(sql)
    con.commit()
    return render_template("/agregar.html", alias=nombre)

@aplicacion.route("/buscar", methods=['GET'])
def buscar():
    sql=f"SELECT  id_categoria,nombre,estado FROM categoria_productos WHERE estado = 'activo'"
    con=mysql.connect()
    cur=con.cursor()
    cur.execute(sql)
    resultado=cur.fetchall()
    con.commit()
    return render_template('/mostrar.html', mostrar= resultado)


if __name__=='__main__':
    aplicacion.run(debug=True ,host="0.0.0.0", port=8080 )


mysql.init_app(aplicacion)

@aplicacion.route("/estado")
def estado():
    return render_template("/estado.html")