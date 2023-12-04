okDiag = []
okOriz = []
okVert = []
def analizaCastig(tabel):
    # algoritm verificare diagonala
    okDiag.clear()
    for i in range(0, 3, 1):
        okDiag.append(tabel[i][i])
    if 'X' not in okDiag and '_' not in okDiag:
        print('O castiga')
        return 1
    elif 'O' not in okDiag and '_' not in okDiag:
        print('X castiga')
        return 1

    x: int
    x, y = 2, 0
    okDiag.clear()
    while (y < 3):
        okDiag.append(tabel[x][y])
        x -= 1
        y += 1
    if 'X' not in okDiag and '_' not in okDiag:
        print('O castiga')
        return 1
    elif 'O' not in okDiag and '_' not in okDiag:
        print('X castiga')
        return 1
    # final algoritm verificare diagonala

    # verificare oriz
    for i in range(0, 3, 1):
        okOriz.clear()
        for j in range(0, 3, 1):
            okOriz.append(tabel[j][i])
        if 'X' not in okOriz and '_' not in okOriz:
            print('O castiga')
            return 1
        elif 'O' not in okOriz and '_' not in okOriz:
            print('X castiga')
            return 1
    # final verificare oriz

    #verificare  vert
    for i in range(0, 3, 1):
        okVert.clear()
        for j in range(0, 3, 1):
            okVert.append(tabel[i][j])
        if 'X' not in okVert and '_' not in okVert:
            print('O castiga')
            return 1
        elif 'O' not in okVert and '_' not in okVert:
            print('X castiga')
            return 1
    # final verificare vert

    # verificare egalitate
    okEgal = []
    for i in range(0, 3, 1):
        for j in range(0, 3, 1):
            okEgal.append(tabel[i][j])
    if ('X' in okEgal and 'O' in okEgal and '_' not in okEgal):
        print("Egalitate")
        return 1

    # final verificare egalitate

def analizaInput(alegere, tabel):
    x = int(alegere[0])
    y = int(alegere[1])
    if x > 3 or y > 3 or x < 1 or y < 1 and tabel[x - 1][y - 1] == '_':
        print("Poti alege o pozitii doar intre 1 si 3")
    elif tabel[x - 1][y - 1] != '_':
        print('Alege alta casut aceea e ocupata')
    else:
        return True
