from xml.etree.ElementTree import XMLID


def initialiseer_bord():
    # bord = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    bord = []
    for rij in range(3):
        rij_inhoud = []
        for kolom in range(3):
            rij_inhoud.append(' ')
        bord.append(rij_inhoud)
    return bord

def print_bord(bord):
    print()
    for rij in bord:
        print("|".join(rij))
        print('_'*5)

def zet(bord,rij,kolom,speler):
    bord[rij][kolom] = speler
    return bord

def controleer_winnaar(bord):
    if controleer_diagonaal(bord) or controleer_verticaal(bord) or controleer_diagonaal(bord):
        return True
    return False



def controleer_horizontaal(bord):
    for rij in bord:
        if rij[0]==rij[1]==rij[2] != ' ':
            return True
        return False


def controleer_verticaal(bord):
    for kolom in range(3):
        if bord[1][kolom]==bord[0][kolom]==bord[2][kolom] != ' ':
            return True
        return False


def controleer_diagonaal(bord):
        if bord[0][0] == bord[1][1] == bord[2][2] != ' ':
            return True
        if bord[0][2] == bord[1][1] == bord[2][0] != ' ':
            return True
        return False
def controleer_input(bord,rij,kolom):
    rij_is_geldig = 0 <= rij <= 2  # Geldig rijnummer
    kolom_is_geldig = 0 <= kolom <= 2  # Geldig kolomnummer

    if rij_is_geldig and kolom_is_geldig:
        if bord[rij][kolom] == ' ':
            return True
    return False


def tic_tac_toe():
    bord= initialiseer_bord()
    huidige_speler = 'X'
    einde_spel = False
    winnaar = ''
    teller = 0
    while not einde_spel:

        if controleer_input(bord,rij,kolom):
            print_bord(bord)
            rij = int(input("kies een rij(0,1 of 2) "))
            kolom = int(input("kies een kolom(0,1 of 2) "))

            bord= zet(bord,rij,kolom,huidige_speler)
            einde_spel = controleer_winnaar(bord)
            teller += 1
            if einde_spel:
                winnaar = huidige_speler
            if huidige_speler == 'X':
                huidige_speler = 'O'
            else:
                huidige_speler = 'X'
        else:
            print('ongeldige zet ')
        if teller == 9:
            einde_spel = True

    print_bord(bord)

    if winnaar == '':
         print("Het spel eindigt in gelijkspel.")
    else:
        print(f"Speler {winnaar} heeft gewonnen!")
tic_tac_toe()









