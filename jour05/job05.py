def chiffrement_cesar(message, decalage):
    resultat = ""
    for caractere in message:
        if caractere.isalpha():  # Vérifier si le caractère est une lettre
            minuscule = caractere.islower()  # Vérifier si le caractère est minuscule
            caractere = chr((ord(caractere) - ord('a' if minuscule else 'A') + decalage) % 26 + ord('a' if minuscule else 'A'))
        resultat += caractere
    return resultat

# Exemple d'utilisation
message_original = "Jules César, général et stratège romain, a été le premier militaire officiel à chiffrer ses messages. Sa méthode était assez simple"
decalage = 3
message_chiffre = chiffrement_cesar(message_original, decalage)
print(f"Message original : {message_original}")
print(f"Message chiffré : {message_chiffre}")
