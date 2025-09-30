from random import randint

RIGHE = 5
COLONNE = 5
listaDiListe = []

minimo = 101
massimo = -1
for j in range(RIGHE):
    lista = []
    for i in range(COLONNE):
        r = randint(1, 100)
        if r < minimo:
            minimo = r
            minindex = (j, i)
        if r > massimo:
            massimo = r
            maxindex = (j, i)
        lista.append(r)
    listaDiListe.append(lista)

for j in range(len(listaDiListe)):
    for i in range(len(listaDiListe[j])):
        print(listaDiListe[j][i], end=" ")
    print(f"-> somma lista[{j}]: {sum(listaDiListe[j])}")

print()

somma = 0
for lista in listaDiListe:
    somma += sum(lista)
print(f"Somma di tutte le liste: {somma}")

print()

max_col, max_row = maxindex
min_col, min_row = minindex

print(
    f"Il numero più piccolo della matrice è: {minimo} nella colonna {min_col} e nella riga {min_row}"
    "\n"
    f"Il numero più grande della matrice è: {massimo} nella colonna {max_col} e nella riga {max_row}"
)

print()

print(
    f"Primo elemento della prima lista innestata: {listaDiListe[0][0]}"
    "\n"
    f"Ultimo elemento dell'ultima lista innestata: {listaDiListe[-1][-1]}"
)
