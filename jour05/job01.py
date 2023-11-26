# Demander à l'utilisateur d'entrer son prénom
prenom = input("Entrez votre prénom : ")

# Utiliser une f-string pour afficher le message de salutation
message = f"Hello {prenom} !"

# Afficher le message de salutation
print(message)

#______________ 2 manière

def dis_hello():
    prenom = input("Entrez votre prénom : ")
    print("Hello", prenom, "!")
dis_hello()    




