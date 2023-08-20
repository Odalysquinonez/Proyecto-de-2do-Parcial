# INTEGRANTES:
# MERO SARCOS CAROLINE THALIA
# QUIÑONEZ JAIME SERGIO AURELIO
# QUIÑONEZ RONQUILLO ODALYS RAQUEL

from datetime import datetime
from sqlite3 import ProgrammingError

from _sqlite3 import IntegrityError

from datos.conexion import Conexion
from dominio.Estudiante import Estudiante


class Estudiantes:
    pass


class EstudianteDao:
    _INSERTAR = "insert into Estudiantes (cedula,nombre,apellido,email,carrera,activo,estatura,f_nacimiento," \
                "peso) values (?,?,?,?,?,?,?,?,?)"
    _SELECCIONAR_X_CEDULA = "select id,cedula,nombre,apellido,email,carrera,activo,estatura,f_nacimiento,peso from Estudiantes where cedula = ? "
    _SELECCIONAR = "select id,cedula,nombre,apellido,email,carrera,activo, estatura,f_nacimiento, peso from Estudiantes"
    _N_EDADES = 'SELECT edad FROM Estudiantes'

    @classmethod
    def insertar_estudiante(cls, estudiante):
        respuesta = {"exito": False, "mensaje": ""}
        flag_exito = False
        mensaje = ""
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (
                    estudiante.cedula, estudiante.nombre, estudiante.apellido, estudiante.email, estudiante.carrera,
                    estudiante.activo, estudiante.estatura, estudiante.fecha_nacimiento, estudiante.peso)
                cursor.execute(cls._INSERTAR, datos)

                edad = cls.calcular_edad(estudiante.fecha_nacimiento)
                cursor.execute("UPDATE Estudiantes SET edad = ? WHERE cedula = ?", (edad, estudiante.cedula))

                flag_exito = True
                mensaje = "INGRESO EXITOSO"
        except IntegrityError as e:
            flag_exito = False

            if e.__str__().find("Cedula") > 0:
                print("CEDULA YA INGRESADA.")
                mensaje = "cedula ya ingresada"
            elif e.__str__().find("Email") > 0:
                print("EMAIL YA INGRESADA.")
                mensaje = "email ya ingresada"
            else:
                print("ERROR DE INTEGRIDAD")
                mensaje = "Error de integridad"
        except ProgrammingError as e:
            flag_exito = False
            print("Los datos Ingresados no son del tamaño permitido")
            mensaje = "Los datos Ingresados no son del tamaño permitido"
        except Exception as e:
            flag_exito = False
            print(e)
        finally:
            respuesta["exito"] = flag_exito
            respuesta["mensaje"] = mensaje
            return respuesta

    @classmethod
    def seleccionar_por_cedula(cls, estudiante):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (estudiante.cedula,)
                resultado = cursor.execute(cls._SELECCIONAR_X_CEDULA, datos)
                persona_encontrada = resultado.fetchone()

                if persona_encontrada is not None:
                    estudiante.id = persona_encontrada[0]
                    estudiante.cedula = persona_encontrada[1]
                    estudiante.nombre = persona_encontrada[2]
                    estudiante.apellido = persona_encontrada[3]
                    estudiante.email = persona_encontrada[4]
                    estudiante.carrera = persona_encontrada[5]
                    estudiante.activo = persona_encontrada[6]
                    estudiante.estatura = persona_encontrada[7]
                    estudiante.fecha_nacimiento = persona_encontrada[8]
                    estudiante.peso = persona_encontrada[9]
        except Exception as e:
            print(e)
        finally:
            return estudiante

    @classmethod
    def seleccionar_estudiantes(cls):
        lista_estudiantes = list()
        try:
            with Conexion.obtenerCursor() as cursor:
                resultado = cursor.execute(cls._SELECCIONAR)
                for tupla_estudiante in resultado.fetchall():
                    estudiante = Estudiante()
                    estudiante.id = tupla_estudiante[0]
                    estudiante.cedula = tupla_estudiante[1]
                    estudiante.nombre = tupla_estudiante[2]
                    estudiante.apellido = tupla_estudiante[3]
                    estudiante.email = tupla_estudiante[4]
                    estudiante.carrera = tupla_estudiante[5]
                    estudiante.activo = tupla_estudiante[6]
                    estudiante.estatura = tupla_estudiante[7]
                    estudiante.fecha_nacimiento = tupla_estudiante[8]
                    estudiante.peso = tupla_estudiante[9]
                    lista_estudiantes.append(estudiante)
        except Exception as e:
            lista_estudiantes = None
        finally:
            return lista_estudiantes


    @classmethod
    def calcular_edad(cls, fecha_nacimiento):
        try:
            birthdate = datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date()
            today = datetime.today().date()
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            return age
        except Exception as e:
            print(f'Error al calcular la edad: {str(e)}')
            return None


    @classmethod
    def obtener_edades_todos_estudiantes(cls):
        tedades = []
        try:
            with Conexion.obtenerCursor() as cursor:
                resultado = cursor.execute(cls._N_EDADES)
                tedades = [tupla_estudiante[0] for tupla_estudiante in resultado.fetchall()]
        except Exception as e:
            print(e)
        finally:
            return tedades


if __name__ == '__main__':
    estudiantes = EstudianteDao.seleccionar_estudiantes()
    for estudiante in estudiantes:
        #Los numeros son para alinear el cuadro

        class Colors: #codigo para imprimir el color
            HEADER = '\033[95m'
            BLUE = '\033[94m'
            GREEN = '\033[92m'
            YELLOW = '\033[93m'
            RED = '\033[91m'
            ENDC = '\033[0m'


        print(Colors.ENDC + "╔═════════════════════════════════════════╗" + Colors.ENDC)
        print(Colors.HEADER + "║  ID:       " + str(estudiante.id) + " " * (
                    29 - len(str(estudiante.id))) + "║" + Colors.ENDC)
        print(
            Colors.HEADER+ "║  Cédula:   " + estudiante.cedula + " " * (29 - len(estudiante.cedula)) + "║" + Colors.ENDC)
        print(
            Colors.HEADER + "║  Nombre:   " + estudiante.nombre + " " * (29 - len(estudiante.nombre)) + "║" + Colors.ENDC)
        print(Colors.HEADER + "║  Apellido: " + estudiante.apellido + " " * (
                    29 - len(estudiante.apellido)) + "║" + Colors.ENDC)
        print(Colors.HEADER + "║  Email:    " + estudiante.email + " " * (29 - len(estudiante.email)) + "║" + Colors.ENDC)
        print(Colors.HEADER + "║  Carrera:  " + estudiante.carrera + " " * (
                    29 - len(estudiante.carrera)) + "║" + Colors.ENDC)
        print(Colors.HEADER + "║  Estatura: " + str(estudiante.estatura) + " " * (
                    29 - len(str(estudiante.estatura))) + "║" + Colors.ENDC)
        print(Colors.HEADER + "║  Peso:     " + str(estudiante.peso) + " " * (
                    29 - len(str(estudiante.peso))) + "║" + Colors.ENDC)

        edad = EstudianteDao.calcular_edad(str(estudiante.fecha_nacimiento))
        if edad is not None:
            print(Colors.HEADER + "║  Edad:     " + str(edad) + " " * (29 - len(str(edad))) + "║" + Colors.ENDC)
        else:
            print(Colors.RED+ "║  Edad no disponible" + " " * 18 + "║" + Colors.ENDC)

        print(Colors.ENDC + "╚═════════════════════════════════════════╝" + Colors.ENDC)
