class Clima:
    def __init__(self):
        self.codigo = []
        self.ciudad = []
        self.temp_minima = []
        self.temp_maxima = []
        self.estado = []

    def menu(self):
        opciones = """
        *********SISTEMA DE GESTION CLIMA********
        1.- REGISTRAR DEPARTAMENTO
        2.- MOSTRAR DEPARTAMENTOS
        3.- DEPARTAMENTOS CON TEMPERATURA BAJA
        4.- DEPARTAMENTOS CON TEMPERATURA ALTA
        5.- PROMEDIO DE LAS TEMPERATURAS MAXIMAS
        6.- SALIR
        """

        print(opciones)
        eleccion = int(input("Elija una opcion del menu: \n"))
        if (eleccion == 1):
            print(self.registrarDepartamento())
            self.verMenu()
        elif (eleccion == 2):
            print(self.descripdepar())
            self.verMenu()
        elif (eleccion == 3):
            print(self.verTempBaja())
            self.verMenu()
        elif (eleccion == 4):
            print(self.verTempAlta())
            self.verMenu()
        elif (eleccion == 5):
            print(self.promedio())
            self.verMenu()
        elif (eleccion == 6):
            Print("Registros realizados correctamente")
        else:
            print("***DIGITE UNA OPCION DEL MENU***")
            self.menu

    def verMenu(self):
        eleccion = input("Desea volver al menu: y/n \n")
        if (eleccion == 'y' or eleccion == 'Y'):
            self.menu()
        else:
            return "Registros realizados correctamente"
    
    def registrarDepartamento(self):
        codigo = input("CODIGO DEL DEPARTAMENTO: \n")
        ciudad = input("Nombre del departamento: \n")
        temp_minima = int(input("Temperatura Minima: \n"))
        temp_maxima = int(input("Temperatura Maxima: \n"))
        print(self.guardar(codigo, ciudad, temp_minima, temp_maxima))
        agregarOtro = input("Desea agregar otro Departamento? y/n \n")
        if (agregarOtro == 'y' or agregarOtro == 'Y'):
            self.registrarDepartamento()
        return "Departamentos registrados exitosamente"

    def guardar(self, codigo, ciudad, temp_minima, temp_maxima):
        self.codigo.append(codigo)
        self.ciudad.append(ciudad)
        self.temp_minima.append(temp_minima)
        self.temp_maxima.append(temp_maxima)
        self.estado.append(1)
        return "La ciudad {} fue regitrada exitosamente.!".format(ciudad)
    
    def descripdepar(self):
        if (self.codigo):
            for posicion in range(len(self.ciudad)):
                self.descripcion(posicion)
            return "Registrado correctamente"
        else:
            return "Todavia no datos registrados"

    def descripcion(self, posicion):
        print("****Descripcion del Departamento {}****".format(self.ciudad[posicion]))
        print("Codigo del departamento: {}".format(self.codigo[posicion]))
        print("Temperatura Baja: {}".format(self.temp_minima[posicion]))
        print("Temperatura Alta: {}".format(self.temp_maxima[posicion]))
    
    def verTempAlta(self):
        print("********DEPARTAMENTOS CON TEMPERATURAS ALTAS********")
        maxima = self.temp_maxima
        if (maxima >= self.temp_maxima):
            print("****Descripcion del Departamento {}****".format(self.ciudad))
            print("Las temperaturas mas Altas es: {}".format(maxima))
            pass

    def verTempBaja(self):
        print("********DEPARTAMENTOS CON TEMPERATURAS BAJAS********")
        minima = self.temp_minima
        if (minima <= self.temp_minima):
            print("****Descripcion del Departamento {}****".format(self.ciudad))
            print("Las temperaturas mas Bajas es: {}".format(minima))
            pass

    def promedio(self):
        lista = self.temp_maxima
        promed1 = sum(lista)/len(lista)
        print("El promedio de las temperaturas maximas es: {}".format(promed1))
        pass


clima = Clima()
clima.guardar(1, "SANTA CRUZ", 15, 29)
clima.guardar(2, "BENI", 17, 31)
clima.guardar(3, "PANDO", 18, 30)
clima.guardar(4, "LA PAZ", 1, 13)
clima.guardar(5, "ORURO", 2, 15)
clima.guardar(6, "POTOSI", 2, 14)
clima.guardar(7, "CBBA", 5, 18)
clima.guardar(8, "SUCRE", 9, 23)
clima.guardar(9, "TARIJA", 10, 25)
clima.menu()