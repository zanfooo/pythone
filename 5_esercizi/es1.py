def media_voti(voti: list) -> float:
    # Calcolo manuale della media con ciclo for
    somma = 0
    for v in voti:
        somma += v
    return somma / len(voti)


studenti = []

n_studenti = int(input("Quanti studenti vuoi inserire? "))

for i in range(n_studenti):
    nome = input("Nome studente: ")
    voti = []

    n_voti = int(input("Quanti voti inserire? "))
    for j in range(n_voti):
        voti.append(int(input("Voto (1-10): ")))

    # Ogni studente è un dizionario dentro la lista studenti
    studenti.append({"nome": nome, "voti": voti})

# Inizializzo max e min con il primo studente
studente_max = studenti[0]
studente_min = studenti[0]
promossi = []

for s in studenti:
    s["media"] = media_voti(s["voti"])  # salvo la media nel dizionario

    # Confronto le medie per trovare max e min
    if s["media"] > studente_max["media"]:
        studente_max = s
    if s["media"] < studente_min["media"]:
        studente_min = s

    if s["media"] >= 6:
        promossi.append(s["nome"])

print("\n--- RIEPILOGO ---")
for s in studenti:
    stato = "Promosso" if s["media"] >= 6 else "Bocciato"
    print(s["nome"], "- Media:", s["media"], "-", stato)
