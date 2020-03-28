from formulas import *

FORMAS_CIRCULARES=["circular solido","circular hueco"]
FORMAS_SOLIDAS=["circular solido","cuadrado solido"]


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


def main():
    #menu principal del programa
    print("Que quieres hacer:")
    print("1. Calcular nueva viga")
    print("0. cerrar programa")
    entrada=input(">")
    if entrada == "1":
        valores_viga()
    elif entrada == "0":
        exit()
    else:
        print("input invalido")
        print("--------------")
        main()

def valores_viga():
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
    if perfil["perfil"] in FORMAS_CIRCULARES:
        r=float(input("radio de la viga(mm): "))
    else:
        y=float(input("ancho de la viga(mm):"))
        z=float(input("alto de la viga(mm):"))

    if not perfil["perfil"] in FORMAS_SOLIDAS:
        t=float(input("espesor de la viga(mm):"))

    k = calculoK(perfil = perfil, x=x, y=y, z=z, r=r, t=t)
    q = calculoQ(perfil = perfil, x=x, y=y, z=z, r=r, t=t)
    at = calculoAt(perfil = perfil, x=x, y=y, z=z, r=r, t=t)
    Ix = calculoIx(perfil = perfil, x=x, y=y, z=z, r=r, t=t)
    Iy = calculoIy(perfil = perfil, x=x, y=y, z=z, r=r, t=t)
    Iz = calculoIz(perfil = perfil, x=x, y=y, z=z, r=r, t=t)
    J = calculoJ(perfil = perfil, x=x, y=y, z=z, r=r, t=t)


def valores_estado():
    #agregamos las cargas a la que se encuentra expuesta la viga
    pass




main()
