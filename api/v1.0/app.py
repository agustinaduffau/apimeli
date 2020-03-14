#!flask/bin/python
from flask import Flask, jsonify 

import subprocess

salida = []

# uname -p =  Información sobre el procesador.
procesador = subprocess.check_output(['uname', '-p'])
salida.append(str(procesador.decode()))

# ps =  Listado de procesos corriendo.
procesos = subprocess.check_output('ps')
salida.append(str(procesos.decode()))

# who = Usuarios con una sesión abierta en el sistema.
sesiones = subprocess.check_output('who')
salida.append(str(sesiones.decode()))

# uname = Nombre del sistema operativo.
so = subprocess.check_output('uname')
salida.append(str(so.decode()))

# uname -o = Versión del sistema operativo.
version = subprocess.check_output(['uname', '-o'])
salida.append(str(version.decode()))

# conectarse al endpoint y enviar salida para su posterior procesamiento

print(salida)


app = Flask(__name__)

infoserver = [
    {
        'Información sobre el procesador': salida[0],
        'Listado de procesos corriendo': salida[1],
        'Usuarios con sesion abierta': salida[2],
 	'Nombre del SO': salida[3],
	'Version_SO': salida[4],
    }
    
]


@app.route('/')
def index():
	return "HELLO WORLD"

@app.route('/apimeli/api/v1.0/')
def create_infoserver():

    return jsonify(infoserver)

if __name__ == "__main__":
	app.run(debug=True)