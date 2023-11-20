nom_produit = "Ordinateur portable"
prix_unitaire = 1000
quantite_stock = 50
print("Nom du produit",":",nom_produit)
print("Prix unitaire",":",prix_unitaire)
print("Quantité en stock",":",quantite_stock)
quantite_achetee = int(input("Entrez la quantité de produits que vous souhaitez acheter : "))
quantité_stock = quantite_stock - quantite_achetee
print("quantité en stock aprés achat:" ,quantité_stock)
prix_unitaire *= 1.10
print(f"Nom du produit : {nom_produit}")
print(f"Prix unitaire après inflation : {prix_unitaire} euros")
print(f"Quantité en stock : {quantité_stock} unités")


