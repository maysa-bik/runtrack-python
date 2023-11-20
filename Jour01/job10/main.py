montant_initial = 20000  
taux_rendement_annuel = 8
gain_annuel = (montant_initial * taux_rendement_annuel) / 100
print("Gain annuel initial :", gain_annuel, "euros")
montant_initial += 5000
taux_rendement_annuel += 2
nouveau_gain_annuel = (montant_initial * taux_rendement_annuel) / 100
print("Nouveau gain annuel :", nouveau_gain_annuel, "euros")
retrait = 0.10 * montant_initial
montant_initial -= retrait
taux_rendement_annuel -= 1
montant_final = montant_initial * (1 + taux_rendement_annuel / 100)
nouveau_gain = montant_final - montant_initial

print("montant final de l'investissement :", montant_final, "euros")
print("nouveau gain après retrait :", nouveau_gain, "euros")