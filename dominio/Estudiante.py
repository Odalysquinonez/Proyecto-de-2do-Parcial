# INTEGRANTES:
# MERO SARCOS CAROLINE THALIA
# QUIÑONEZ JAIME SERGIO AURELIO
# QUIÑONEZ RONQUILLO ODALYS RAQUEL
from datetime import datetime

from dominio.Persona import Persona
class Estudiante(Persona):
    contador_estudiante = 0

    def __init__(self, cedula:str=None, nombre:str=None, apellido:str=None, email:str=None, telefono:str=None, direccion:str=None, numero_libros:int=0, activo:bool=True, carrera:str=None, nivel:str=None,estatura:int =0,fecha_nacimiento:datetime=None,peso:int=0,edad:int=None,mediana:int=0,moda:int=0):
        super().__init__(cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera,estatura,fecha_nacimiento,peso,edad,mediana,moda)
        self.fecha_nacimiento = fecha_nacimiento
        self.id = Estudiante.contador_estudiante + 1
        self._nivel = nivel
        Estudiante.contador_estudiante += 1

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, value):
        self._nivel = value


def lista_estudiantes():
    return None
#if __name__ == '__main__':
    #e1 = Estudiante(cedula='0932548449', nombre='joseph', apellido='paez', email='josephsamuelpaez@gmail.com',
                    #telefono='0984902300', direccion='mapasingue ', numero_libros=0, activo=True, carrera='GIG',
                    #nivel=3)
   # e2 = Estudiante(cedula='0915459077', nombre='viviana', apellido='caice', email='vcaicezuniga1978@gmail.com',
                   # telefono='0979512906', direccion='centro sur', numero_libros=0, activo=True, carrera='GIG',
                   # nivel=3)
    #e3 = Estudiante(cedula='0953509502', nombre='alejandra', apellido='barrera',
                   # email=' alejandrabarrera0207@gmail.com',
                   # telefono='0979262951', direccion='daule', numero_libros=0, activo=True, carrera='GIG',
                   # nivel=3)
   # e4 = Estudiante(cedula='0952308245', nombre='jamilet', apellido='pillasagua', email='jamifernanda@gmail.com',
                    #telefono='0989475023', direccion='sauces', numero_libros=0, activo=True, carrera='GIG',
                   # nivel=3)

    #print(e1)
   # print(e2)
   # print(e3)
    #print(e4)