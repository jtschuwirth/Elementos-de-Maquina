from math import pi

class Viga:
    def __init__(self, material, perfil, x, y ,z, r, t):
        self.material = material
        self.perfil = perfil
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.t = t

    def __str__(self):
        a = f"""
        material = {self.material["material"]}
        perfil = {self.perfil["perfil"]}
        x =  {self.x}
        y =  {self.y}
        z =  {self.z}
        r =  {self.r}
        t =  {self.t}
        """
        return a
    @property
    def K(self):
        a = self.z
        b = self.y
        x = self.x
        r = self.r
        t = self.t
        return eval(self.perfil["K"])

    @property
    def Q(self):
        a = self.z
        b = self.y
        x = self.x
        r = self.r
        t = self.t
        return eval(self.perfil["Q"])

    @property
    def At(self):
        a = self.z
        b = self.y
        x = self.x
        r = self.r
        t = self.t
        return eval(self.perfil["At"])

    @property
    def Ix(self):
        a = self.z
        b = self.y
        x = self.x
        r = self.r
        t = self.t
        return eval(self.perfil["Ix"])

    @property
    def Iy(self):
        a = self.z
        b = self.y
        x = self.x
        r = self.r
        t = self.t
        return eval(self.perfil["Iy"])

    @property
    def Iz(self):
        a = self.z
        b = self.y
        x = self.x
        r = self.r
        t = self.t
        return eval(self.perfil["Iz"])

    @property
    def J(self):
        a = self.z
        b = self.y
        x = self.x
        r = self.r
        t = self.t
        return eval(self.perfil["J"])
