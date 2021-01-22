# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

   sudo pip install <package> -t .

"""
from telnetlib import Telnet

base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "Telnet" + os.sep + "libs" + os.sep
sys.path.append(cur_path)

module = GetParams("module")
global telcon_connection


class TelConnection(Telnet):
    def __init__(self, host, user, pwd, port=0):
        super().__init__(host, port)
        self.user = user
        self.pwd = pwd

    def connect(self):
        try:
            self.read_until(b"login: ")
            self.write(self.user.encode('ascii') + b"\n")
            if self.pwd:
                self.read_until(b"Password: ")
                self.write(self.pwd.encode('ascii') + b"\n")
        except Exception as e:
            PrintException()
            raise e


if module == "config":
    host = GetParams("host")
    user = GetParams("user")
    pwd = GetParams("password")
    port = GetParams("port")

    try:
        if not port:
            port = 0
        port = int(port)
        telcon_connection = TelConnection(host, user, pwd, port)
        telcon_connection.connect()
    except Exception as e:
        PrintException()
        raise e

if module == "read":
    result = GetParams("result")
    try:
        response = b" "
        try:
            while True:  # read until we stop
                message = telcon_connection.read_until(b'\n', timeout=0.1)
                response += message
                if message == b'':  # check if there was no data to read
                    break  # now we stop

        except EOFError:  # If connection was closed
            print('connection closed')

        SetVar(result, response.decode("ascii"))
    except Exception as e:
        PrintException()
        raise e

if module == "write":
    msg = GetParams("msg")
    try:
        msg = msg + "\n"
        telcon_connection.write(msg.encode('ascii'))
    except Exception as e:
        PrintException()
        raise e
