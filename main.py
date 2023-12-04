import afisare
import analiza
verifFin = 0
tabel = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]

XsauO = 'X'
print("Acesta este un joc de X si 0\nCum se joaca: vei avea de scris pozitia unde doresti sa iti pui X sau 0 folosind coordonate de tip coloana si rand")

while(True):
    afisare.tabelPrint(tabel)
    while(True):
        alegere = input(f"Alege pozitia pe care o vei juca\nMomentan joaca {XsauO}: ").split()
        x = int(alegere[0])
        y = int(alegere[1])
        if(analiza.analizaInput(alegere, tabel) == True):
            tabel[x - 1][y - 1] = XsauO
            if XsauO == 'X':
                XsauO = 'O'
            else:
                XsauO = 'X'
            break
        else:
            continue

    if (analiza.analizaCastig(tabel) == 1):
        while(True):
            afisare.tabelPrint(tabel)
            alegere2 = input('Doresti sa mai joci?\nDaca da scrie DA daca nu scrie NU')

            if alegere2 != 'DA' and alegere2 != 'da':
                exit(0)
            else:
                verifFin = 0
                tabel = [['_', '_', '_'],
                         ['_', '_', '_'],
                         ['_', '_', '_']]
                XsauO = 'X'
                break