import argparse
import tarjetas

figuras= ['Corazones','Pinos','Tréboles','Diamantes']
listaCartas = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 20)
diccionarioCartas = {}

def main(nombres, mano):
    print("Bienvenido al juego de pares y trios con baraja francesa ")
    d= tarjetas.Baraja(diccionarioCartas, figuras, listaCartas, nombres, mano)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-j", "--nombres", help="nombres", default=["Selene", "Coronavirus"])
    parser.add_argument("-m", "--mano", help="mano", default=5)
    args = parser.parse_args()
    nombres = args.nombres
    mano = args.mano
    main(nombres, mano)