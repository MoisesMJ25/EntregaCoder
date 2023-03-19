import sys
datos_cliente = sys.argv

if len(datos_cliente) != 6:
    print("Error. Porfavor ingrese la información correcta")
else:
    print(f"Bienvenido {datos_cliente[1]} de {datos_cliente[4]}")

class Cliente: #Creación de la clase clientes
    tipo = "persona"
    def __init__(self, nombre, cedula, correo, pais, edad):
        self.nombre = nombre
        self.cedula = cedula
        self.correo = correo
        self.pais = pais
        self.edad = edad

    def __str__(self): # Uso de la función str
        return f"Nombre: {self.nombre}\nCédula: {self.cedula}\nCorreo: {self.correo}\nPaís: {self.pais}\nEdad: {self.edad}"

    def grupo_edad(self): # función para separar por rango de edades
        if self.edad < 18:
            return "El cliente {} es menor de edad".format(self.nombre)
        return f"El cliente {self.nombre} es mayor de edad"

def registrar(self):
    return f"Cliente regitrado en {self.pais}"

def comprar(self):
    return f"La compra ha sido exitosa, su comprobante llegará al correo: {self.correo}"