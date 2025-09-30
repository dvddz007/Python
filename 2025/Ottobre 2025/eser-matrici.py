from random import randint

RIGHE = int(input("Inserire la lunghezza di righe della matrice: "))
COLONNE = int(input("Inserire la lunghezza di colonne della matrice: "))


def stampa_matrice(m: list[list[int]]):
    """
        Stampa una matrice.
    """
    for r in range(len(m)):
        for c in range(len(m[r])):
            print(m[r][c], end=" ")
        print()


def trova_min_max(m: list[list[int]]) -> tuple:
    """
        Trova il valore minimo e massimo in una matrice.

       Restituisce una tupla (minimo, massimo, minpos, maxpos)
       - minimo: int
       - massimo: int
       - minpos: tuple[int, int]
       - maxpos: tuple[int, int]
    """
    minimo = m[0][0]
    massimo = m[0][0]
    minpos = (0, 0)
    maxpos = (0, 0)
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] < minimo:
                minimo = m[r][c]
                minpos = (r, c)
            if m[r][c] > massimo:
                massimo = m[r][c]
                maxpos = (r, c)
    return minimo, massimo, minpos, maxpos


pari = 0
dispari = 0
n = int(input("Inserire un numero da cercare: "))
nrow = None
ncol = None
matrice = []
for r in range(RIGHE):
    lista = []
    for c in range(COLONNE):
        x = randint(1, 100)
        if x == n:
            nrow = r
            ncol = c
        if x % 2 == 0:
            pari += 1
        else:
            dispari += 1
        lista.append(x)
    matrice.append(lista)

stampa_matrice(matrice)

print()

somma = 0
for r in range(RIGHE):
    somma += matrice[r][0]
print(f"Somma prima colonna: {somma}")

somma = 0
for r in range(len(matrice)):
    somma += sum(matrice[r])

print()

minimo, massimo, minpos, maxpos = trova_min_max(matrice)

print(f"Media matrice: {somma / (RIGHE * COLONNE)}")
print(f"Il valore più piccolo è {minimo} e si trova in {minpos}")
print(f"Il valore più grande è {massimo} e si trova in {maxpos}")
print(f"Elementi pari: {pari}")
print(f"Elementi dispari: {dispari}")

if nrow is None or ncol is None:
    print(f"Il numero {n} non è presente nella matrice")
else:
    print(f"Il numero {n} si trova nella riga {nrow} e colonna {ncol}")
