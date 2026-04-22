import tkinter as tk
from tkinter import messagebox
from main import generer_mot_de_passe

class FenetreGenerateur:
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.title("🔐 Générateur de mot de passe")
        self.fenetre.geometry("500x450")
        self.fenetre.resizable(False, False)
        self.fenetre.configure(bg="#5865F2")

        self.centrer_fenetre(500, 450)

        self.creer_widgets()

    def centrer_fenetre(self, largeur, hauteur):
        """Centre la fenêtre sur l'écran"""
        largeur_ecran = self.fenetre.winfo_screenwidth()
        hauteur_ecran = self.fenetre.winfo_screenheight()
        x = (largeur_ecran - largeur) // 2
        y = (hauteur_ecran - hauteur) // 2
        self.fenetre.geometry(f"{largeur}x{hauteur}+{x}+{y}")

    def creer_widgets(self):
        # Titre
        tk.Label(
            self.fenetre,
            text="🔐 Générateur de mot de passe",
            font=("Arial", 18, "bold"),
            bg="#5865F2",
            fg="white"
        ).pack(pady=10)
        
        tk.Label(
            self.fenetre,
            text="Longueur souhaitée du mot de passe: ",
            font=("Arial", 12),
            bg="#5865F2",
            fg="white"
        ).pack()    

        self.champ_longueur = tk.Entry(
            self.fenetre,
            font=("Arial", 12),
            bg="white",
            fg="#5865F2",
            insertbackground="white",
            relief="flat",
            bd=10,
            justify="center",
            width=10
        )
        self.champ_longueur.pack(pady=(10, 0), ipady=5)

        self.label_erreur = tk.Label(
            self.fenetre,
            text="",
            font=("Arial", 9, "italic"),
            bg="#5865F2",
            fg="#FF4757"
        )
        self.label_erreur.pack(pady=(0, 10))

        self.champ_longueur.bind("<Return>", lambda e: self.generer())

        # Bouton pour générer
        self.bouton_generer = tk.Button(
            self.fenetre,
            text="Générer le mot de passe",
            command=self.generer,
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            relief="raised",
            bd=5,
            cursor="hand2"
        )
        self.bouton_generer.pack(pady=10, padx=20, ipady=8)

        self.bouton_generer.bind("<Enter>", lambda e: self.bouton_generer.config(bg="#45a049"))
        self.bouton_generer.bind("<Leave>", lambda e: self.bouton_generer.config(bg="#4CAF50"))

        # Zone d'affichage
        tk.Label(
            self.fenetre,
            text="Mot de passe généré :",
            font=("Arial", 12),
            bg="#5865F2",
            fg="white"
        ).pack()

        self.resultat_var = tk.StringVar()
        self.resultat_var.set("-")

        self.label_resultat = tk.Label(
            self.fenetre,
            textvariable=self.resultat_var,
            font=("Consolas", 16, "bold"),
            bg="white",
            fg="#5865F2",
            relief="sunken",
            bd=5,
            padx=10,
            pady=10,
            wraplength=400
        )
        self.label_resultat.pack(pady=10, padx=20, fill="x")

        # Bouton copier
        self.bouton_copier = tk.Button(
            self.fenetre,
            text="📋 Copier",
            command=self.copier,
            font=("Arial", 10, "bold"),
            bg="#ffffff",
            fg="#5865F2",
            relief="flat",
            bd=3
        )
        self.bouton_copier.pack(pady=5)

    def generer(self):
        """Génère le mot de passe et met à jour l'interface"""
        try:
            saisie = self.champ_longueur.get().strip()

            #Effacer le message d'erreur précédent
            self.label_erreur.config(text="")

            if not saisie:
                self.label_erreur.config(text="Veuillez entrer une longueur")
                return

            try:
                longueur = int(saisie)
            except ValueError:
                self.label_erreur.config(text="Veuillez entrer un nombre valide.")
                return

            if longueur <= 0 or longueur > 128:
                self.label_erreur.config(text="La longueur doit être comprise entre 1 et 128.")
                return

            # Appel de la fonction du fichier main.py
            mdp = generer_mot_de_passe(longueur)
            
            # Mise à jour du label
            self.resultat_var.set(mdp)

        except ValueError:
            messagebox.showerror("❌ Erreur", "Veuillez entrer un nombre valide.")
            self.resultat_var.set("Erreur")

    def copier(self):
        """Copie le mot de passe dans le presse-papiers"""
        mdp = self.resultat_var.get()
        if mdp != "-" and mdp != "Erreur":
            self.fenetre.clipboard_clear()
            self.fenetre.clipboard_append(mdp)
            
            # Petit effet visuel pour montrer que c'est copié
            texte_original = self.bouton_copier.cget("text")
            self.bouton_copier.config(text="✅ Copié !")
            self.fenetre.after(2000, lambda: self.bouton_copier.config(text=texte_original))
        else:
            messagebox.showwarning("📋 Information", "Aucun mot de passe à copier.")

    def lancer(self):
        """Lance la boucle principale de l'application"""
        self.fenetre.mainloop()

if __name__ == "__main__":
    app = FenetreGenerateur()
    app.lancer()