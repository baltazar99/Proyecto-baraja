from random import randint

def jugador (nombre, mano):
    print('----------')
    print(nombre)
    print('----------')
    for m in mano:
        print(m)

def Carta(a, b):
    carta = "{} de {}".format(a,b)
    return carta

def Baraja(diccionarioCartas, figuras, listaCartas, nombres, reparte):
    n_cartas = 52
    for k, v in zip(figuras, listaCartas):
        for l in listaCartas:
           diccionarioCartas.setdefault(k, []).append(l)
    for n in nombres:
        mano_del_jugador = n + 'lista_mano'
        mano_del_jugador = []
        for i in range(reparte): # tiramos cartas
            x = randint(0, 3)  # random para la figura
            y = randint(0, 12)  # random para el numero
            key = list(diccionarioCartas.keys())
            a = key[x]
            b = diccionarioCartas[figuras[x]][y]
            carta = Carta(a, b)
            if carta not in mano_del_jugador:
                mano_del_jugador.append(carta)
            else:
                n_cartas = n_cartas - i

        jugador(n, mano_del_jugador)