class Empleado:
    def __init__(self, nombre, cedula, salario):
        self.nombre = nombre
        self.cedula = cedula
        self.salario = salario

class Empleados:
    def __init__(self):
        self.empleados = []
        # Seeders
        self.nuevoEmpleado(nombre="Jose Perez", cedula="1234567", salario=1500)
        self.nuevoEmpleado(nombre="Ramiro Ramirez", cedula="3456789", salario=1600)
        self.nuevoEmpleado(nombre="Jose Gonzales", cedula="123400123", salario=1400)
        self.nuevoEmpleado(nombre="Jeaneth Flores", cedula="8347474", salario=1000)

    def nuevoEmpleado(self, **params):
        self.empleados.append(Empleado(**params))

    def nuevoEmpleadoJSON(self, data):
        self.nuevoEmpleado(nombre=data["nombre"], cedula=data["cedula"], salario=data["salario"])

    def listarEmpleados(self):
        return self.empleados

    def listarEmpleadosJSON(self):
        lista = []
        for item in self.empleados:
            lista.append({
                "nombre": item.nombre,
                "cedula": item.cedula,
                "salario": item.salario,
            })
        return lista

    def mostrarEmpleado(self, index):
        return self.empleados[index]

    def mostrarEmpleadoJSON(self, index):
        item = self.empleados[index]
        return {
            "nombre": item.nombre,
            "cedula": item.cedula,
            "salario": item.salario,
        }

    def editarEmpleado(self, index, **params):
        self.empleados[index] = Empleado(**params)

    def eliminarEmpleado(self, index):
        del self.empleados[index]

       
    def sumarSalario(self):
        total = 0
        for item in self.empleados:
                total += item.salario
        return total

