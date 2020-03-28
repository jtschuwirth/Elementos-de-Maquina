def conversor_fuerzas(fuerzas, x, y, z):
    #recibe una lista de fuerzas y retorna una tupla con
    #cargas_axiales
    #cortes
    #momentos flectores
    #torsores
    pass



def carga_axial_fuerzas(fuerzas):
    #retorna la carga axial de las fuerzas
    Nx = sum(map(lambda x: x[1][0], fuerzas))
    return Nx


def fuerza_cortante_y(fuerzas, x):
    Vy = sum(map(lambda x: x[1][1], fuerzas))
    return Vy

def fuerza_cortante_z(fuerzas, x):
    Vz = sum(map(lambda x: x[1][2], fuerzas))
    return Vz

def momento_y(fuerzas, momentos):
    pass

def momento_z():
    pass



def tension(viga, cargas_axiales, momentos, x, y, z):
    pass
