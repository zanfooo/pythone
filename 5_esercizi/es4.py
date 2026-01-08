def conta_parole(parole: list) -> dict:
    contatore = {}
    for p in parole:
        # Se la parola esiste aumento il contatore, altrimenti la creo
        if p in contatore:
            contatore[p] += 1
        else:
            contatore[p] = 1
    return contatore


parole = input("Inserisci una frase: ").split()

conteggio = conta_parole(parole)

piu_lunga = parole[0]
piu_corta = parole[0]
ripetute = []

for p in parole:
    # Confronto la lunghezza delle parole
    if len(p) > len(piu_lunga):
        piu_lunga = p
    if len(p) < len(piu_corta):
        piu_corta = p

# Creo una lista con le parole che compaiono più volte
for p in conteggio:
    if conteggio[p] > 1:
        ripetute.append(p)

print("Conteggio:", conteggio)
print("Più lunga:", piu_lunga)
print("Più corta:", piu_corta)
print("Ripetute:", ripetute)
