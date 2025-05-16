'''
Esercizio 12: Trova l'indice del massimo

Data una lista di numeri interi, trova l'indice della prima occorrenza del valore massimo, senza usare il metodo index().

numeri = [3, 7, 2, 9, 5, 9]
# Risultato atteso: 3 # (prima volta che compare 9)
'''

numeri = [3, 7, 2, 9, 5, 9]

massimo = numeri[0]
for i in range(len(numeri)):
    if massimo < numeri[i]:
        massimo = numeri[i]
        maxindex = i

print(maxindex)
