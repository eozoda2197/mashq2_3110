class Kitob:
    def __init__(self, nom, muallif):
        self.nom = nom
        self.muallif = muallif


class Kutubxona:
    def __init__(self):
        self.kitoblar = []

    def kitob_qosh(self, kitob):
        self.kitoblar.append(kitob)

    def muallif_kitoblari(self, muallif):
        return [k for k in self.kitoblar if k.muallif == muallif]
