def conversor_fuerzas(fuerzas, x, y, z):
    #recibe una lista de fuerzas y retorna una tupla con
    #cargas_axiales
    #cortes
    #momentos flectores
    #torsores
    pass



def carga_axial_fuerzas(fuerzas, x, y, z):
    #retorna la carga axial de las fuerzas
    Nx = sum(map(lambda x: x[1][0], fuerzas))
    return Nx


def fuerza_cortante_y(fuerzas, x, y, z):
    fuerzas = filter(lambda i: i[0][0] < x, fuerzas)
    Vy = sum(map(lambda x: x[1][1], fuerzas))
    return Vy

def fuerza_cortante_z(fuerzas, x, y, z):
    fuerzas = filter(lambda i: i[0][0] < x, fuerzas)
    Vz = sum(map(lambda i: i[1][2], fuerzas))
    return Vz

def momento_y(fuerzas, momentos, x, y, z):
    fuerzas = filter(lambda i: i[0][0] < x, fuerzas)
    My = sum(map(lambda i: (x-i[0][0])*(i[1][2]), fuerzas))
    return My

def momento_z(fuerzas, momentos, x, y, z):
    fuerzas = filter(lambda i: i[0][0] < x, fuerzas)
    Mz = sum(map(lambda i: (x-i[0][0])*(i[1][1]), fuerzas))
    return Mz



def tension(viga, fuerzas, momentos, x, y, z):
    componente1 = carga_axial_fuerzas(fuerzas, x, y, z)/viga.At
    componente2 = momento_y(fuerzas, momentos, x, y, z)*z/viga.Iy
    componente3 = momento_z(fuerzas, momentos, x, y, z)*y/viga.Iz
    return componente1 + componente2 - componente3
