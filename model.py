

def myround(x, base=5):
    return base * round(int(x) / base)

class Igralec:

    def __init__(self, ime, tocke, radlc):
        self.ime = ime #str
        self.tocke = tocke #int
        self.radlc = radlc #int
        return

    def __repr__(self):
        return "{}, {} točk, {} radlcev".format(self.ime, self.tocke, self.radlc)


    def dvojne_tocke(self):
        if int(self.radlc) < 0:
            return "Napaka! Ni mogoče imeti negativno število radlcev."
        elif int(self.radlc) == 0:
            return False
        else: 
            return True

    
    def posodobi_radlc(self):
        if int(self.radlc) < 0:
            return "Napaka! Ni mogoče imeti negativno število radlcev."
        elif int(self.radlc) == 0:
            return "Število radlcev je že 0, igralacu se točke ne podvojijo."
        else:
            self.radlc -= 1
        return 

    def dodaj_radlc(self):
        if int(self.radlc) < 0:
            return "Napaka! Ni mogoče imeti negativno število radlcev."
        else:
            self.radlc += 1
        return

    def posodobi_tocke(self, tocke, igra, napovedi, dodatki, koeficient_kontra=0):
        sprememba = 0
        if self.napovedi(napovedi) == 125:
                sprememba = 125
                if self.dvojne_tocke():
                    self.tocke += 2 * sprememba * (2 ** koeficient_kontra)
                    return
                else:
                    self.tocke += sprememba * (2 ** koeficient_kontra)
                    return
        elif self.napovedi(napovedi) == 500:
                sprememba = 500
                if self.dvojne_tocke():
                    self.tocke += 2 * sprememba * (2 ** koeficient_kontra)
                    return
                else:
                    self.tocke += sprememba * (2 ** koeficient_kontra)
                    return
        elif self.napovedi(napovedi) == -125:
                sprememba = -125
                if self.dvojne_tocke():
                    self.tocke += 2 * sprememba * (2 ** koeficient_kontra)
                    return
                else:
                    self.tocke += sprememba * (2 ** koeficient_kontra)
                    return
        elif self.napovedi(napovedi) == -500:
                sprememba = -500
                if self.dvojne_tocke():
                    self.tocke += 2 * sprememba * (2 ** koeficient_kontra)
                    return
                else:
                    self.tocke += sprememba * (2 ** koeficient_kontra)
                    return
        elif self.dodatki(dodatki) == -250:
                sprememba = -250
                if self.dvojne_tocke():
                    self.tocke += 2 * sprememba * (2 ** koeficient_kontra)
                    return
                else:
                    self.tocke += sprememba * (2 ** koeficient_kontra)
                    return
        elif self.dodatki(dodatki) == 250:
                sprememba = 250
                if self.dvojne_tocke():
                    self.tocke += 2 * sprememba * (2 ** koeficient_kontra)
                    return
                else:
                    self.tocke += sprememba * (2 ** koeficient_kontra)
                    return
        elif 'VB' in napovedi[1]:
                sprememba = -125
                if self.dvojne_tocke():
                    self.tocke += 2 * sprememba * (2 ** koeficient_kontra)
                    return
                else:
                    self.tocke += sprememba * (2 ** koeficient_kontra)
                    return
        elif 'V' in napovedi[0]:
                sprememba = 500
                if self.dvojne_tocke():
                    self.tocke += 2 * sprememba * (2 ** koeficient_kontra)
                    return
                else:
                    self.tocke += sprememba * (2 ** koeficient_kontra)
                    return
        elif 'V' in napovedi[1]:
                sprememba = -500
                if self.dvojne_tocke():
                    self.tocke += 2 * sprememba * (2 ** koeficient_kontra)
                    return
                else:
                    self.tocke += sprememba * (2 ** koeficient_kontra)
                    return
        elif 'V' in dodatki[0]:
                sprememba = 250
                if self.dvojne_tocke():
                    self.tocke += 2 * sprememba * (2 ** koeficient_kontra)
                    return
                else:
                    self.tocke += sprememba * (2 ** koeficient_kontra)
                    return
        elif self.dvojne_tocke() == True:
            if self.zmaga(tocke):
                sprememba += self.razlika_tock(tocke)
                sprememba += self.igra(igra)
                self.posodobi_radlc()
                sprememba += self.napovedi(napovedi)
                sprememba += self.dodatki(dodatki)
            else:
                sprememba += self.razlika_tock(tocke)
                sprememba -= self.igra(igra)
                sprememba += self.napovedi(napovedi)
                sprememba += self.dodatki(dodatki)
            self.tocke += 2 * sprememba * (2 ** koeficient_kontra)
        else:
            if self.zmaga(tocke):
                sprememba += self.razlika_tock(tocke)
                sprememba += self.igra(igra)
                self.posodobi_radlc()
                sprememba += self.napovedi(napovedi)
                sprememba += self.dodatki(dodatki)
            else:
                sprememba += self.razlika_tock(tocke)
                sprememba -= self.igra(igra)
                sprememba += self.napovedi(napovedi)
                sprememba += self.dodatki(dodatki)
            self.tocke += sprememba * (2 ** koeficient_kontra)

        return

    def igra(self, igra):
        sprememba = 0
        if igra == '3':
            sprememba += 10
            return sprememba
        elif igra == '2':
            sprememba += 20
            return sprememba
        elif igra == '1':
            sprememba += 30
            return sprememba
        elif igra == 'S3':
            sprememba += 40
            return sprememba
        elif igra == 'S2':
            sprememba += 50
            return sprememba
        elif igra == 'S1':
            sprememba += 60
            return sprememba
        elif igra == 'B':
            sprememba += 70
            return sprememba
        elif igra == 'SBT':
            sprememba += 80
            return sprememba
        elif igra == 'OB':
            sprememba += 90
            return sprememba
        elif igra == 'K':
            sprememba = 70
            return sprememba
        else:
            return 'Napaka, igra s kodo {} ne obstaja.'.format(igra)

    def berac(self, uspesnost,  kontra=0):
        if self.dvojne_tocke():
            if uspesnost == 1:
                self.tocke += 2 * 70 * (2 ** kontra)
                self.posodobi_radlc()
            else:
                self.tocke -= 2 * 70 * (2 ** kontra)
        else:
            if uspesnost == 1:
                self.tocke += 70 * (2 ** kontra)
            else:
                self.tocke -= 70 * (2 ** kontra)
        return

    def SBT(self, uspesnost,  kontra=0):
        if self.dvojne_tocke():
            if uspesnost == 1:
                self.tocke += 2 * 80 * (2 ** kontra)
                self.posodobi_radlc()
            else:
                self.tocke -= 2 * 80 * (2 ** kontra)
        else:
            if uspesnost == 1:
                self.tocke += 80 * (2 ** kontra)
            else:
                self.tocke -= 80 * (2 ** kontra)
        return

    def OB(self, uspesnost,  kontra=0):
        if self.dvojne_tocke():
            if uspesnost == 1:
                self.tocke += 2 * 90 * (2 ** kontra)
                self.posodobi_radlc()
            else:
                self.tocke -= 2 * 90 * (2 ** kontra)
        else:
            if uspesnost == 1:
                self.tocke += 90 * (2 ** kontra)
            else:
                self.tocke -= 90 * (2 ** kontra)
        return

    def klop(self, tocke):
        if tocke == 'Poln':
            if self.dvojne_tocke():
                self.tocke -= 2 * 70
            else:
                self.tocke -= 70
        elif int(tocke) == 0:
            if self.dvojne_tocke():
                self.tocke += 2 * 70
            else:
                self.tocke += 70
        else:
            if self.dvojne_tocke():
                self.tocke -= myround(tocke) * 2
            else:
                self.tocke -= myround(tocke)
        return


    def zmaga(self, tocke):
        if int(tocke) > 35:
            return True
        else: 
            return False

    def razlika_tock(self, tocke):
        if int(tocke) < 0:
            return 'Napaka, ni mogoče zbrati negatvno število točk.'
        elif int(tocke) > 70:
            return 'Napaka, ni možno zbrati več kot 70 točk.'
        else:
            sprememba = 0
            x = myround(tocke) - 35
            sprememba +=  x
            return sprememba

    def napovedi(self, sez):
        sprememba = 0
        if len(sez[0]) != 0: 
            for napoved in sez[0]:
                if napoved == '4K':
                    sprememba += 20           
                elif napoved == 'T':
                    sprememba += 20
                elif napoved == 'P':
                    sprememba += 50
                elif napoved == 'ZK':
                    sprememba += 20 
                elif napoved == 'V':
                    return 500
                elif napoved == 'BV':
                    return 125
        elif len(sez[1]) != 0:
            for napoved in sez[0]:
                if napoved == '4K':
                    sprememba -= 20           
                elif napoved == 'T':
                    sprememba -= 20
                elif napoved == 'P':
                    sprememba -= 50
                elif napoved == 'ZK':
                    sprememba -= 20 
                elif napoved == 'V':
                    return -500
                elif napoved == 'BV':
                    return -125
        return sprememba

    def dodatki(self, sez):
        sprememba = 0
        if len(sez[0]) != 0: 
            for napoved in sez[0]:
                if napoved == '4K':
                    sprememba += 10           
                elif napoved == 'T':
                    sprememba += 10
                elif napoved == 'P':
                    sprememba += 25
                elif napoved == 'ZK':
                    sprememba += 10 
                elif napoved == 'V':
                    return 250
        elif len(sez[1]) != 0:
            for napoved in sez:
                if napoved == '4K':
                    sprememba -= 10           
                elif napoved == 'T':
                    sprememba -= 10
                elif napoved == 'P':
                    sprememba -= 25
                elif napoved == 'ZK':
                    sprememba -= 10 
                elif napoved == 'V':
                    return -250
        return sprememba

    def mond_fang(self):
        if self.dvojne_tocke():
            self.tocke -= 40
        else:   
            self.tocke -= 20
        return


class Tockovanje:

    def __init__(self, player_1, player_2, player_3, player_4):
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_3 = player_3
        self.player_4 = player_4
        return 

    def __repr__(self):
        return "Trenutno stanje: "

def novo_tockovanje(player_1, player_2, player_3, player_4):
    #naredi novo tockovanje z igralci
    p1 = nov_igralec(player_1)
    p2 = nov_igralec(player_2)
    p3 = nov_igralec(player_3)
    p4 = nov_igralec(player_4)
    return p1, p2, p3, p4

    

        

# class Igra_v_4:
# 
#     def __init__(self, player_1, player_2, player_3, player_4)# :
#         self.player_1 = player_1
#         self.player_2 = player_2
#         self.player_3 = player_3
#         self.player_4 = player_4
#         return
# 
#     def __repr__(self):
#         return "Igra, ki jo igrajo {}, {}, {} in {}".format# (self.player_1.ime, self.player_2.ime, # self.player_3.ime, self.player_4.ime)
# 
#     
#     def dva(self, igralec, partner):
# 
#         return
#     
#     def igralec(self):
#         return
# 
# def nova_igra(ime_1, ime_2, ime_3, ime_4):
#     player_1 = novi_igralec(ime_1)
#     player_2 = novi_igralec(ime_2)
#     player_3 = novi_igralec(ime_3)
#     player_4 = novi_igralec(ime_4)
#     return Igra_v_4(player_1, player_2, player_3,player_4)
# 
# def novi_igralec(ime):
#     igralec = Igralec(ime, 0, 0)
#     return igralec
# 

def nov_igralec(ime, tocke=0, radlc=0):
    return Igralec(ime, tocke , radlc)


igralci = {'player_1': '', 'player_2': '', 'player_3' : '', 'player_4': ''}
stanje = {'igralec': '', 'igra': ''}


