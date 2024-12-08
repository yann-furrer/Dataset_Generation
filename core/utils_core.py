import os , sys
import random
import string
# Ajouter le dossier racine (project/) au chemin d'import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
#from utils.load import load_yaml_config, load_rules

def extract_last_types(field) -> list :
    """
    return type of object field in param
    The field param come yaml config file
    """
    types = []
    field_type = field.get('type')
    count = field.get('rules', {}).get('count', 1)

    # Déterminer le type du champ
    if not field_type:
        if 'fakerType' in field:
            field_type = 'string'
        else:
            field_type = 'string'  # Type par défaut si non spécifié

    # Inclure le type du champ actuel une seule fois
    if field_type:
        types.append(field_type)

    if field_type == 'array':
        # Récupérer les types des sous-champs
        sub_types = []
        for sub_field in field.get('fields', []):
            sub_types.extend(extract_last_types(sub_field))

        # Ajouter les sous-champs sans suffixe
        types.extend(sub_types)

        # Si un count est présent et supérieur à 1, dupliquer les sous-champs avec suffixes
        if count > 1:
            for i in range(0, count-1 ):
               
                for t in sub_types:
                    types.append(t)
    elif field_type == 'object':
        # Récupérer les types des sous-champs
        sub_types = []
        for sub_field in field.get('fields', []):
            sub_types.extend(extract_last_types(sub_field))

        # Ajouter les sous-champs sans suffixe
        types.extend(sub_types)
    return types


def get_field_types(dataset) -> list :
    """
    retourne un tableau de types des champs du dataset
    """
    all_types = []
    for field in dataset.get('fields', []):
        all_types.extend(extract_last_types(field))
    return all_types



def extract_paths(obj, current_path='', paths=None):
    """
    Extract all possible paths in a nested object
    Return: ObjectTest.test5.test8.test10
    """
   
    if paths is None:
        paths = []
    if current_path:
        paths.append(current_path)
    if isinstance(obj, dict):
        for k, v in obj.items():
            new_path = f"{current_path}.{k}" if current_path else k
            extract_paths(v, new_path, paths)
    elif isinstance(obj, list):
        for idx, item in enumerate(obj):
            new_path = f"{current_path}[{idx}]"
            extract_paths(item, new_path, paths)
    return paths



def extract_last_field_names(field ):
    
    
    """Extract field names from a config yaml file 
    the purpose to this fonction is to give correct name to the method 
    add_method_to_class"""
    field_names = []
    field_name = field.get('fieldName', '')
    field_type = field.get('type', '')
    count = field.get('rules', {}).get('count', 1)

    # Inclure le fieldName du champ actuel une seule fois
    if field_name:
        field_names.append(field_name)

    if field_type in ['array', 'object']:
        # Récupérer les noms des sous-champs
        sub_field_names = []
        for sub_field in field.get('fields', []):
            sub_field_names.extend(extract_last_field_names(sub_field))

        # Ajouter les sous-champs sans suffixe
        field_names.extend(sub_field_names)

        # Si un count est présent et supérieur à 1, dupliquer les sous-champs avec suffixes
        if count > 1:
            for i in range(0, count-1 ):
                suffix = f"_{i+1}"
                for name in sub_field_names:
                    field_names.append(name + suffix)
    return field_names



def get_last_field_names(dataset):
    all_field_names = []
    for field in dataset.get('fields', []):
        all_field_names.extend(extract_last_field_names(field))
    return all_field_names




def update_value_by_path(obj, path, value):
    """
    Met à jour la valeur dans un objet à un chemin spécifique donné sous forme de texte.

    :param obj: L'objet de base (dictionnaire ou autre).
    :param path: Chemin sous forme de texte (ex. "data.test[0].ok").
    :param value: Nouvelle valeur à assigner.
    """
    is_error = False
    current = obj
    parts = path.split('.')
    for i, part in enumerate(parts):
        if '[' in part and ']' in part:
            # Gestion des index dans le chemin (ex. test[0])
            key, index = part.split('[')
            index = int(index[:-1])  # Retirer le ']' et convertir en entier
            if i == len(parts) - 1:
                # Dernier élément, mise à jour de la valeur
                try: # le try permet de ne rien faire si la clé n'existe pas car le parent à déja été modifié
                    current[key][index] = value
                except Exception as e:
                    is_error = True    
            else:
                # Avancer dans l'objet
                try:
                    current = current[key][index]
                except Exception as e:
                    is_error = True
        else:
            # Gestion des clés simples
            if i == len(parts) - 1:
                # Dernier élément, mise à jour de la valeur
                try:
                    current[part] = value
                except Exception as e:
                    is_error = True
                #current[part] = value
            else:
                # Avancer dans l'objet
                current = current[part]
    return is_error



def generate_id(params):
    # Définir les options par défaut
    length = params.get('len', 15)
    include_letters = params.get('includeLetters', True)
    include_numbers = params.get('includeNumbers', True)
    include_special_chars = params.get('includeSpecialChars', False)
    start_by = params.get('stratBy', "")
    
    # Créer le pool de caractères
    characters = ""
    if include_letters:
        characters += string.ascii_letters  # Lettres majuscules et minuscules
    if include_numbers:
        characters += string.digits  # Chiffres
    if include_special_chars:
        characters += string.punctuation  # Caractères spéciaux
    
    # S'assurer que le pool de caractères n'est pas vide
    if not characters:
        raise ValueError("Le pool de caractères est vide. Activez au moins une option pour inclure des lettres, chiffres ou caractères spéciaux.")
    
    # Générer la chaîne aléatoire
    random_part = ''.join(random.choice(characters) for _ in range(length - len(start_by)))
    
    # Retourner l'ID complet
    return start_by + random_part




def parse_string(input_str):
    """
    Analyse une chaîne de caractères pour déterminer son type ou la retourne telle quelle si ce n'est ni un chiffre,
    ni un booléen, ni un float.

    :param input_str: La chaîne de caractères à analyser.
    :return: Un des types suivants : None, bool, float ou la chaîne d'origine.
    """
    if input_str.lower() in ['none', 'null']:  # Vérifie si la chaîne correspond à None
        return None
    elif input_str.lower() in ['true', 'false']:  # Vérifie si la chaîne correspond à un booléen
        return input_str.lower() == 'true'
    try:
        # Essaye de convertir en float
        return float(input_str)
    except ValueError:
        # Si ce n'est ni None, ni booléen, ni float, retourne la chaîne telle quelle
        return input_str