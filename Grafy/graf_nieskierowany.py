class GrafNieskierowany:

    def __init__(self, wierzcholki) -> None:
        self.wierzcholki = [].append(wierzcholki)
        self.krawedzie = []
        self.mappings = {}
        self.stopnie = {}
    
    def addWierzcholki(self, w):
        self.wierzcholki.append(w)
    
    def deleteWierzcholki(self, w):
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
        if(w1 not in self.wierzcholki or w2 not in self.wierzcholki):
            print("Nie mozna stworzyc krawędzi dla nieistniejącego wierzchołka")
        else:
            krawedz = [w1, w2]
            self.mappings[w1] = w2
            self.mappings[w2] = w1
            krawedz.append(krawedz)
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
        res = self.stopienWszystkichWierzcholkow
        return min(res)

    def znajdzMaxStopien(self): 
        res = self.stopienWszystkichWierzcholkow
        return max(res)
    
    def wierzParz(self):
        res = self.stopienWszystkichWierzcholkow
        res2 = []
        for stopien in res:
            if stopien%2==0:
                res2.append(stopien)

        return res2
    
    def wierzNparz(self):
        res = self.stopienWszystkichWierzcholkow
        res2 = []
        for stopien in res:
            if stopien%2!=0:
                res2.append(stopien)

        return res2
    

    def sortedStopnie(self):
        res = self.stopienWszystkichWierzcholkow
        return res.sort(reverse=True)