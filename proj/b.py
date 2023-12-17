import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

# Création de la fenêtre principale
root = tk.Tk()
root.title("Calendrier et objectifs du projet")

# Fonction pour afficher le calendrier
def afficher_calendrier():
    top = tk.Toplevel(root)
    cal = Calendar(top, font="Arial 14", selectmode='day', locale='fr_FR')
    cal.pack(fill="both", expand=True)

# Création des widgets pour afficher le calendrier
calendrier_label = tk.Label(root, text="Calendrier")
calendrier_label.grid(row=0, column=0)
calendrier_button = tk.Button(root, text="Afficher calendrier", command=afficher_calendrier)
calendrier_button.grid(row=0, column=1)

# Fonction pour ajouter un objectif dans la listebox
def ajouter_objectif():
    objectif = objectif_entry.get()
    date = date_entry.get()
    objectif_listbox.insert(tk.END, f"{date} - {objectif}")
    objectif_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

# Fonction pour supprimer un objectif de la listebox
def supprimer_objectif():
    selection = objectif_listbox.curselection()
    if selection:
        objectif_listbox.delete(selection)

# Création des widgets pour ajouter et supprimer des objectifs
objectifs_label = tk.Label(root, text="Objectifs")
objectifs_label.grid(row=1, column=0)
objectif_entry = tk.Entry(root)
objectif_entry.grid(row=1, column=1)
date_label = tk.Label(root, text="Date")
date_label.grid(row=2, column=0)
date_entry = tk.Entry(root)
date_entry.grid(row=2, column=1)
ajouter_objectif_button = tk.Button(root, text="Ajouter objectif", command=ajouter_objectif)
ajouter_objectif_button.grid(row=3, column=0)
supprimer_objectif_button = tk.Button(root, text="Supprimer objectif", command=supprimer_objectif)
supprimer_objectif_button.grid(row=3, column=1)

# Création de la listebox pour afficher les objectifs
objectif_listbox = tk.Listbox(root, width=100)
objectif_listbox.grid(row=4, column=0, columnspan=2)

# Ajout d'exemples d'objectifs
objectif_listbox.insert(tk.END, "2022-01-15 - Finaliser le design de l'interface utilisateur")
objectif_listbox.insert(tk.END, "2022-02-01 - Terminer la phase de développement")

# Lancement de la boucle principale
root.mainloop()
