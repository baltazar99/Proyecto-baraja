class Carta:

    def __init__(self,numero,figura):
        self.numero=numero
        self.figura=figura
    def __str__(self,numero,figura):
        return "[{}-{}]".format(self.numero, self.figura)


class Baraja:
    def __init__(self):
        figura=[pica="\u2660",corazon="\u2665",diamante="\u2660",trebol="\u2663" ]
        numero=["2","3","4","5","6","7","8","9","10","11","12","13","20"] 
        self.mazo=[]
        for n in nuemors:
            for f in figura:  
            carta=Carta(n,f)
            self.mazo.append(carta)
            
    def mostrar_baraja(self):
        print()
        for num, carta in enumerate(self.mazo):
            if (num-3) %4 !=0:
                print(carta, end=" ")
            else
                print(carta)
        print() 


baraja=Baraja()
baraja.mostrar_baraja()