from viga import Viga
import formulas as fm
from math import pi, sin,  cos, sqrt
from numpy import arange

FORMAS_CIRCULARES=["circular solido","circular hueco"]
FORMAS_SOLIDAS=["circular solido","cuadrado solido"]
SALTO_PUNTO_CRITICO = 100

def main():
    #menu principal del programa
    viga = None
    fuerzas = []
    momentos = []
    deflexion = []

    while True:
        print("Que quieres hacer:")
        print("1. Crear nueva Viga")
        print("2. Abrir Viga predeterminada")
        print("")
        print("3. Agregar una Carga")
        print("4. Agregar Cargas predeterminadas")
        print("")
        print("5. Calcular Matriz de Tensiónes en un punto")
        print("6. Calcular Punto mas critico")
        print("")
        print("7. Calcular deflexión maxima (Solo Vigas con soportes en los extremos y carga en el centro)")
        print("8.")
        print("")
        print("9. Imprimir Viga y Cargas")
        print("0. cerrar programa")
        entrada=input(">")
        if entrada == "1":
            viga = crear_viga()

        elif entrada == "2":
            viga = leer_viga_predeterminada()

        elif entrada == "3":
            print("Que tipo de carga es(f o m)?")
            tipocarga = input(">")
            if tipocarga == "f":
                a = crear_fuerza()
                if a != -1:
                    fuerzas.append(a)
            elif tipocarga == "m":
                a = crear_momento()
                if a != -1:
                    momentos.append(a)
            else:
                print("input invalido")
                print("")
                print("")

        elif entrada == "4":
            cargas = leer_cargas()
            for carga in cargas:
                if carga["tipo"] == "f":
                    fuerzas.append((carga["posicion"],carga["vector"]))
                elif carga["tipo"] == "m":
                    momentos.append((carga["posicion"],carga["vector"]))
                elif carga["tipo"] == "t":
                    torsores.append((carga["posicion"],carga["vector"]))


        elif entrada == "5":
            print("ingresa posición del punto a evaluar (mm) separada por ',': x,y,z")
            n = [float(x)/1000 for x in input().split(",")]
            matriz_tension = [(fm.tension(viga, fuerzas, momentos, n[0], n[1], n[2])/1000000,
                               fm.esfuerzo_cortante_xy(viga, fuerzas, momentos, n[0], n[1], n[2])/1000000,
                               fm.esfuerzo_cortante_xz(viga, fuerzas, momentos, n[0], n[1], n[2])/1000000),
                               (fm.esfuerzo_cortante_xy(viga, fuerzas, momentos, n[0], n[1], n[2])/1000000,0,0),
                               (fm.esfuerzo_cortante_xz(viga, fuerzas, momentos, n[0], n[1], n[2])/1000000,0,0)]
            print("")
            sigma_vm = sqrt(matriz_tension[0][0]**2+3*((matriz_tension[0][1]**2)+(matriz_tension[0][2])**2))
            for x in matriz_tension:
                print(x)
            print("Mpa")
            print("")
            print("Tension Von Mises:,", sigma_vm ,"Mpa" )
            print("")


        elif entrada == "6":
            valores_obtenidos = set() #set con tuplas (tension, (x,y,z))
            if viga.perfil["perfil"] in FORMAS_CIRCULARES:
                for x1 in arange(0,viga.x,viga.x/SALTO_PUNTO_CRITICO):
                    for theta in arange(0, 2*pi, 2*pi/SALTO_PUNTO_CRITICO):
                        y1 = viga.r*cos(theta)
                        z1 = viga.r*sin(theta)
                        resultado = fm.tension(viga, fuerzas, momentos, x1, y1, z1)
                        valores_obtenidos.add((resultado,(x1,y1,z1)))
            else:
                pass


            maximo = max(valores_obtenidos, key = lambda x: x[0])
            minimo = min(valores_obtenidos, key = lambda x: x[0])

            print(f"Máximo = {maximo[0]/1000000} MPa; pos = {maximo[1]}")
            print(f"Míximo = {minimo[0]/1000000} MPa; pos = {minimo[1]}")

        elif entrada == "7":
            def_max = fm.deflexion_maxima(viga, fuerzas)
            def_max_mm = def_max*1000
            print(def_max_mm,"mm")


        elif entrada == "9":
            imprimir_datos(viga,fuerzas,momentos)
        elif entrada == "0":
            exit()
        else:
            print("input invalido")
            print("--------------")

def imprimir_datos(viga, fuerzas,momentos):
    print("Datos de la viga")
    print(viga)
    print("Datos de las fuerzas")
    for x in fuerzas:
        print(x)
    print("Datos de los momentos")
    for x in momentos:
        print(x)

def crear_fuerza():
    print("ingresa posición de la fuerza (m) separada por ',': x,y,z")
    n = [float(x) for x in input().split(",")]
    print("ingresa vector de la fuerza (N) separadas por ',': x,y,z")
    m = [float(x) for x in input().split(",")]
    print("Quieres crear una fuerza con los siguientes datos y/n?")
    print("posicion = ",n)
    print("vector   = ",m)
    a = input(">")
    if a =="y" or a =="Y":
        return (n,m)
    else:
        a=input("ingresa 0 para regresar, otro input para crear otra fuerza\n>")
        if a==0:
            return -1
        return crear_fuerza()

def crear_momento():
    print("ingresa posición del momento (m) separada por ',': x,y,z")
    n = [float(x) for x in input().split(",")]
    print("ingresa vector del momento (Nm) separadas por ',': x,y,z")
    m = [float(x) for x in input().split(",")]
    print("Quieres crear un momento con los siguientes datos y/n?")
    print("posicion = ",n)
    print("vector   = ",m)
    a = input(">")
    if a =="y" or a =="Y":
        return (n,m)
    else:
        a=input("ingresa 0 para regresar, otro input para crear otra fuerza\n>")
        if a==0:
            return -1
        return crear_momento()


def crear_viga():
    #Elegimos el material el tipo de perfil y las dimensiones de la viga
    print("Cual es el material de la viga")
    materiales=leer_materiales()
    for i,j in enumerate(materiales):
        print(str(i+1)+". "+str(j["material"]))
    entrada1=input(">")
    if not (entrada1.isnumeric()) or not (int(entrada1)in range(1,len(materiales)+1)):
        print("input invalido")
        print("--------------")
        valores_viga()
    material=materiales[int(entrada1)-1]


    print("cual es el perfil de la viga")
    perfiles=leer_perfiles()
    for i,j in enumerate(perfiles):
        print(str(i+1)+". "+str(j["perfil"]))
    entrada2=input(">")
    if not (entrada2.isnumeric()) or not (int(entrada2)in range(1,len(perfiles)+1)):
        print("input invalido")
        print("--------------")
        valores_viga()
    perfil=perfiles[int(entrada2)-1]

    x, y, z, r, t = 0, 0, 0, 0, 0
    print("cuales son las dimensiones de la viga:")
    x=float(input("Largo de la viga(mm): "))
    x=x/1000
    if perfil["perfil"] in FORMAS_CIRCULARES:
        r=float(input("radio de la viga(mm): "))
        r=r/1000
    else:
        y=float(input("ancho de la viga(mm):"))
        y=y/1000
        z=float(input("alto de la viga(mm):"))
        z=z/1000

    if not perfil["perfil"] in FORMAS_SOLIDAS:
        t=float(input("espesor de la viga(mm):"))
        t=t/1000

    return Viga(material,perfil,x,y,z,r,t)


def valores_estado():
    #agregamos las cargas a la que se encuentra expuesta la viga
    pass


def leer_materiales():
    #Lee el excel de los materiales
    materiales=[]
    with open ("materiales.csv","r") as file:
        file.readline()
        for line in file:
            line=line.strip("\n").split(";") #Creamos una lista
            materiales.append({"material":line[0],
                               "E":float(line[1]),
                               "G":float(line[2])})
    return materiales

def leer_perfiles():
    #lee el excel de los perfiles
    perfiles=[]
    with open ("perfiles.csv","r") as file:
        file.readline()
        for line in file:
            line=line.strip("\n").split(";") #Creamos una lista
            perfiles.append({"perfil":line[0],
                             "K":(line[1]),
                             "Q":(line[2]),
                             "At":(line[3]),
                             "Ix":(line[4]),
                             "Iy":(line[5]),
                             "Iz":(line[6]),
                             "J":(line[7])})
    return perfiles

def leer_cargas():
    cargas = []
    with open ("cargas.csv","r") as file:
        file.readline()
        for line in file:
            line=line.strip("\n").split(";") #Creamos una lista
            cargas.append({"tipo":line[0],
                             "posicion":[float(line[1])/1000,float(line[2])/1000,float(line[3])/1000],
                             "vector":[int(line[4]),int(line[5]),int(line[6])]})
    return cargas

def leer_viga_predeterminada():
    with open ("viga_predeterminada.csv","r") as file:
        file.readline()
        line = file.readline()
        line=line.strip("\n").split(";") #Creamos una lista
        viga = {"material":line[0],
                     "perfil":(line[1]),
                      "x":float(line[2])/1000,
                      "y":float(line[3])/1000,
                      "z":float(line[4])/1000,
                      "r":float(line[5])/1000,
                      "t":float(line[6])/1000}

        materiales = leer_materiales()
        for material in materiales:
            if material["material"] == viga["material"]:
                break
        perfiles = leer_perfiles()
        for perfil in perfiles:
            if perfil["perfil"] == viga["perfil"]:
                break

        return Viga(material,
                    perfil,
                    viga["x"],
                    viga["y"],
                    viga["z"],
                    viga["r"],
                    viga["t"])


main()
