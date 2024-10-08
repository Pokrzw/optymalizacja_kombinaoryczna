from termcolor import cprint


class GrafNieskierowany:

    def __init__(self, wierzcholki) -> None:
        self.wierzcholki = wierzcholki
        self.krawedzie = []
        self.mappings = {}
        self.stopnie = {}
    
    def addWierzcholki(self, w):
        if w in self.wierzcholki:
            print("Juz istnieje taki wierzcholek")
        else:
            self.wierzcholki.append(w)
    
    def deleteWierzcholki(self, w):
        if w not in self.wierzcholki:
            print("Nie ma takiego wierzcholka")
        else:
            for krawedz in self.krawedzie:
                if w in krawedz:
                    self.krawedzie.remove(krawedz)

            for wierzcholek in self.mappings:
                if wierzcholek==w:
                    self.mappings.pop(w, None)
                else:
                    self.mappings[wierzcholek].remove(w)

            self.wierzcholki.remove(w)

    
    def addKrawedzie(self, w1, w2):
        if w1 not in self.wierzcholki or w2 not in self.wierzcholki:
            print("Nie mozna stworzyc krawędzi dla nieistniejącego wierzchołka")
        if (w1, w2) in self.mappings or (w2, w1) in self.mappings:
            print("Już istnieje taka krawedz")
        else:
            krawedz = [w1, w2]
            if w1 not in self.mappings:
                self.mappings[w1] = []
            if w2 not in self.mappings:
                self.mappings[w2] = []
            self.mappings[w1].append(w2)
            self.mappings[w2].append(w1)
            self.krawedzie.append(krawedz)
            self.stopienWierzcholka(w1)
            self.stopienWierzcholka(w2)
    
    def usunKrawedzie(self, w1, w2):
        if(w1 not in self.wierzcholki or w2 not in self.wierzcholki):
            print("Nie mozna usunac krawędzi dla nieistniejącego wierzchołka")
        else:
            for krawedz in self.krawedzie:
                if w1 in krawedz and w2 in krawedz:
                    self.krawedzie.remove(krawedz)


            self.mappings[w1].remove(w2)
            self.mappings[w2].remove(w1)
            self.stopienWierzcholka(w1)
            self.stopienWierzcholka(w2)

    def stopienWierzcholka(self, w):
        if w not in self.wierzcholki:
            print("Nie można znaleźć stopnia dla wierzchołka, którego nie ma w grafie")
        else:
            stopien = 0
            for krawedz in self.krawedzie:
                if w in krawedz:
                    stopien += 1
            self.stopnie[w] = stopien
            return stopien
    
    def stopienWszystkichWierzcholkow(self):
        res = []
        for w in self.wierzcholki:
            res.append(self.stopienWierzcholka(w))
        return res

    def znajdzMinStopien(self):
        res = self.stopienWszystkichWierzcholkow()
        return min(res)

    def znajdzMaxStopien(self): 
        res = self.stopienWszystkichWierzcholkow()
        return max(res)
    
    def wierzParz(self):
        res = self.stopienWszystkichWierzcholkow()
        res2 = []
        for stopien in res:
            if stopien%2==0:
                res2.append(stopien)

        return res2
    
    def wierzNparz(self):
        res = self.stopienWszystkichWierzcholkow()
        res2 = []
        for stopien in res:
            if stopien%2!=0:
                res2.append(stopien)

        return res2
    

    def sortedStopnie(self):
        res = self.stopienWszystkichWierzcholkow()
        return res.sort(reverse=True)


graf1 = GrafNieskierowany(["A", "B", "C", "D"])
print(graf1.wierzcholki)
graf1.addKrawedzie("A", "B")
graf1.addKrawedzie("B", "C")
graf1.addKrawedzie("C", "D")
graf1.addKrawedzie("A", "D")


# graf1.addKrawedzie("A", "B")
print(graf1.krawedzie)
print(graf1.mappings)
print(graf1.stopnie)
graf1.usunKrawedzie("A", "B")
print(graf1.wierzcholki)
print(graf1.krawedzie)
print(graf1.mappings)
print(graf1.stopnie)
print(graf1.stopienWierzcholka("A"))
print(graf1.stopienWierzcholka("C"))
print(graf1.stopienWszystkichWierzcholkow())
print(graf1.znajdzMaxStopien())
print(graf1.znajdzMinStopien())
print(graf1.sortedStopnie())
