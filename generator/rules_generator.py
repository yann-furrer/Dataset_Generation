import json

# Ce Code à pour but de créer le conditions contraires du fichier rules_amf.json pour générer des données 
# aléatoires qui ne respectent pas les règles du fichier rules_amf.json
def inverse_json_rules(input_file_path, output_file_path):
    """
    Inverse les opérateurs dans un fichier JSON de règles et enregistre le résultat dans un nouveau fichier.

    :param input_file_path: Chemin du fichier d'entrée (JSON contenant les règles).
    :param output_file_path: Chemin du fichier de sortie où enregistrer les règles inversées.
    """
    # Fonction pour inverser les opérateurs
    def invert_operator(operator):
        inversion_map = {
            "greater_than": "less_than_or_equal_to",
            "less_than": "greater_than_or_equal",
            "equal": "not_equal",
            "not_equal": "equal",
            "contains": "contains", # does_not_contain n'existe pas dans les règles initiales
            "does_not_contain": "contains",
            "is_true" : "is_false"
        }
        return inversion_map.get(operator, operator)

    # Lecture du fichier JSON d'entrée
    with open(input_file_path, "r") as input_json_file:
        input_json = json.load(input_json_file)

    # Transformation des règles
    output_json = []
    new_conditions = [{ "conditions" : { "all": []},"actions": [{"name": "nothing"}]}]
    for rule in input_json:
       
            
            for condition in rule.get("conditions", {}).get("all", []):
                new_conditions[0]["conditions"]["all"].append(   {
                    "name": condition["name"],
                    "operator": invert_operator(condition["operator"]),
                    "value": condition["value"]
                })
     
        # output_json.append({
        #     "conditions": new_conditions,
        #     "actions": rule.get("actions", [{"name" : "nothing"}]),  # Les actions restent identiques
            
        # })

    # Enregistrement du fichier JSON inversé
    with open(output_file_path, "w") as file:
        json.dump(new_conditions, file, indent=4)

    print(f"JSON inversé sauvegardé dans '{output_file_path}'")

#