def saldo_finale(operazioni: list) -> float:
    saldo = 0
    for op in operazioni:
        saldo += op
    return saldo


operazioni = []
for i in range(int(input("Numero operazioni: "))):
    operazioni.append(float(input("Operazione: ")))

saldo = 0
saldo_max = 0
saldo_min = 0
depositi = 0
prelievi = 0
storico_saldi = []

for op in operazioni:
    saldo += op
    storico_saldi.append(saldo)  # salvo il saldo dopo ogni operazione

    # Traccio massimo e minimo raggiunti nel tempo
    if saldo > saldo_max:
        saldo_max = saldo
    if saldo < saldo_min:
        saldo_min = saldo

    if op > 0:
        depositi += 1
    else:
        prelievi += 1

print("\n--- CONTO ---")
print("Saldo finale:", saldo_finale(operazioni))
print("Saldo massimo:", saldo_max)
print("Saldo minimo:", saldo_min)
print("Depositi:", depositi)
print("Prelievi:", prelievi)
print("Storico saldi:", storico_saldi)
