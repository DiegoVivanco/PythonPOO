from dni import *

# Nombre de la clase
class CuentaCorriente:
    """Representa a una Cuenta Corriente que nos permite almacenar los datos asociados a la cuenta bancaria
    de un cliente, e interactuar con ellos."""

    # Inicializador con sus atributos o propiedades establecidas
    def __init__(self):
        """inicializa una Cuenta Corriente con nombre, apellido, direccion, telefono, nif y saldo."""
        self.nombre = ""
        self.apellido = ""
        self.direccion = ""
        self.telefono = ""
        self.nif = NIF()
        self.saldo = float

    def __init__(self, nombre="", apellido="",direccion="", telefono="",nif="", saldo=0.0):
        """inicializa una Cuenta Corriente con nombre, apellido, direccion, telefono,
        nif y saldo."""
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.nif = NIF(cadena=nif)
        self.saldo = saldo

    # Utilización de setters and getters. Estos métodos especiales sirven para el manejo de las propiedades más importantes del objeto
    # Métodos set() y get() para todas las propiedades [Abstracción y encapsulamiento].
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def getApellido(self):
        return self.apellido

    def setDireccion(self, direccion):
        self.direccion = direccion

    def getDireccion(self):
        return self.direccion

    def setTelefono(self, telefono):
        self.telefono = telefono

    def getTelefono(self):
        return self.telefono

    def setNif(self, cadena):
        self.nif.setNif(cadena)

    def getNif(self):
        return self.nif.getNif()

    def getNifSano(self):
        return self.nif.getSano()

    def setNifSano(self, sano):
        self.nif.setSano(self, sano)

    def setSaldo(self, saldo):
        self.saldo = saldo

    def getSaldo(self):
        return self.saldo

# Comportamientos de la Cuenta Corriente

    def retirarDinero(self, cantidadRetirada):
        """ Efectua y regresa un calculo matemático, que es la resta"""
    
        #return self.getSaldo() - cantidadRetirada
        ###############################################################

        dineroRestante = (self.getSaldo() - cantidadRetirada)
        self.setSaldo(dineroRestante)
        return (cantidadRetirada, dineroRestante)

    def ingresarDinero(self, cantidadIngresada):
        """ Efectua y regresa un cálculo matemático, que es la suma"""
        
        #return self.getSaldo() + cantidadIngresada
        ###############################################################
        dineroTotal = (self.getSaldo() + cantidadIngresada)
        self.setSaldo(dineroTotal)
        return (cantidadIngresada, dineroTotal)

    def checkNif(self):
        self.nif.checkNif()

    def consultarCuenta(self):
        """ Nos da a conocer por pantalla los datos que tiene la cuenta"""

        print ("Cuenta Corriente de:", self.getNombre(), self.getApellido() ,"\nDNI: ", self.getNif())
        print ("Direccion de domicilio:", self.getDireccion(), "\nTelefono:", self.getTelefono())
        print ("Saldo Disponible:", self.getSaldo())

    def saldoNegativo(self):
        """ Analiza y devuelve un valor lógico mediante una condición establecida"""
        return self.getSaldo() > 0



class NIF(Dni):

    def __init__(self, cadena=""):
        Dni.__init__(self, cadena)

    def setNif(self, cadena=""):
        self.setDni(cadena)

    def getNif(self):
        self.getDni()

    def getSano(self):
        return self.sano

    def checkNif(self):
        self.checkDni()


if __name__ == '__main__':

    cuenta = CuentaCorriente()
    cuenta.setNif("45610975C")
    print ("Tu DNI es:", cuenta.getNif())
    cuenta.checkNif()
    print ("Se ha verificado que el DNI es:",cuenta.getNifSano())

    print ("\n\n")

    cuenta.setNombre("Diego")
    cuenta.setApellido("Vivanco")
    cuenta.setNif("45610975C")
    cuenta.setDireccion("Calle de la begonia")
    cuenta.setTelefono("59568456")
    cuenta.setSaldo(1200)
    cuenta.consultarCuenta()

    print ("\n")

    cantidadRetirada, dineroRestante = cuenta.retirarDinero(120)
    cantidadIngresada, dineroTotal = cuenta.ingresarDinero(180)

    print ("El retiro de", cantidadRetirada, "euros se ha efectuado correctamente, su saldo actual es:", dineroRestante)
    print ("El ingreso de", cantidadIngresada, "euros se ha efectuado correctamente, su saldo actual es:", dineroTotal)
    print ("El estado de la cuenta es:", cuenta.saldoNegativo())
