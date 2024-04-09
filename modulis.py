A = 70
def printA():
    print('Aš esu nauja printA() funkcija')
    print('Dar vienas pakeitimas')

class Vehicle():
    def __init__(self, P, R):
        self.P = P
        self.R = R
class Car(Vehicle):
    def __init__(self, P, R, S):
       super().__init__(P, R)
       self.S = S
    
    def GetSeats(self):
        Txt = self.P + " turi " + str(self.S) + " sedimu vietu"
        return Txt


class Bus(Vehicle):
    def __init__(self, P, R, S):
       super().__init__(P, R)
       self.S = S
    
    def GetSeats(self):
        Txt = self.P + "turi " + str(self.S) + " sedimu vietu "
        return Txt


class Train(Vehicle):
    def __init__(self, P, R, S):
       super().__init__(P, R)
       self.S = S
    
    def GetSeats(self):
        Txt = self.P + "turi " + str(self.S) + " sedimu vietu"
        return Txt

#sukurkite failus nuskaitančią klasę, ji turi būti aprašyta jūsų kuriamame modulyje;
#ta klasė turi nuskaityti pateiktą failą, ir suskaidyti stulpelius į sąrašus:
#sąrašai I, U, j, P, duomenys iš juos iš atitinkamų taip pat pavadintų stulpelių
#realizuokite tai, jog klasė rastų tokį dydį - maksimalų P, suskaičiuotų tokį dydį pce = Pmax / 1000 * 100%;
#šie dydžiai turi būti pasiekiamį arba kaip atributas, arba galite įdėti metodą jam gauti
# class FileAnalyzer():
#     def __init__(self, pav, skirtukas):
#         self.pavadinimas = pav
#         self.skirt = skirtukas
#         self.I = []
#         self.U = []
#         self.J = []
#         self.P = []
#         pass
#     def TxtReader(self):
#         fname = self.pavadinimas
#         f = open(fname, mode='r', encoding='utf-8')
#         tekstas = f.readlines()
#         print(tekstas)
#         f.close()
#         for x in tekstas[1:]:
#             self.I.append(float(x.split(self.skirt)[0]))
#             self.U.append(float(x.split(self.skirt)[1]))
#             self.J.append(float(x.split(self.skirt)[2]))
#             self.P.append(float(x.split(self.skirt)[3].replace('\n', '')))
#         print(self.I)
#         print(self.U)
#         print(self.J)
#         print(self.P)

#     def getPMax(self):
#         Pmax = max(self.P)
#         return Pmax
#     print(self.Pmax)

#     def getPCE(self):
#         Pmax = self.getPMax()
#         pce = round(Pmax/1000*100, 2)
#         return pce
#     print(self.pce)


# # z = TxtAnalyzer('data0.txt',';')
# # z.TxtReader()
# # print(z.getVidurkis())
# # print(z.getMinimali())
# # print(z.getMax())
class FileAnalyzer:
    """
    Labai kieta mano klasė
    """
    def __init__(self, fname):
        self.fname = fname        
        self.U = []
        self.I = []  
        self.j = []
        self.P = []
        self.__readText()

    def __readText(self):
        """
        Labai kietas mano funkcija  
        """
        failas = open(self.fname, 'r')
        tekstas = failas.readlines()
        failas.close()
        for eilute in tekstas[1:]:
            self.U.append(float(eilute.split(';')[0]))
            self.I.append(float(eilute.split(';')[1]))
            self.j.append(float(eilute.split(';')[2]))
            self.P.append(float(eilute.split(';')[3]))
        print(self.U)
        print(self.I)
        print(self.j)
        print(self.P)
    def Pmax(self):
        Pmax = max(self.P)
        return Pmax
    
    def PCE(self):
        Pmax = max(self.P)
        pce = Pmax / 1000 * 100
        return pce