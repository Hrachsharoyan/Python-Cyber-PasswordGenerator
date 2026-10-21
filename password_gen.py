import random 
import string

print("=== GÉNÉRATEUR DE MOTS DE PASSE SECURISÉS ===")

longeur_mdp = 12

tous_les_caracteres = string.ascii_letters + string.digits + string.punctuation
print(tous_les_caracteres)

liste_piochee = random.choices(tous_les_caracteres, k=longeur_mdp)

mot_de_passe = "".join(liste_piochee)
print(f"[SUCCESS] Votre mot de passe sécurisé a été généré : {mot_de_passe}")