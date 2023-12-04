def tabelPrint(tabel):
    print("---------")
    for i in range(0, 3, 1):
        print("|", end=" ")
        for j in range(0, 3, 1):
            print(tabel[i][j], end=" ")
        print("|")
    print("---------")
