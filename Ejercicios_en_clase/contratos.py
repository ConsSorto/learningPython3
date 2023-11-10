from abc import ABC, abstractclassmethod

class Utilidades:
    @staticmethod
    def calcular_impuesto(salario):
        if salario > 5000:
            return salario * 0.12
        else:
            return 500


class Persona:
    nombre = None
 
    def __init__(self, nombre):
        self.nombre = nombre
 
class Empleados(Persona):
    salario = None
    impuesto = None

    def __init__(self, nombre, salario):
        super().__init__(nombre)
        self.salario = salario
        self.impuesto = Utilidades.calcular_impuesto(salario)

class Estado:
    nombre = None
    fecha_inicio = None
    fecha_fin = None

    def __init__(self, nombre, fecha_inicio, fecha_fin):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

class Contrato(ABC):
    emp_responsable = None
    metros = None
    cliente = None
    fecha_inicio = None
    fecha_fin = None
    estado = None
    empleados = None
    precio = None
    utilidad = None

    def __init__(self, emp_responsable, metros, cliente, fecha_inicio, fecha_fin, estado, empleados):
        self.emp_responsable = emp_responsable
        self.metros = metros
        self.cliente = cliente
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado
        self.empleados = empleados

    def setear_precio(self):
        total = 0
        for empleado in self.empleados:
            total += empleado.salario
        
        self.precio= (self.emp_responsable.salario + total) * 2
    
    
    @abstractclassmethod
    def calcular_utilidad(self):
        pass


class AseoDomicilio(Contrato):
    lavado_planchado = None
    cocinar = None
    cantidad_banos = None
    cantidad_habitaciones = None

    def __init__(self, emp_responsable, metros, cliente, fecha_inicio, fecha_fin, estado, empleados, lavado_planchado, cocinar, cantidad_banos, cantidad_habitaciones):
        super().__init__(emp_responsable, metros, cliente, fecha_inicio, fecha_fin, estado, empleados)
        self.lavado_planchado = lavado_planchado
        self.cocinar = cocinar
        self.cantidad_banos = cantidad_banos
        self.cantidad_habitaciones = cantidad_habitaciones
    #utilidad para domicilio es 40% si hay mas de dos empleados en caso contrario 30%      
    
    def calcular_utilidad(self):
        print("entro")
        if len(self.empleados) > 2:
            print("entro condicion true")
            self.utilidad = self.precio * 0.40
        else:
            print("entro condicion false")
            self.utilidad = self.precio * 0.30
        print("finalizo")




class AseoEmpresarial(Contrato):
    mesero = None
    cantidad_banos = None
    cantidad_habitaciones = None
    quimicos = None
    
    def __init__(self, emp_responsable, metros, cliente, fecha_inicio, fecha_fin, estado, empleados, mesero, cantidad_banos, cantidad_habitaciones, quimicos):
        super().__init__(emp_responsable, metros, cliente, fecha_inicio, fecha_fin, estado, empleados)
        self.mesero = mesero
        self.quimicos = quimicos
        self.cantidad_banos = cantidad_banos
        self.cantidad_habitaciones = cantidad_habitaciones
       

cliente = Persona('Cliente Bueno')
empleadosR = Empleados('Responsable', 5000)
empleados = Empleados('Juan Perez', 1000)
empleados2 = Empleados('Pedro Sanchez', 5000)
empleados3 = Empleados('Ana Maria', 6000)

print(empleadosR.impuesto)
print(empleados3.impuesto)

#empleados = [empleados, empleados2, empleados3]
#empleados = [empleados]

empl = [empleados, empleados2, empleados3]

estado = Estado('Proceso', '20231108', '20231108')

aseo_domiciliario = AseoDomicilio(empleadosR, 10, cliente, '20231201', '20231215', estado, empl, True, True, 5, 4)

aseo_domiciliario.setear_precio()

for emplea in aseo_domiciliario.empleados:
    print(emplea.nombre)

aseo_domiciliario.calcular_utilidad()

print(aseo_domiciliario.precio)
print(aseo_domiciliario.utilidad)


"""
empleados = [empleados, empleados2, empleados3]


estado = Estado('Proceso', '20231108', '20231108')

aseo_domiciliario = AseoDomicilio(empleadosR, 10, cliente, '20231201', '20231215', estado, empleados, True, True, 5, 4)

aseo_empresarial = AseoEmpresarial(empleadosR, 10, cliente, '20231201', '20231215', estado, empleados, True, 5, True, 4)


print(f"Persona Responsable : {aseo_domiciliario.emp_responsable.nombre}, {aseo_domiciliario.emp_responsable.salario}")

print(aseo_domiciliario.estado.nombre)

print(aseo_domiciliario.cliente.nombre)

aseo_domiciliario.setear_precio()

print(aseo_domiciliario.precio)

print(aseo_empresarial)"""
