FORMAS_CIRCULARES=["circular solido","circular hueco"]

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

def torsor(fuerzas, momentos, x, y, z):
    fuerzas = filter(lambda i: i[0][0] < x, fuerzas)
    fuerzas = filter(lambda i: i[1][1] != 0 and i[0][2] != 0, fuerzas)
    fuerzas = filter(lambda i: i[1][2] != 0 and i[0][1] != 0, fuerzas)
    torsor = sum(map(lambda i: (-(i[0][2])*(i[1][1])-(i[0][1])*(i[1][2])), fuerzas))

    momentos = filter(lambda i: i[0][0] < x, momentos)
    torsor = torsor + sum(map(lambda i: (i[1][0]), momentos))
    return torsor


def momento_y(fuerzas, momentos, x, y, z):
    fuerzas = filter(lambda i: i[0][0] < x, fuerzas)
    My = sum(map(lambda i: (x-i[0][0])*(i[1][2]), fuerzas))

    momentos = filter(lambda i: i[0][0] < x, momentos)
    My = My + sum(map(lambda i: (i[1][1]), momentos))
    return My

def momento_z(fuerzas, momentos, x, y, z):
    fuerzas = filter(lambda i: i[0][0] < x, fuerzas)
    Mz = sum(map(lambda i: (x-i[0][0])*(i[1][1]), fuerzas))

    momentos = filter(lambda i: i[0][0] < x, momentos)
    Mz = Mz + sum(map(lambda i: (i[1][2]), momentos))
    return Mz



def tension(viga, fuerzas, momentos, x, y, z):
    componente1 = carga_axial_fuerzas(fuerzas, x, y, z)/viga.At
    componente2 = momento_y(fuerzas, momentos, x, y, z)*z/viga.Iy
    componente3 = momento_z(fuerzas, momentos, x, y, z)*y/viga.Iz
    return componente1 + componente2 - componente3

def esfuerzo_cortante_xy(viga, fuerzas, momentos, x, y, z):
    #por ahora utilizaremos un metodo simplificado de calculo de esfuerzos cortantes

    if viga.perfil["perfil"] in FORMAS_CIRCULARES:
        componente1 = fuerza_cortante_y(fuerzas, x, y, z)/viga.At
        componente2 = -torsor(fuerzas, momentos, x, y, z)*z/viga.J

    else:
        componente1 = fuerza_cortante_y(fuerzas, x, y, z)/viga.At
        if y != 0 or z != 0:
            componente2 = -torsor(fuerzas, momentos, x, y, z)*(z/(z**2+y**2))/viga.Q
        else:
            componente2 = 0

    Tau_xy = componente1+componente2
    return Tau_xy
    # if viga.perfil not in FORMAS_CIRCULARES:
    #     y_prima = (viga.y/2 - y)/2
    #     area_prima =
    #     Qy = area_prima*y_prima
    #     b = viga.z
    #     componente1 = fuerza_cortante_y(fuerzas,x,y,z)*Qy/(viga.Iy*b)
    #     #compontente2 = -momento_x(fuerzas, momentos, x, y, z)*sin(theta)/viga.Q

def esfuerzo_cortante_xz(viga, fuerzas, momentos, x, y, z):
    #por ahora utilizaremos un metodo simple de calculo esfuerzos cortantes
    if viga.perfil["perfil"] in FORMAS_CIRCULARES:
        componente1 = fuerza_cortante_z(fuerzas, x, y, z)/viga.At
        componente2 = -torsor(fuerzas, momentos, x, y, z)*y/viga.J

    else:
        componente1 = fuerza_cortante_z(fuerzas, x, y, z)/viga.At
        if y != 0 or z != 0:
            componente2 = -torsor(fuerzas, momentos, x, y, z)*(y/(z**2+y**2))/viga.Q
        else:
            componente2 = 0

    Tau_xz = componente1+componente2
    return Tau_xz
    # if viga.perfil not in FORMAS_CIRCULARES:
    #     z_prima = (viga.z/2 - z)/2
    #     area_prima =
    #     Qz = area_prima*z_prima
    #     d = viga.y
    #     componente1 = fuerza_cortante_z(fuerzas,x,y,z)*Qz/(viga.Iz*d)
    #     #compontente2 = momento_x(fuerzas, momentos, x, y, z)*cos(theta)/viga.Q
    #     Tau_xz = componente1 + componente 2
    #         return Tau_xz




def deflexion(viga, fuerzas, momentos, torsores, x, y, z):
    pass
