from dni import *

# Nombre de la clase
class CuentaCorriente:
    """Representa a una Cuenta Corriente que nos permite almacenar los datos asociados a la cuenta bancaria
    de un cliente, e interactuar con ellos."""

    # Inicializador con sus atributos o propiedades establecidas

    def __init__(self, nombre="", apellido="",direccion="", telefono="",nif="", saldo=0.0):
        """inicializa una Cuenta Corriente con nombre, apellido, direccion, telefono,
        nif y saldo."""
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.nif = Dni()
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

    def setNif(self, nif):
        self.nif = nif

    def getNif(self):
        return self.nif

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



# Casos Test
if __name__ == '__main__':

#Casos Test sobre los set y get de las propiedades de la clase
   
    cuenta = CuentaCorriente()
    test = [[cuenta.getNombre(), ""],
    [cuenta.getApellido(), ""],
    [cuenta.getDireccion(), ""],
    #[cuenta.getNif, ""],
    [cuenta.getTelefono(), ""],
    [cuenta.getSaldo(), 0.0]]

    print ("Casos Test sobre los set y get de las propiedades de la clase")
    for miniTest in test:
        if miniTest[0] == miniTest[1]:
            print ('ok test correcto')
        else:
            print ('fail test')


    cuenta.setNombre("Diego")
    cuenta.setApellido("Vivanco")
    cuenta.setNif("45610975C")
    cuenta.setDireccion("Calle de la begonia")
    cuenta.setTelefono("59568456")
    cuenta.setSaldo(1200)

    print ("Casos Test sobre los set y get de las propiedades de la clase")    
    test = [[cuenta.getNombre(), "Diego"],
    [cuenta.getApellido(), "Vivanco"],
    [cuenta.getNif(), "45610975C"],
    [cuenta.getDireccion(), "Calle de la begonia"],
    [cuenta.getTelefono(), "59568456"],
    [cuenta.getSaldo(), 1200]]
    for miniTest in test:
        if miniTest[0] == miniTest[1]:
            print ('ok test correcto')
        else:
            print ('fail test')

    print ("\n")

###########################################################################################

#Casos Test retirarDinero()
        
    print ("Caso Test retirarDinero()")
    cuenta.setSaldo(100)
    cuenta.ingresarDinero(100)
    if cuenta.getSaldo() == 200:
        print ("ok test correcto")
    else:
        print ("fail test")

#Casos Test ingresarDinero()
    
    print ("Caso Test ingresarDinero()")
    cuenta.retirarDinero(100)
    if cuenta.getSaldo() == 100:
        print ("ok test correcto")
    else:
        print ("fail test")

    print ("\n")

###########################################################################################

#Casos Test saldoNegativo()
    print ("Caso Test saldoNegativo()")
    tuCuenta=CuentaCorriente()
    tuCuenta.setSaldo(100)
    cuenta.setSaldo(0)
    cuenta.retirarDinero(100)
    test = [[cuenta.saldoNegativo(), False],
    [tuCuenta.saldoNegativo(), True]]
    for miniTest in test:
        if miniTest[0]== miniTest[1]:
            print('ok test saldoNegativo')
        else:
            print('fail test saldoNegativo')

    print ("\n")

###########################################################################################

#Ejemplo de uso de la Clase CuentaCorriente
    cuenta.setSaldo(1200)
    cuenta.consultarCuenta()
    cantidadRetirada, dineroRestante = cuenta.retirarDinero(120)
    cantidadIngresada, dineroTotal = cuenta.ingresarDinero(180)

    print ("El retiro de", cantidadRetirada, "euros se ha efectuado correctamente, su saldo actual es:", dineroRestante)
    print ("El ingreso de", cantidadIngresada, "euros se ha efectuado correctamente, su saldo actual es:", dineroTotal)
    print ("El estado de la cuenta es:", cuenta.saldoNegativo())
