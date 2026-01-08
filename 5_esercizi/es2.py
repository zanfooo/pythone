def media(lista: list) -> float:
    somma = 0
    for n in lista:
        somma += n
    return somma / len(lista)


numeri = []
for i in range(int(input("Quanti numeri vuoi inserire? "))):
    numeri.append(int(input("Numero: ")))

m = media(numeri)

sopra = 0
sotto = 0
maggiori_media = []

for n in numeri:
    # Conto e salvo solo i numeri maggiori della media
    if n > m:
        sopra += 1
        maggiori_media.append(n)
    elif n < m:
        sotto += 1

max_seq = 1
corrente = 1

# Confronto ogni numero con il precedente
for i in range(1, len(numeri)):
    if numeri[i] == numeri[i - 1]:
        corrente += 1
        if corrente > max_seq:
            max_seq = corrente
    else:
        corrente = 1

print("Media:", m)
print("Sopra media:", sopra)
print("Sotto media:", sotto)
print("Numeri > media:", maggiori_media)
print("Sequenza più lunga:", max_seq)
