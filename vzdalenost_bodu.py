from math import cos, sin, acos, pi

class Bod:
    counter = 0
    def __init__(self, v, u):
        Bod.counter += 1
        self.__id = Bod.counter
        self.v = v
        self.u = u

    @property
    def v(self):
        return self._v
    
    @v.setter
    def v(self, v):
        self._v = v

    @property
    def u(self):
        return self._u
    
    @u.setter
    def u(self, u):
        self._u = u

    def info(self):
        print(f"\nBod {self.__id} [{self.u}; {self.v}]")

class Ortodroma:
    def __init__(self, body):
        self.body = body 
        bod1 = self.body[0]
        bod2 = self.body[1]
        self.s1 = (pi / 2) - bod1.v * pi / 180
        self.s2 = (pi / 2) - bod2.v * pi / 180
        self.d = bod2.u * pi / 180 - bod1.u * pi / 180

    def vzdalenost(self):
        self.c = acos(cos(self.s1) * cos(self.s2) + sin(self.s1) * sin(self.s2) * cos(self.d))
        self.delka = 6371.1 * self.c
        return self.delka, self.c
    
    def azimut(self):
        try: 
            self.az1 = acos((cos(self.s2) - cos(self.s1) * cos(self.c)) / (sin(self.s1) * sin(self.c))) * 180 / pi 
            self.az2 = acos((cos(self.s1) - cos(self.s2) * cos(self.c)) / (sin(self.s2) * sin(self.c))) * 180 / pi
            
            if bod1.u > bod2.u and bod1.u - bod2.u <= 180:
                self.az1 = 360 - self.az1
            elif bod1.u > bod2.u and bod1.u - bod2.u > 180:
                self.az2 = 360 - self.az2
            elif bod1.u < bod2.u and bod2.u - bod1.u <= 180:
                self.az2 = 360 - self.az2
            elif bod1.u < bod2.u and bod2.u - bod1.u > 180:
                self.az1 = 360 - self.az1

        except ValueError:
            if bod1.u == bod2.u:
                if bod1.v < bod2.v:
                    self.az1 = 0
                    self.az2 = 180
                else:
                    self.az1 = 180
                    self.az2 = 0
            elif bod1.v == bod2.v:
                if bod1.u < bod2.u:
                    self.az1 = 90
                    self.az2 = 270
                else:
                    self.az1 = 270
                    self.az2 = 90

        return self.az1, self.az2
    
    def info(self):
        print(f"\nOrtodroma: \n  Delka: {self.delka} km \n  Azimut z bodu 1: {self.az1}° \n  Azimut z bodu 2: {self.az2}°\n")

def souradnice(popis, minimum, maximum):
    while True: 
        vstup = input(popis)
        try:
            hodnota = float(vstup)
            if minimum <= hodnota <= maximum:
                return hodnota
            else:
                print(f"{hodnota} není v rozmezí ({minimum}; {maximum})!")
        except ValueError:
            if "," in vstup:
                print("Číslo pište s desetinnou tečkou místo čárky.")
            else:
                print("Zadaná hodnota není číslo.")

v1 = souradnice("Zadejte zeměpisnou šířku prvního bodu: ", -90, 90)
u1 = souradnice("Zadejte zeměpisnou délku prvního bodu: ", -180, 180)
v2 = souradnice("Zadejte zeměpisnou šířku druhého bodu: ", -90, 90)
u2 = souradnice("Zadejte zeměpisnou délku druhého bodu: ", -180, 180)

bod1 = Bod(v1, u1)
bod1.info()
bod2 = Bod(v2, u2)
bod2.info()
sezmanbodu = [bod1, bod2]

ortdr = Ortodroma(sezmanbodu)
ortdr.vzdalenost()
ortdr.azimut()
ortdr.info()