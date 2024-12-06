import json
#Function to create dict to json file
def create_file(filename):

    path_file = "./dataset/"+filename
    """
    Crée un fichier avec le nom donné en paramètre.
    Si le fichier existe déjà, avertit l'utilisateur.

    Args:
        filename (str): Le nom du fichier à créer.

    Returns:
        str: Message indiquant le résultat de l'opération.
    """
    import os

    # Vérifier si le fichier existe déjà
    if os.path.exists(filename):
        print(f"Le fichier '{filename}' existe déjà.")
        raise FileExistsError(f"Le fichier '{filename}' existe déjà.")
    
    # Créer le fichier
    try:
        with open(path_file, 'w') as file:
            file.write("")  # Crée un fichier vide
        print(f"Le fichier '{filename}' a été créé avec succès.")
        return path_file
    except Exception as e:
        return f"Erreur lors de la création du fichier : {e}"



def create_csv_file_from_dict(data, file_path):
    import csv
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data.keys())
        writer.writerows(zip(*data.values()))
    return file_path

def append_batch_to_json_file(file_path, batch_data):
    """
    Ajoute un batch de dictionnaires (liste de dict) à la fin d'un fichier JSON contenant une liste,
    sans charger tout le fichier en mémoire.

    :param file_path: Chemin vers le fichier JSON
    :param batch_data: Liste de dictionnaires à ajouter
    """
    if not isinstance(batch_data, list):
        raise ValueError("Le batch_data doit être une liste de dictionnaires.")

    # Convertir le batch en JSON
    json_batch = ",\n".join(json.dumps(obj) for obj in batch_data)

    try:
        with open(file_path, "r+") as f:
            f.seek(0, 2)  # Aller à la fin du fichier
            taille_fichier = f.tell()

            if taille_fichier > 2:  # Si le fichier n'est pas vide (contient une liste JSON)
                f.seek(taille_fichier - 1)  # Reculer pour remplacer le dernier ']'
                f.write(",\n" + json_batch + "\n]")  # Ajouter le batch à la liste existante
            else:
                # Si le fichier est vide ou très petit (ex. "[]"), réinitialiser une liste
                f.write("[\n" + json_batch + "\n]")
    except FileNotFoundError:
        # Si le fichier n'existe pas, le créer
        with open(file_path, "w") as f:
            f.write("[\n" + json_batch + "\n]")

    # print(f"{len(batch_data)} éléments ajoutés avec succès.")