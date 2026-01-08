def valore_magazzino(prodotti: list) -> float:
    totale = 0
    for p in prodotti:
        totale += p["prezzo"] * p["quantita"]
    return totale


magazzino = []
for i in range(int(input("Quanti prodotti inserire? "))):
    magazzino.append({
        "nome": input("Nome: "),
        "prezzo": float(input("Prezzo: ")),
        "quantita": int(input("Quantità: "))
    })

# Inizializzo con il primo prodotto
prodotto_max = magazzino[0]
esauriti = []

for p in magazzino:
    valore = p["prezzo"] * p["quantita"]

    # Confronto il valore totale del prodotto
    if valore > prodotto_max["prezzo"] * prodotto_max["quantita"]:
        prodotto_max = p

    if p["quantita"] == 0:
        esauriti.append(p["nome"])

print("\n--- MAGAZZINO ---")
print("Valore totale:", valore_magazzino(magazzino))
print("Prodotto più prezioso:", prodotto_max["nome"])
print("Prodotti esauriti:", esauriti)
