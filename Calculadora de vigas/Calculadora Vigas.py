from viga import Viga
import formulas as fm

FORMAS_CIRCULARES=["circular solido","circular hueco"]
FORMAS_SOLIDAS=["circular solido","cuadrado solido"]


def main():
    #menu principal del programa
    viga = None
    fuerzas = []
    momentos = []
    torsores = []

    while True:
        print("Que quieres hacer:")
        print("1. Crear nueva Viga")
        print("2. Agregar Fuerza")
        print("3. Agregar componentes de la tabla Elementos")
        print("5. Calcular Tensión")
        print("6. Calcular Deflexión")
        print("9. Imprimir Viga y Fuerzas")
        print("0. cerrar programa")
        entrada=input(">")
        if entrada == "1":
            viga = crear_viga()
        elif entrada == "2":
            a = crear_fuerza()
            if a != -1:
                fuerzas.append(a)

        elif entrada == "3":
            elementos = leer_elementos()
            for elemento in elementos:
                if elemento["tipo"] == "f":
                    fuerzas.append((elemento["posicion"],elemento["vector"]))
                elif elemento["tipo"] == "m":
                    momentos.append((elemento["posicion"],elemento["vector"]))
                elif elemento["tipo"] == "t":
                    torsores.append((elemento["posicion"],elemento["vector"]))


        elif entrada == "5":
            print("ingresa posición de la tensión (m) separada por ',': x,y,z")
            n = [float(x) for x in input().split(",")]
            print(fm.tension(viga, fuerzas, momentos, n[0], n[1], n[2]))


        elif entrada == "9":
            imprimir_datos(viga,fuerzas)
        elif entrada == "0":
            exit()
        else:
            print("input invalido")
            print("--------------")

def imprimir_datos(viga, fuerzas):
    print("Datos de la viga")
    print(viga)
    print("Datos de las fuerzas")
    for x in fuerzas:
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

def leer_elementos():
    elementos = []
    with open ("elementos.csv","r") as file:
        file.readline()
        for line in file:
            line=line.strip("\n").split(";") #Creamos una lista
            elementos.append({"tipo":line[0],
                             "posicion":[int(line[1]),int(line[2]),int(line[3])],
                             "vector":[int(line[4]),int(line[5]),int(line[6])]})
    return elementos





main()
