import bottle
import model


igralci = {'player_1': '', 'player_2': '', 'player_3' : '', 'player_4': ''}
stanje = {'igralec': '', 'igra': '', 'tocke':'', 'napovedi': '', 'dodatki':'', 'kontra': '', 'mond_fang': '', 'partner': ''}
info = {'igralec': '', 'igra': '', 'tocke':'', 'napovedi_uspesne': '', 'dodatki':'', 'kontra': '', 'mond_fang': '', 'partner': '', 'napovedi_rezane': '', 'tihe_napovedi':'', 'tihe_rezane':'', 'nasprotnik_napovedi':'', 'nasprotnik_rezane':'', 'nasprotnik_tihe':'', 'nasprotnik_tihe_rezane':'' }
klop = {'player_1': '', 'player_2': '', 'player_3' : '', 'player_4': ''}


@bottle.get('/')
def prva_stran():
    return bottle.template('zacetna_stran.tpl')

# @bottle.get('/ScoreBoard/?')
# def novo_stanje():
#     # prikaže novo stanje
#     return bottle.template('Score_Board.tpl')

@bottle.post('/ScoreBoard/')
def novi_igralci():
    igralci['player_1'] = model.Igralec(bottle.request.forms.p1, 0, 0)
    igralci['player_2'] = model.Igralec(bottle.request.forms.p2, 0, 0)
    igralci['player_3'] = model.Igralec(bottle.request.forms.p3, 0, 0)
    igralci['player_4'] = model.Igralec(bottle.request.forms.p4, 0, 0)
    bottle.redirect('/ScoreBoard/')
    return bottle.template('Score_Board.tpl', p1=igralci['player_1'].ime, p2=igralci['player_2'].ime, p3=igralci['player_3'].ime, p4=igralci['player_4'].ime)


@bottle.get('/ScoreBoard/')
def sore_board():
    return bottle.template('Score_Board.tpl', p1=igralci['player_1'].ime, p2=igralci['player_2'].ime, p3=igralci['player_3'].ime, p4=igralci['player_4'].ime, Radlc1=igralci['player_1'].radlc, Radlc2=igralci['player_2'].radlc, Radlc3=igralci['player_3'].radlc, Radlc4=igralci['player_4'].radlc, Točke1=igralci['player_1'].tocke, Točke2=igralci['player_2'].tocke, Točke3=igralci['player_3'].tocke, Točke4=igralci['player_4'].tocke)


#izbira igralca

@bottle.post('/ScoreBoard/igralec/')
def nova_runda():
    
    bottle.redirect('/ScoreBoard/igralec/')
    return None

@bottle.get('/ScoreBoard/igralec/')
def update():
    return bottle.template('igralec.tpl',  p1=igralci['player_1'].ime, p2=igralci['player_2'].ime, p3=igralci['player_3'].ime, p4=igralci['player_4'].ime, P1=igralci['player_1'], P2=igralci['player_2'], P3=igralci['player_3'], P4=igralci['player_4'])


# izbira igre


@bottle.post('/ScoreBoard/igra')
def izbira_igralca():
    if igralci['player_1'].ime == bottle.request.forms.igralec:
        stanje['igralec'] = igralci['player_1']
        info['igralec'] = igralci['player_1'].ime
    elif igralci['player_2'].ime == bottle.request.forms.igralec:
        stanje['igralec'] = igralci['player_2']
        info['igralec'] = igralci['player_2'].ime
    elif igralci['player_3'].ime == bottle.request.forms.igralec:
        stanje['igralec'] = igralci['player_3']
        info['igralec'] = igralci['player_3'].ime
    elif igralci['player_4'].ime == bottle.request.forms.igralec:
        stanje['igralec'] = igralci['player_4']
        info['igralec'] = igralci['player_4'].ime
    else:
        stanje['igralec'] = "Napaka"
        info['igralec'] = "Napaka"
        
    bottle.redirect('/ScoreBoard/igra')
    return None
@bottle.get('/ScoreBoard/igra')
def igralec123():
    return bottle.template('igra.tpl')



# vpis tock 

@bottle.post('/ScoreBoard/tocke')
def vpis_tock():
    if "Tri" == bottle.request.forms.igra:
        stanje['igra'] = "3"
        info['igra'] = "Tri"
    elif bottle.request.forms.igra == "Dva":
        stanje['igra'] = "2"
        info['igra'] = "Dva"
    elif bottle.request.forms.igra == "Ena":
        stanje['igra'] = "1"
        info['igra'] = "Ena"
    elif bottle.request.forms.igra == "Solo tri":
        stanje['igra'] = "S3"
        info['igra'] = "Solo tri"
    elif bottle.request.forms.igra == "Solo dva":
        stanje['igra'] = "S2"
        info['igra'] = "Solo dva"
    elif bottle.request.forms.igra == "Solo ena":
        stanje['igra'] = "S1"
        info['igra'] = "Solo ena"
    elif bottle.request.forms.igra == "Berač":
        stanje['igra'] = "B"
        info['igra'] = "Berač"
    elif bottle.request.forms.igra == "Solo brez talona":
        stanje['igra'] = "SBT"
        info['igra'] = "Solo brez talona"
    elif bottle.request.forms.igra == "Odprti berač":
        stanje['igra'] = "OB"
        info['igra'] = "Odprti berač"
    else:
        stanje['igra'] = "Napaka"
        info['igra'] = "Napaka"

    bottle.redirect('/ScoreBoard/tocke')
    return 

@bottle.get('/ScoreBoard/tocke')
def tocke():
    return bottle.template('tocke.tpl')

# napovedi uspešne

@bottle.post('/ScoreBoard/napovedi_uspesne')
def vpis_napovedi():
    
    stanje['tocke'] = bottle.request.forms.tocke
    info['tocke'] = bottle.request.forms.tocke
    bottle.redirect('/ScoreBoard/napovedi_uspesne')
    return 

@bottle.get('/ScoreBoard/napovedi_uspesne')
def napovedi():
    return bottle.template('napovedi_uspesne.tpl')


# napovedi neuspešne

@bottle.post('/ScoreBoard/napovedi_neuspesne')
def vpis_neuspesnih_napovedi():
    napovedi_uspesne = bottle.request.forms.getall('napoved')
    stanje['napovedi'] = []
    stanje['napovedi'].append(napovedi_uspesne)
    info['napovedi_uspesne'] = ', '.join(napovedi_uspesne)
    bottle.redirect('/ScoreBoard/napovedi_neuspesne')
    return 

@bottle.get('/ScoreBoard/napovedi_neuspesne')
def napovedi_neuspesne():
    return bottle.template('napovedi_neuspesne.tpl')




# napovedi tihe

@bottle.post('/ScoreBoard/napovedi_tihe')
def vpis_tihih_napovedi():
    napovedi_neuspesne = bottle.request.forms.getall('napoved_fail')
    stanje['napovedi'].append(napovedi_neuspesne)
    info['napovedi_rezane'] = ', '.join(bottle.request.forms.getall('napoved_fail'))
    bottle.redirect('/ScoreBoard/napovedi_tihe')
    return 

@bottle.get('/ScoreBoard/napovedi_tihe')
def napovedi_tihe():
    return bottle.template('napovedi_tihe.tpl')





# napovedi tihe neuspešne

@bottle.post('/ScoreBoard/napovedi_tihe_neuspesne')
def vpis_tihih_neuspesnih_napovedi():
    napovedi_tihe = bottle.request.forms.getall('tiha')
    stanje['dodatki'] = []
    stanje['dodatki'].append(napovedi_tihe)
    info['tihe_napovedi'] = ', '.join(bottle.request.forms.getall('tiha'))
    bottle.redirect('/ScoreBoard/napovedi_tihe_neuspesne')
    return 

@bottle.get('/ScoreBoard/napovedi_tihe_neuspesne')
def napovedi_tihe_neuspesne():
    return bottle.template('napovedi_tihe_neuspesne.tpl')




# napovedi nasprotnika

@bottle.post('/ScoreBoard/napovedi_nasprotnika')
def vpis_nasprotnikovih_napovedi():
    napovedi_tihe_neuspesne = bottle.request.forms.getall('tiha_neuspesna')
    stanje['dodatki'].append(napovedi_tihe_neuspesne)
    info['tihe_rezane'] = ', '.join(bottle.request.forms.getall('tiha_neuspesna'))
    bottle.redirect('/ScoreBoard/napovedi_nasprotnika')
    return 

@bottle.get('/ScoreBoard/napovedi_nasprotnika')
def napovedi_nasprotnika():
    return bottle.template('napovedi_nasprotnika.tpl')




# napovedi nasprotnika rezane

@bottle.post('/ScoreBoard/napovedi_nasprotnika_rezane')
def vpis_nasprotnikovih_napovedi_rezanih():
    napovedi_nasprotnik = bottle.request.forms.getall('nasprotink')
    for napoved in napovedi_nasprotnik:
        stanje['napovedi'][1].append(napoved)
    info['nasprotnik_napovedi'] = ', '.join(bottle.request.forms.getall('nasprotink')) 
    bottle.redirect('/ScoreBoard/napovedi_nasprotnika_rezane')
    return 

@bottle.get('/ScoreBoard/napovedi_nasprotnika_rezane')
def napovedi_nasprotnika_rezane():
    return bottle.template('napovedi_nasprotnika_rezane.tpl')



# napovedi nasprotnika tihe

@bottle.post('/ScoreBoard/napovedi_nasprotnika_tihi')
def vpis_nasprotnikovih_napovedi_tihih():
    nasprotnik_napovedi_rezane = bottle.request.forms.getall('nasprotnik_rezane')
    for rezana_napoved in nasprotnik_napovedi_rezane:
        stanje['napovedi'][0].append(rezana_napoved)
    info['nasprotnik_rezane'] = ', '.join(bottle.request.forms.getall('nasprotnik_rezane'))
    bottle.redirect('/ScoreBoard/napovedi_nasprotnika_tihi')
    return
    

@bottle.get('/ScoreBoard/napovedi_nasprotnika_tihi')
def napovedi_nasprotnika_tihi():
    return bottle.template('napovedi_nasprotnika_tihi.tpl')


# napovedi nasprotnika tihe rezane

@bottle.post('/ScoreBoard/napovedi_nasprotnika_tihe_rezane')
def vpis_nasprotnikovih_napovedi_tihih_rezanih():
    nasprotnik_napovedi_tihe = bottle.request.forms.getall('nasprotnik_tihe')
    for tihe in nasprotnik_napovedi_tihe:
        stanje['dodatki'][1].append(tihe)
    info['nasprotnik_tihe'] = ', '.join(nasprotnik_napovedi_tihe)
    bottle.redirect('/ScoreBoard/napovedi_nasprotnika_tihe_rezane')
    return 

@bottle.get('/ScoreBoard/napovedi_nasprotnika_tihe_rezane')
def napovedi_nasprotnika_tihe_rezane():
    return bottle.template('napovedi_nasprotnika_tihe_rezane.tpl')



# partner

@bottle.post('/ScoreBoard/partner')
def vpis_partnerja():
    nasprotnik_napovedi_tihe_rezane = bottle.request.forms.getall('nasprotnik_tihe_rezane')
    for rezane in nasprotnik_napovedi_tihe_rezane:
        stanje['dodatki'][0].append(rezane)
    info['nasprotnik_tihe_rezane'] = ', '.join(nasprotnik_napovedi_tihe_rezane)
    bottle.redirect('/ScoreBoard/partner')
    return 

@bottle.get('/ScoreBoard/partner')
def partner():
    return bottle.template('partner.tpl', p1=igralci['player_1'].ime, p2=igralci['player_2'].ime, p3=igralci['player_3'].ime, p4=igralci['player_4'].ime, P1=igralci['player_1'], P2=igralci['player_2'], P3=igralci['player_3'], P4=igralci['player_4'])




# kontre

@bottle.post('/ScoreBoard/kontre')
def vpis_kontre():
    if igralci['player_1'].ime == bottle.request.forms.partner:
        stanje['partner'] = igralci['player_1']
        info['partner'] = igralci['player_1'].ime
    elif igralci['player_2'].ime == bottle.request.forms.partner:
        stanje['partner'] = igralci['player_2']
        info['partner'] = igralci['player_2'].ime
    elif igralci['player_3'].ime == bottle.request.forms.partner:
        stanje['partner'] = igralci['player_3']
        info['partner'] = igralci['player_3'].ime
    elif igralci['player_4'].ime == bottle.request.forms.partner:
        stanje['partner'] = igralci['player_4']
        info['partner'] = igralci['player_4'].ime
    else:
        stanje['partner'] = "Napaka"
        stanje['partner'] = "Napaka"

    bottle.redirect('/ScoreBoard/kontre')
    return 

@bottle.get('/ScoreBoard/kontre')
def kontre():
    return bottle.template('kontre.tpl')



# Mond Fang

@bottle.post('/ScoreBoard/mond_fang')
def vpis_mond_fang():
    if bottle.request.forms.kontra == "Brez":
        stanje['kontra'] = 0
        info['kontra'] = "Brez"
    elif bottle.request.forms.kontra == "Kontra (2x)":
        stanje['kontra'] = 1
        info['kontra'] = "Kontra (2x)"
    elif bottle.request.forms.kontra == "Kontra kontri (4x)":
        stanje['kontra'] = 2
        info['kontra'] = "Kontra kontri (4x)"
    elif bottle.request.forms.kontra == "Kontra kontra kontri (8x)":
        stanje['kontra'] = 3
        info['kontra'] = "Kontra kontra kontri (8x)"
    elif bottle.request.forms.kontra == "Kontra kontra kontra kontri (16x)":
        stanje['kontra'] = 4
        info['kontra'] = "Kontra kontra kontra kontri (16x)"
    else:
        stanje['kontra'] = "Napaka"
        info['kontra'] = "Napaka"
    bottle.redirect('/ScoreBoard/mond_fang')
    return 

@bottle.get('/ScoreBoard/mond_fang')
def mond_fang():
    return bottle.template('mond_fang.tpl', p1=igralci['player_1'].ime, p2=igralci['player_2'].ime, p3=igralci['player_3'].ime, p4=igralci['player_4'].ime)

@bottle.post('/ScoreBoard/preverjanje')
def preverjanje():
    if bottle.request.forms.mond_fang == igralci['player_1'].ime:
        stanje['mond_fang'] = igralci['player_1']
        info['mond_fang'] = igralci['player_1'].ime
    elif bottle.request.forms.mond_fang == igralci['player_2'].ime:
        stanje['mond_fang'] = igralci['player_2']
        info['mond_fang'] = igralci['player_2'].ime
    elif bottle.request.forms.mond_fang == igralci['player_3'].ime:
        stanje['mond_fang'] = igralci['player_3']
        info['mond_fang'] = igralci['player_3'].ime
    elif bottle.request.forms.mond_fang == igralci['player_4'].ime:
        stanje['mond_fang'] = igralci['player_4']
        info['mond_fang'] = igralci['player_4'].ime
    elif bottle.request.forms.mond_fang == "Mond fang se to partijo ni zgodil" :
        stanje['mond_fang'] = ''
        info['mond_fang'] = "Mond fang se to partijo ni zgodil"
    bottle.redirect('/ScoreBoard/preverjanje')
    return

@bottle.get('/ScoreBoard/preverjanje')
def preverjanje():
    return bottle.template('preverjanje.tpl', igralec=info['igralec'], igra=info['igra'], tocke=info['tocke'], napovedi=info['napovedi_uspesne'], kontra=info['kontra'], mond_fang=info['mond_fang'], partner=info['partner'], napovedi_fail=info['napovedi_rezane'], napovedi_tihe=info['tihe_napovedi'], napovedi_tihe_rezane= info['tihe_rezane'], napovedi_nasprotnik=info['nasprotnik_napovedi'], nasprotnik_rezane=info['nasprotnik_rezane'], nasprotnik_tihe=info['nasprotnik_tihe'], napovedi_nasprotnika_tihe_rezane=info['nasprotnik_tihe_rezane'])



@bottle.post("/ScoreBoard/racunanje")
def racunanje():

    if stanje['igralec'] == igralci['player_1']:
        stanje_igralec = igralci['player_1']
    elif stanje['igralec'] == igralci['player_2']:
        stanje_igralec = igralci['player_2']
    elif stanje['igralec'] == igralci['player_3']:
        stanje_igralec = igralci['player_3']
    elif stanje['igralec'] == igralci['player_4']:
        stanje_igralec = igralci['player_4']
    
    trenutno_stanje = stanje_igralec.tocke 
    stanje_igralec.posodobi_tocke(stanje['tocke'], stanje['igra'], stanje['napovedi'], stanje['dodatki'], stanje['kontra'])

    if stanje['partner'] != stanje['igralec']: 
        if stanje['partner'] == igralci['player_1']:
            partner = igralci['player_1']
        elif stanje['partner'] == igralci['player_2']:
            partner = igralci['player_2']
        elif stanje['partner'] == igralci['player_3']:
            partner = igralci['player_3']
        elif stanje['partner'] == igralci['player_4']:
            partner = igralci['player_4']
        partner.tocke += (stanje_igralec.tocke - trenutno_stanje)


    if stanje['mond_fang'] == igralci['player_1']:
        igralci['player_1'].mond_fang
    elif stanje['mond_fang'] == igralci['player_2']:
        igralci['player_2'].mond_fang
    elif stanje['mond_fang'] == igralci['player_3']:
        igralci['player_3'].mond_fang
    elif stanje['mond_fang'] == igralci['player_4']:
        igralci['player_4'].mond_fang

    if 'V' in stanje['napovedi'][0] or 'V' in stanje['napovedi'][1] or 'V' in stanje['dodatki'][0] or 'V' in stanje['dodatki'][1] or 'BV' in stanje['napovedi'][0] or 'BV' in stanje['napovedi'][1]:
        igralci['player_1'].dodaj_radlc()
        igralci['player_2'].dodaj_radlc()
        igralci['player_3'].dodaj_radlc()
        igralci['player_4'].dodaj_radlc()
    

    bottle.redirect("/ScoreBoard/")


    return

#berac

@bottle.post('/ScoreBoard/berac')
def berac_preusmeritev():
    bottle.redirect('/ScoreBoard/berac')
    return

@bottle.get('/ScoreBoard/berac')
def berac():
    return bottle.template('berac.tpl')


@bottle.post('/ScoreBoard/kontra_berac')
def kontra_berac():
    if 'Opravil' == bottle.request.forms.opravljenost:
        stanje['partner'] = 1
        info['partner'] = 'Opravil'
    elif 'Padel' == bottle.request.forms.opravljenost:
        stanje['partner'] = 0
        info['partner'] = 'Padel'
    else:
        stanje['partner'] = "Napaka"
        info['partner'] = "Napaka"

    bottle.redirect('/ScoreBoard/kontra_berac')
    return

@bottle.get('/ScoreBoard/kontra_berac')
def kontra_berac_get():
    return bottle.template('kontra_berac.tpl')


@bottle.post('/ScoreBoard/preverjanje_berac')
def berac_preverjanje():
    if bottle.request.forms.kontra == "Brez":
        stanje['kontra'] = 0
        info['kontra'] = "Brez"
    elif bottle.request.forms.kontra == "Kontra (2x)":
        stanje['kontra'] = 1
        info['kontra'] = "Kontra (2x)"
    elif bottle.request.forms.kontra == "Kontra kontri (4x)":
        stanje['kontra'] = 2
        info['kontra'] = "Kontra kontri (4x)"
    elif bottle.request.forms.kontra == "Kontra kontra kontri (8x)":
        stanje['kontra'] = 3
        info['kontra'] = "Kontra kontra kontri (8x)"
    elif bottle.request.forms.kontra == "Kontra kontra kontra kontri (16x)":
        stanje['kontra'] = 4
        info['kontra'] = "Kontra kontra kontra kontri (16x)"
    else:
        stanje['kontra'] = "Napaka"
        info['kontra'] = "Napaka"
    
    
    bottle.redirect('/ScoreBoard/preverjanje_berac')
    return
 

@bottle.get('/ScoreBoard/preverjanje_berac')
def preverjanje_berac_c():
    return bottle.template('berac_preverjanje.tpl', o=info['partner'], igralec=info['igralec'], kontra=info['kontra']) 

@bottle.post("/ScoreBoard/racunanje_berac")
def racunanje_berac():
    if stanje['igralec'] == igralci['player_1']:
        stanje_igralec = igralci['player_1']
    elif stanje['igralec'] == igralci['player_2']:
        stanje_igralec = igralci['player_2']
    elif stanje['igralec'] == igralci['player_3']:
        stanje_igralec = igralci['player_3']
    elif stanje['igralec'] == igralci['player_4']:
        stanje_igralec = igralci['player_4']
    
    trenutno_stanje = stanje_igralec.tocke 
    stanje_igralec.berac(stanje['partner'], stanje['kontra'])
    igralci['player_1'].dodaj_radlc()
    igralci['player_2'].dodaj_radlc()
    igralci['player_3'].dodaj_radlc()
    igralci['player_4'].dodaj_radlc()

    bottle.redirect('/ScoreBoard/')
    return


#SBT

@bottle.post('/ScoreBoard/SBT')
def SBT_preusmeritev():
    bottle.redirect('/ScoreBoard/SBT')
    return

@bottle.get('/ScoreBoard/SBT')
def SBT():
    return bottle.template('SBT.tpl')


@bottle.post('/ScoreBoard/kontra_SBT')
def kontra_SBT():
    if 'Opravil' == bottle.request.forms.opravljenost:
        stanje['partner'] = 1
        info['partner'] = 'Opravil'
    elif 'Padel' == bottle.request.forms.opravljenost:
        stanje['partner'] = 0
        info['partner'] = 'Padel'
    else:
        stanje['partner'] = "Napaka"
        info['partner'] = "Napaka"

    bottle.redirect('/ScoreBoard/kontra_SBT')
    return

@bottle.get('/ScoreBoard/kontra_SBT')
def kontra_SBT_get():
    return bottle.template('kontra_SBT.tpl')


@bottle.post('/ScoreBoard/preverjanje_SBT')
def SBT_preverjanje():
    if bottle.request.forms.kontra == "Brez":
        stanje['kontra'] = 0
        info['kontra'] = "Brez"
    elif bottle.request.forms.kontra == "Kontra (2x)":
        stanje['kontra'] = 1
        info['kontra'] = "Kontra (2x)"
    elif bottle.request.forms.kontra == "Kontra kontri (4x)":
        stanje['kontra'] = 2
        info['kontra'] = "Kontra kontri (4x)"
    elif bottle.request.forms.kontra == "Kontra kontra kontri (8x)":
        stanje['kontra'] = 3
        info['kontra'] = "Kontra kontra kontri (8x)"
    elif bottle.request.forms.kontra == "Kontra kontra kontra kontri (16x)":
        stanje['kontra'] = 4
        info['kontra'] = "Kontra kontra kontra kontri (16x)"
    else:
        stanje['kontra'] = "Napaka"
        info['kontra'] = "Napaka"
    
    
    bottle.redirect('/ScoreBoard/preverjanje_SBT')
    return
 

@bottle.get('/ScoreBoard/preverjanje_SBT')
def preverjanje_SBT_c():
    return bottle.template('SBT_preverjanje.tpl', o=info['partner'], igralec=info['igralec'], kontra=info['kontra']) 

@bottle.post("/ScoreBoard/racunanje_SBT")
def racunanje_SBT():
    if stanje['igralec'] == igralci['player_1']:
        stanje_igralec = igralci['player_1']
    elif stanje['igralec'] == igralci['player_2']:
        stanje_igralec = igralci['player_2']
    elif stanje['igralec'] == igralci['player_3']:
        stanje_igralec = igralci['player_3']
    elif stanje['igralec'] == igralci['player_4']:
        stanje_igralec = igralci['player_4']
    
    trenutno_stanje = stanje_igralec.tocke 
    stanje_igralec.SBT(stanje['partner'], stanje['kontra'])
    igralci['player_1'].dodaj_radlc()
    igralci['player_2'].dodaj_radlc()
    igralci['player_3'].dodaj_radlc()
    igralci['player_4'].dodaj_radlc()

    bottle.redirect('/ScoreBoard/')
    return

#OB

@bottle.post('/ScoreBoard/OB')
def OB_preusmeritev():
    bottle.redirect('/ScoreBoard/OB')
    return

@bottle.get('/ScoreBoard/OB')
def OB():
    return bottle.template('OB.tpl')


@bottle.post('/ScoreBoard/kontra_OB')
def kontra_OB():
    if 'Opravil' == bottle.request.forms.opravljenost:
        stanje['partner'] = 1
        info['partner'] = 'Opravil'
    elif 'Padel' == bottle.request.forms.opravljenost:
        stanje['partner'] = 0
        info['partner'] = 'Padel'
    else:
        stanje['partner'] = "Napaka"
        info['partner'] = "Napaka"

    bottle.redirect('/ScoreBoard/kontra_OB')
    return

@bottle.get('/ScoreBoard/kontra_OB')
def kontra_OB_get():
    return bottle.template('kontra_OB.tpl')


@bottle.post('/ScoreBoard/preverjanje_OB')
def OB_preverjanje():
    if bottle.request.forms.kontra == "Brez":
        stanje['kontra'] = 0
        info['kontra'] = "Brez"
    elif bottle.request.forms.kontra == "Kontra (2x)":
        stanje['kontra'] = 1
        info['kontra'] = "Kontra (2x)"
    elif bottle.request.forms.kontra == "Kontra kontri (4x)":
        stanje['kontra'] = 2
        info['kontra'] = "Kontra kontri (4x)"
    elif bottle.request.forms.kontra == "Kontra kontra kontri (8x)":
        stanje['kontra'] = 3
        info['kontra'] = "Kontra kontra kontri (8x)"
    elif bottle.request.forms.kontra == "Kontra kontra kontra kontri (16x)":
        stanje['kontra'] = 4
        info['kontra'] = "Kontra kontra kontra kontri (16x)"
    else:
        stanje['kontra'] = "Napaka"
        info['kontra'] = "Napaka"
    
    
    bottle.redirect('/ScoreBoard/preverjanje_OB')
    return
 

@bottle.get('/ScoreBoard/preverjanje_OB')
def preverjanje_OB_c():
    return bottle.template('OB_preverjanje.tpl', o=info['partner'], igralec=info['igralec'], kontra=info['kontra']) 

@bottle.post("/ScoreBoard/racunanje_OB")
def racunanje_OB():
    if stanje['igralec'] == igralci['player_1']:
        stanje_igralec = igralci['player_1']
    elif stanje['igralec'] == igralci['player_2']:
        stanje_igralec = igralci['player_2']
    elif stanje['igralec'] == igralci['player_3']:
        stanje_igralec = igralci['player_3']
    elif stanje['igralec'] == igralci['player_4']:
        stanje_igralec = igralci['player_4']
    
    trenutno_stanje = stanje_igralec.tocke 
    stanje_igralec.OB(stanje['partner'], stanje['kontra'])
    igralci['player_1'].dodaj_radlc()
    igralci['player_2'].dodaj_radlc()
    igralci['player_3'].dodaj_radlc()
    igralci['player_4'].dodaj_radlc()

    bottle.redirect('/ScoreBoard/')
    return

@bottle.post("/ScoreBoard/klop")
def klop_e():
    bottle.redirect("/ScoreBoard/klop")
    return

@bottle.get("/ScoreBoard/klop")
def klpo_klop():
    return bottle.template('klop.tpl',  p1=igralci['player_1'].ime, p2=igralci['player_2'].ime, p3=igralci['player_3'].ime, p4=igralci['player_4'].ime)


@bottle.post('/ScoreBoard/klop_preverjanje')
def klop_preverjanje():
    if igralci['player_1'].ime == bottle.request.forms.poln:
        klop['player_1'] = 'Poln'
        klop['player_2'] = 'Oproščen'
        klop['player_3'] = 'Oproščen'
        klop['player_4'] = 'Oproščen'
    elif bottle.request.forms.poln== igralci['player_2'].ime :
        klop['player_2'] = 'Poln'
        klop['player_1'] = 'Oproščen'
        klop['player_3'] = 'Oproščen'
        klop['player_4'] = 'Oproščen'
    elif bottle.request.forms.poln == igralci['player_3'].ime :
        klop['player_3'] = 'Poln'
        klop['player_2'] = 'Oproščen'
        klop['player_1'] = 'Oproščen'
        klop['player_4'] = 'Oproščen'
    elif bottle.request.forms.poln == igralci['player_4'].ime :
        klop['player_4'] = 'Poln'
        klop['player_2'] = 'Oproščen'
        klop['player_3'] = 'Oproščen'
        klop['player_1'] = 'Oproščen'
    else:    
        tocke1 = bottle.request.forms.p1
        klop['player_1'] = tocke1
        tocke2 = bottle.request.forms.p2
        klop['player_2'] = tocke2
        tocke3 = bottle.request.forms.p3
        klop['player_3'] = tocke3
        tocke4 = bottle.request.forms.p4
        klop['player_4'] = tocke4
    bottle.redirect('/ScoreBoard/klop_preverjanje')
    return


@bottle.get('/ScoreBoard/klop_preverjanje')
def klop_preverjavanje():
    return bottle.template('klop_preverjanje.tpl', p1=igralci['player_1'].ime, p2=igralci['player_2'].ime, p3=igralci['player_3'].ime, p4=igralci['player_4'].ime, tocke1=klop['player_1'], tocke2=klop['player_2'], tocke3=klop['player_3'], tocke4=klop['player_4'])

@bottle.post("/ScoreBoard/racunanje_klop")
def racunanje_klop():
    if klop['player_1'] == 'Poln':
        igralci['player_1'].klop('Poln')
        igralci['player_1'].dodaj_radlc()
        igralci['player_2'].dodaj_radlc()
        igralci['player_3'].dodaj_radlc()
        igralci['player_4'].dodaj_radlc()
    elif klop['player_2'] == 'Poln':
        igralci['player_2'].klop('Poln')
        igralci['player_1'].dodaj_radlc()
        igralci['player_2'].dodaj_radlc()
        igralci['player_3'].dodaj_radlc()
        igralci['player_4'].dodaj_radlc()    
    elif klop['player_3'] == 'Poln':
        igralci['player_3'].klop('Poln')
        igralci['player_1'].dodaj_radlc()
        igralci['player_2'].dodaj_radlc()
        igralci['player_3'].dodaj_radlc()
        igralci['player_4'].dodaj_radlc()
    elif klop['player_4'] == 'Poln':
        igralci['player_4'].klop('Poln')
        igralci['player_1'].dodaj_radlc()
        igralci['player_2'].dodaj_radlc()
        igralci['player_3'].dodaj_radlc()
        igralci['player_4'].dodaj_radlc()
    else:
        if klop['player_1'] == '0':
            igralci['player_1'].klop('0')
            if klop['player_2'] == '0':
                igralci['player_2'].klop('0')
            elif klop['player_3'] == '0':
                igralci['player_3'].klop('0')
            elif klop['player_4'] == '0':
                igralci['player_4'].klop('0')
            igralci['player_1'].dodaj_radlc()
            igralci['player_2'].dodaj_radlc()
            igralci['player_3'].dodaj_radlc()
            igralci['player_4'].dodaj_radlc()

        elif klop['player_2'] == '0':
            igralci['player_2'].klop('0')
            if klop['player_3'] == '0':
                igralci['player_3'].klop('0')
            elif klop['player_4'] == '0':
                igralci['player_4'].klop('0')
            igralci['player_1'].dodaj_radlc()
            igralci['player_2'].dodaj_radlc()
            igralci['player_3'].dodaj_radlc()
            igralci['player_4'].dodaj_radlc()
    
        elif klop['player_3'] == '0':
            igralci['player_3'].klop('0')
            if klop['player_4'] == '0':
                igralci['player_4'].klop('0')
            igralci['player_1'].dodaj_radlc()
            igralci['player_2'].dodaj_radlc()
            igralci['player_3'].dodaj_radlc()
            igralci['player_4'].dodaj_radlc()

        elif klop['player_4'] == '0':
            igralci['player_4'].klop('0')
            igralci['player_1'].dodaj_radlc()
            igralci['player_2'].dodaj_radlc()
            igralci['player_3'].dodaj_radlc()
            igralci['player_4'].dodaj_radlc()

        else:    
            igralci['player_1'].klop(klop['player_1'])
            igralci['player_2'].klop(klop['player_2'])
            igralci['player_3'].klop(klop['player_3'])
            igralci['player_4'].klop(klop['player_4'])
            igralci['player_1'].dodaj_radlc()
            igralci['player_2'].dodaj_radlc()
            igralci['player_3'].dodaj_radlc()
            igralci['player_4'].dodaj_radlc()

    bottle.redirect("/ScoreBoard/")
    return

@bottle.post("/Custom/")
def customize():
    bottle.redirect("/Custom/")
    return

@bottle.get("/Custom/")
def kustom():
    return bottle.template('custom.tpl')

@bottle.post("/ScoreBoard/custom")
def kustommm():
    igralci['player_1'] = model.Igralec(bottle.request.forms.p1, bottle.request.forms.t1, bottle.request.forms.r1)
    igralci['player_2'] = model.Igralec(bottle.request.forms.p2, bottle.request.forms.t2, bottle.request.forms.r2)
    igralci['player_3'] = model.Igralec(bottle.request.forms.p3, bottle.request.forms.t3, bottle.request.forms.r3)
    igralci['player_4'] = model.Igralec(bottle.request.forms.p4, bottle.request.forms.t4, bottle.request.forms.r4)
    bottle.redirect('/ScoreBoard/')
    
bottle.run(debug=True, reloader=True)