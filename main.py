import random
import string

def generer_mot_de_passe(longueur):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe

print("=== [GESTIONNAIRE DE MOTS DE PASSE] ===")
print("")

if __name__ == "__main__":
    try:
        while True:
            try:
                saisie = input("Entrez la longueur du mot de passe : ")
                longueur = int(saisie)
                
                if longueur <= 0:
                    print("!! Veuillez entrer un nombre supérieur à 0.")
                    continue
                if longueur > 128:
                    print("!! C'est un très long mot de passe ! Par sécurité, la limite est de 128 caractères.")
                    continue
                    
                mot_de_passe = generer_mot_de_passe(longueur)
                print("\n>> Mot de passe généré : ", mot_de_passe)
                break
                
            except ValueError:
                print(f"!! '{saisie}' n'est pas un nombre valide. Veuillez entrer un nombre.")
    except (KeyboardInterrupt, EOFError):
        print("\n\n!! Opération annulée par l'utilisateur. Au revoir !")

