class Empleado:
    _numero_empleado = None
    _nombre = None

    def __init__(self, numero_empleado, nombre):
        self._numero_empleado = numero_empleado
        self._nombre = nombre

class Administrativo(Empleado):
    puesto = None
    oficina = None

    def __init__(self, numero_empleado, nombre):
        super().__init__(numero_empleado, nombre)

class Docente(Empleado):
    departamento = None
    horario = None

    def __init__(self, numero_empleado, nombre):
        super().__init__(numero_empleado, nombre)
    
class Jefe(Administrativo, Docente):
    fecha_inicio = None
    fecha_fin = None
    bono = None

    def __init__(self, numero_empleado, nombre):
        super().__init__(numero_empleado, nombre)


jefe = Jefe(1234, 'Nestor')
jefe.fecha_inicio = "2020-07-01"
jefe.puesto = "Jefe de Sistemas"
jefe.departamento = "Ingenieria en Sistemas"

print(jefe._nombre)
print(jefe.fecha_inicio)
print(jefe.puesto)
print(jefe.departamento)