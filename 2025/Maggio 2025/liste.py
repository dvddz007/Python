'''
Esercizio 12: Trova l'indice del massimo

Data una lista di numeri interi, trova l'indice della prima occorrenza del valore massimo, senza usare il metodo index().

numeri = [3, 7, 2, 9, 5, 9]
# Risultato atteso: 3 # (prima volta che compare 9)

numeri = [3, 7, 2, 9, 5, 9]

massimo = numeri[0]
maxindex = 0
for i in range(len(numeri)):
    if massimo < numeri[i]:
        massimo = numeri[i]
        maxindex = i

print(maxindex)
'''

'''
Esercizio 13: Elimina tutti gli zeri consecutivi

Data una lista di numeri interi, rimuovi tutti gli zeri che compaiono consecutivamente (lasciandone solo uno al massimo).

numeri = [1, 0, 0, 2, 0, 0, 0, 3, 0, 4]
# Risultato atteso: [1, 0, 2, 0, 3, 0, 4]
'''

'''
numeri = [1, 0, 0, 2, 0, 0, 0, 3, 0, 4]

i = 0
while i < len(numeri) -1:
    if numeri[i] == 0 and numeri[i+1] == 0:
        numeri.pop(i+1)
    i += 1
print(numeri)
'''

'''
Esercizio 15: Trova l'elemento con la massima differenza dai vicini

Data una lista di numeri, trova l'elemento (non il primo né l'ultimo) che ha la maggiore differenza assoluta con la media dei due vicini.

lista = [3, 8, 10, 4, 9, 2]
# Risultato atteso: 10  # (vicini: 8 e 4, media = 6 → diff = 4)
'''

'''
def avg(n, m: int) -> float:
    return round((n + m) / 2)


lista = [3, 8, 10, 4, 9, 2]

maxdif = 0
massimo = 0

for i in range(1, len(lista)-1):
    media = avg(lista[i-1], lista[i+1])
    diff = abs(lista[i] - media)
    if diff > maxdif:
        maxdif = diff
        massimo = lista[i]

print(massimo)
'''

'''
Esercizio 14: Rimuovi elementi tra duplicati

Data una lista, rimuovi tutti gli elementi che si trovano tra la prima e l'ultima occorrenza di un valore duplicato, compresi i duplicati stessi.

lista = [1, 2, 3, 4, 2, 5, 6]
# Risultato atteso: [1, 5, 6]  # tutto da 2 a 2 incluso viene rimosso
'''

'''
lista = [1, 2, 3, 4, 2, 5, 6]

start = 0
finish = 0

for i in range(len(lista)):
    if lista.count(lista[i]) > 1:
        start = lista[i]
        startind = i
        for j in range(i+1, len(lista)):
            if start == lista[j]:
                finish = lista[j]
                finishind = j
                break
        del lista[startind:finishind+1]  # rimuovo i valori da starting a finishind escluso (+1 per rimuoverlo)
        # la DEL rimuove una porzione di valori dalla lista. a differenza della pop o la remove, non rimuove un solo valore.
        break

print(lista)
'''