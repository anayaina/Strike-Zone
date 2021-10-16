
from random import randint
import cv2
import enum

class Graficas(enum.Enum):
    cv2 = 0

class Tipo(enum.Enum):
    Sin_lanzar = 0
    Bola = 1
    Strike = 2
    Golpe = 3

class Punto:
    x = None
    y = None

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Pelota:
    diametro = None
    color = None
    tipo = None
    x = None
    y = None

    def __init__(self, x, y) -> None:
        self.diametro = 20
        self.x = x
        self.y = y
        self.tipo = Tipo.Sin_lanzar

def dibujar_imagen(image, grafica, bola: Pelota):
    window_name = 'Strikezone Image'
    centro = (bola.x, bola.y)
    radio = 20
    color = bola.color
    grosor = -2

    image = cv2.circle(image, centro, radio, color, grosor)
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    counter = 1
    while counter <= 3:
        if counter == 1:
            a = Pelota(randint(200, 490), randint(200, 480))
        if counter == 2:
            a = Pelota(randint(100, 420), randint(100, 420))
        if counter == 3:
            a = Pelota(randint(30, 500), randint(30, 500))

        # COORDENADAS STRIKE
        SZ_ESI = Punto(314, 171)
        SZ_ESD = Punto(416, 171)
        SZ_EII = Punto(314, 360)
        SZ_EID = Punto(416, 360)
        if (a.x >= SZ_ESI.x and a.x <= SZ_EID.x):   # x's de esquinas superiores
            if(a.y >= SZ_ESI.y and a.y <= SZ_EID.y):  # y's de esquinas superiores
                a.color = (255, 120, 120)
                print("\n" + "Strike!")
                dibujar_imagen(image, GRAFICAS, a)

        # COORDENADAS BOLA
        BL_ESI = Punto(224, 167)
        BL_ESD = Punto(477, 167)
        BL_EII = Punto(213, 480)
        BL_EID = Punto(477, 480)
        if (a.x >= BL_ESI.x and a.x <= BL_EID.x):   # x's de esquinas superiores
            if(a.y >= BL_ESI.y and a.y <= BL_EID.y):  # y's de esquinas superiores
                a.color = (255, 120, 110)
                print("\n" + "Bola!")
                dibujar_imagen(image, GRAFICAS, a)

        # COORDENADAS GOLPE
        BL_ESI = Punto(30, 93)
        BL_ESD = Punto(207, 93)
        BL_EII = Punto(34, 480)
        BL_EID = Punto(198, 480)
        # El golpe esta un poco alejado del bateador por las cordenadas dadas
        # cuando la pelota cae cerca del brazo del bateador 
        if (a.x >= BL_ESI.x and a.x <= BL_EID.x):   # x's de esquinas superiores
            if(a.y >= BL_ESI.y and a.y <= BL_EID.y):  # y's de esquinas superiores
                a.color = (255, 120, 100)
                print("\n" + "Golpe!")
                dibujar_imagen(image, GRAFICAS, a)

# PATH DEL ARCHIVO
strike_zone_file = "/Users/ignacioe.anayapradas/des4/strike_zone/strike_zone.png"
GRAFICAS = Graficas.cv2  # cv2
image = cv2.imread(strike_zone_file)
main()
