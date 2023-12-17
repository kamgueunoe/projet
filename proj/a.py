import tkinter as tk
import mysql.connector

# Connexion à la base de données MySql
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="pdata"
)




# Création des tables dans la base de données
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS taches (id INT AUTO_INCREMENT PRIMARY KEY, tache VARCHAR(255), date DATE, description TEXT, utilisateur VARCHAR(255))")
cursor.execute("CREATE TABLE IF NOT EXISTS ressources (id INT AUTO_INCREMENT PRIMARY KEY, ressource VARCHAR(255), quantite INT, utilisateur VARCHAR(255))")
db.commit()



# Création de la fenêtre principale
root = tk.Tk()
root.title("Collaboration sur projet")

# Fonction pour ajouter une tâche dans la base de données
def ajouter_tache():
    tache = tache_entry.get()
    date = date_entry.get()
    description = description_entry.get()
    utilisateur = utilisateur_entry.get()
    cursor = db.cursor()
    query = "INSERT INTO taches (tache, date, description, utilisateur) VALUES (%s, %s, %s, %s)"
    values = (tache, date, description, utilisateur)
    cursor.execute(query, values)
    db.commit()
    afficher_taches()

# Fonction pour afficher les tâches dans la listebox
def afficher_taches():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM taches")
    taches = cursor.fetchall()
    tache_listbox.delete(0, tk.END)
    for tache in taches:
        tache_listbox.insert(tk.END, f"{tache[1]} - {tache[2]} - {tache[3]} - {tache[4]}")

# Création des widgets pour ajouter une tâche
tache_label = tk.Label(root, text="Tâche")
tache_label.grid(row=0, column=0)
tache_entry = tk.Entry(root)
tache_entry.grid(row=0, column=1)
date_label = tk.Label(root, text="Date")
date_label.grid(row=1, column=0)
date_entry = tk.Entry(root)
date_entry.grid(row=1, column=1)
description_label = tk.Label(root, text="Description")
description_label.grid(row=2, column=0)
description_entry = tk.Entry(root)
description_entry.grid(row=2, column=1)
utilisateur_label = tk.Label(root, text="Utilisateur")
utilisateur_label.grid(row=3, column=0)
utilisateur_entry = tk.Entry(root)
utilisateur_entry.grid(row=3, column=1)
ajouter_tache_button = tk.Button(root, text="Ajouter tâche", command=ajouter_tache)
ajouter_tache_button.grid(row=4, column=0)

# Création de la listebox pour afficher les tâches
tache_listbox = tk.Listbox(root)
tache_listbox.grid(row=5, column=0, columnspan=2)
afficher_taches()

# Fonction pour ajouter une ressource dans la base de données
def ajouter_ressource():
    ressource = ressource_entry.get()
    quantite = quantite_entry.get()
    utilisateur = utilisateur_entry.get()
    cursor = db.cursor()
    query = "INSERT INTO ressources (ressource, quantite, utilisateur) VALUES (%s, %s, %s)"
    values = (ressource, quantite, utilisateur)
    cursor.execute(query, values)
    db.commit()
    afficher_ressources()

# Fonction pour afficher les ressources dans la listebox
def afficher_ressources():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM ressources")
    ressources = cursor.fetchall()
    ressource_listbox.delete(0, tk.END)
    for ressource in ressources:
        ressource_listbox.insert(tk.END, f"{ressource[1]} - {ressource[2]} - {ressource[3]}")

# Création des widgets pour ajouter une ressource
ressource_label = tk.Label(root, text="Ressource")
ressource_label.grid(row=6, column=0)
ressource_entry = tk.Entry(root)
ressource_entry.grid(row=6, column=1)
quantite_label = tk.Label(root, text="Quantité")
quantite_label.grid(row=7, column=0)
quantite_entry = tk.Entry(root)
quantite_entry.grid(row=7, column=1)
utilisateur_label = tk.Label(root, text="Utilisateur")
utilisateur_label.grid(row=8, column=0)
utilisateur_entry = tk.Entry(root)
utilisateur_entry.grid(row=8, column=1)
ajouter_ressource_button = tk.Button(root, text="Ajouter ressource", command=ajouter_ressource)
ajouter_ressource_button.grid(row=9, column=0)

# Création de la listebox pour afficher les ressources
ressource_listbox = tk.Listbox(root)
ressource_listbox.grid(row=10, column=0, columnspan=2)
afficher_ressources()

# Lancement de la boucle principale
root.mainloop()
