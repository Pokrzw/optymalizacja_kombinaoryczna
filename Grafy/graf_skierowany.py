class GrafSkierowany:
    def __init__(self, wierzcholki) -> None:
        self.wierzcholki = wierzcholki
        self.krawedzie = []
        self.stopnieWCH = {}
        self.stopnieWY = {}


    #1. Sprawdza czy wierzcholek znajduje sie w tablicy wierzcholki
    #2. Jezlei nie ma to appenduje do tablicy wierzcholki w
    def addWierzcholki(self, w):
        if w in self.wierzcholki:
            print("Juz istnieje taki wierzcholek")
        else:
            self.wierzcholki.append(w)

    #1. Sprawdza czy wierzcholek znajduje sie w tablicy wierzcholki
    #2. Jezeli tak, to sprawdza, czy jest w jakichs krawedziach w tablicy krawedzie, jezeli tak, to ta kkrawedz usuwa
    #3. Kopia tablicy dla stopnia wchodzacego 
    #4. Przechodzi przez slownik stopnieWCH 

    def deleteWierzcholki(self, w):

        if w not in self.wierzcholki:
            print("Nie ma takiego wierzcholka")
            return
        #usuwanie krawedzi z wierzcholkiem
        self.krawedzie = list(filter(lambda x: w not in x, self.krawedzie))
      
        stopnieWCH_copy = dict(self.stopnieWCH)
        
        del stopnieWCH_copy[w]
        for wierzcholek in self.stopnieWCH:
            #usuwanie wierzcholka jezeli jest czescia wartosci:
            if w in self.stopnieWCH[wierzcholek]:
                stopnieWCH_copy[wierzcholek].remove(w)

        self.stopnieWCH = stopnieWCH_copy
        #usuwanie stopnia wychodzacego
        stopnieWY_copy = dict(self.stopnieWY)
        
        for wierzcholek in self.stopnieWY:
        #usuwanie wierzcholka jezeli jest kluczem:    
            if wierzcholek == w:
                stopnieWY_copy.pop(w, None)
            #usuwanie jezeli jest w wierzcholku
            else:
            #usuwanie wierzcholka jezeli jest czescia wartosci:
                if w in self.stopnieWY[wierzcholek]:
                    stopnieWY_copy[wierzcholek].remove(w)

        self.stopnieWY = stopnieWY_copy
        #usuwanie z listy wierzcholkow
        self.wierzcholki.remove(w)


    def addKrawedzie(self, w1, w2):
        #kolejnosc wierzcholka ma znaczenie
        if w1 not in self.wierzcholki or w2 not in self.wierzcholki:
            print("Nie mozna stworzyc krawędzi dla nieistniejącego wierzchołka")
            return
        if (w1, w2) in self.krawedzie:
            print("Juz istnieje taka krawedz")
            return

        krawedz = (w1, w2)
        if w1 not in self.stopnieWY:
            self.stopnieWY[w1] = []
        if w2 not in self.stopnieWCH:
            self.stopnieWCH[w2] = []    
        self.stopnieWY[w1].append(w2)
        self.stopnieWCH[w2].append(w1)
        self.krawedzie.append(krawedz)

    def deleteKrawedzie(self, w1, w2):
        if w1 not in self.wierzcholki or w2 not in self.wierzcholki:
            print("Nie mozna stworzyc krawędzi dla nieistniejącego wierzchołka")
        else:
            krawedz = (w1, w2)
            if krawedz in self.krawedzie:
                self.krawedzie.remove(krawedz)
                self.stopnieWY[w1].remove(w2)
                self.stopnieWCH[w2].remove(w1)

    def stopienWychodzacy(self, w):
        if w not in self.stopienWychodzacy:
            print("Ten wierzcholek nie wchodzi do zadnego wierzcholka")
        else:
            return len(self.stopienWychodzacy[w])
    
    def stopienWchodzacy(self, w):
        if w not in self.stopienWchodzacy:
            print("Do tego wierzcholka nie laczy sie zaden inny wierzcholek")
        else:
            return len(self.stopienWchodzacy[w])
  
graf1 = GrafSkierowany(["A", "B", "C"])
print(graf1.wierzcholki)
graf1.addKrawedzie("A", "B")
graf1.addKrawedzie("C", "B")
graf1.addKrawedzie("A", "C")
graf1.addKrawedzie("C", "A")
print(graf1.krawedzie)
print("STOPNIE WCHODZACE:", graf1.stopnieWCH)
print("STOPNIE WYCHODZACE:",graf1.stopnieWY)
graf1.deleteKrawedzie("C", "A")
print("USUNIETO CA")
print(graf1.wierzcholki)
print(graf1.krawedzie)
print("STOPNIE WCHODZACE:", graf1.stopnieWCH)
print("STOPNIE WYCHODZACE:",graf1.stopnieWY)
graf1.deleteKrawedzie("A", "A")
print("USUNIETO AA")
print(graf1.wierzcholki)
print(graf1.krawedzie)
print("STOPNIE WCHODZACE:", graf1.stopnieWCH)
print("STOPNIE WYCHODZACE:",graf1.stopnieWY)
graf1.deleteKrawedzie("A", "C")
print("USUNIETO AC")
print(graf1.wierzcholki)
print(graf1.krawedzie)
print("STOPNIE WCHODZACE:", graf1.stopnieWCH)
print("STOPNIE WYCHODZACE:",graf1.stopnieWY)
graf1.deleteKrawedzie("A", "B")
print("USUNIETO AB")
print(graf1.wierzcholki)
print(graf1.krawedzie)
print("STOPNIE WCHODZACE:", graf1.stopnieWCH)
print("STOPNIE WYCHODZACE:",graf1.stopnieWY)
graf1.deleteKrawedzie("C", "B")
print("USUNIETO CB")
print(graf1.wierzcholki)
print(graf1.krawedzie)
print("STOPNIE WCHODZACE:", graf1.stopnieWCH)
print("STOPNIE WYCHODZACE:",graf1.stopnieWY)



# graf1.addKrawedzie("A", "D")