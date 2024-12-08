import os , sys
from tqdm import tqdm
# Ajouter le dossier racine (project/) au chemin d'import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from core.utils_core import update_value_by_path
from core.dataset_factory import  generate_nested_object
from utils.extract import append_batch_to_json_file

from business_rules.engine import run_all
from business_rules.variables import BaseVariables
from business_rules.actions import BaseActions, rule_action
from business_rules.fields import FIELD_NUMERIC, FIELD_TEXT, FIELD_NO_INPUT


# Ajout des méthodes dynamiques à la classe VariablesProduit
#add_methods_to_class(VariablesProduit, array_of_field_name, path_config, array_of_type)

# Définition des variables pour les règles
class VariablesProduit(BaseVariables):
    def __init__(self, data):
        self.data = data
        


class ActionsProduit(BaseActions):
    def __init__(self, data, path_config, array_of_field_name):
        self.data = data
        # Ajout des variables et actions à la classe pour les utiliser dans les règles
        self.path_config = path_config
        self.array_of_field_name = array_of_field_name

    def nothing(self):
        pass

    @rule_action(params={'field_name': FIELD_TEXT})
    def setNull(self, field_name, path_config, array_of_field_name):
       # index = array_of_field_name.index(field_name)
        update_value_by_path(self.data, path_config[array_of_field_name.index(field_name)], None)

        """Met à zéro la valeur d'un champ spécifié."""
        self.data[path_config] = None

    @rule_action(params={'rabais': FIELD_NUMERIC})
    def appliquer_rabais(self, rabais):
        """Applique un rabais spécifié en pourcentage."""
        self.data["discount"] = f"Rabais de {rabais}% appliqué"


def generate_random_data(nb_iterations, yaml_config) -> dict :
   
    """Génère des données JSON aléatoires."""
    return [generate_nested_object(yaml_config) for _ in tqdm.tqdm(range(nb_iterations))]


def execute_rules(nb_iterations, rules, variable_instance, action_instance, path_config, array_of_field_name, yaml_config, file_path) -> tuple:
    """Exécute les règles pour générer des données JSON conformes."""
    result = []
    total_rules_executed = 0
    #print(rules)
    
    for rule in rules:
        occurrences = rule.get('occurrences', 1)
        count = 0
        while count < occurrences:
            data = generate_nested_object(yaml_config)

            is_correct_data = run_all(
                rule_list=[rule],
                defined_variables=variable_instance(data),
                defined_actions=action_instance(data, path_config, array_of_field_name),
                stop_on_first_trigger=False
            )
            
            if is_correct_data:
                result.append(data)
                count += 1
                total_rules_executed += 1
            # Sauvegarde des résultats par lots de 1000 pour éviter les problèmes de mémoire
            if len(result) == 5000:
                    append_batch_to_json_file(file_path, result)
                    result.clear()

    # Sauvegarde des résultats si la taille est inférieur à 1000
    if result:
        print("passe la batch")
        append_batch_to_json_file(file_path, result)
                    
    return len(result), total_rules_executed



# def rules_execution(nb_iterations, regles ):
#     """
#     Exécute les règles pour générer des données JSON conformes.
    
#     :param nb_iterations: Nombre total de lignes à générer
#     :return: Nombre de résultats générés et les résultats eux-mêmes
#     """

#     result = []
#     total_rules_executed = 0
#     #for _ in tqdm(range(nb_iterations)):
    
#     for regle in regles:
#         occurrences = regle.get('occurrences', 1)  # Nombre d'occurrences requis
#         count = 0  # Compteur des cas générés respectant la règle
#         while count < occurrences:
#         # Génération d'un objet JSON aléatoire
#             data = generate_nested_object(load_yaml_config())
#             variables = VariablesProduit(data)
#             actions = ActionsProduit(data)

#             # Exécution des règles
#             is_correct_data = run_all(
#                 rule_list=[regle],
#                 defined_variables=variables,
#                 defined_actions=actions,
#                 stop_on_first_trigger=False
#                 )
                
#             if is_correct_data:
#               #  print(is_correct_data)
#                 result.append(data)
#                 count += 1
#                 total_rules_executed += 1
#    # if nb_iterations < total_rules_executed:

#        # print("Nombre d'itérations insuffisant pour ex")
              



    # print("Résultats générés :", len(result))
    # print("Nombre total de règles exécutées :", total_rules_executed)
    # return len(result), result, total_rules_executed


def random_rules_execution(nb_iterations, rules, variable_instance, action_instance, path_config, array_of_field_name, yaml_config, file_path) -> tuple:
    """
    Exécute les règles pour générer des données JSON conformes.
    
    :param nb_iterations: Nombre total de lignes à générer
    :return: Nombre de résultats générés et les résultats eux-mêmes
    """
    result = []
    total_rules_executed = 0
    #print(rules)
    
    
    count = 0
        
    print("Aléatoire en cours d'exécution :")
    print(nb_iterations)
    with tqdm(total=nb_iterations) as pbar:
        while count < nb_iterations:
            data = generate_nested_object(yaml_config)

            is_correct_data = run_all(
                    rule_list=rules,
                    defined_variables=variable_instance(data),
                    defined_actions=action_instance(data, path_config, array_of_field_name),
                    stop_on_first_trigger=True
                )
                
            if is_correct_data:
                result.append(data)
                count += 1
                total_rules_executed += 1
                pbar.update(1)
            # Sauvegarde des résultats par lots de 1000 pour éviter les problèmes de mémoire
            if len(result) == 5000:
                    append_batch_to_json_file(file_path, result)
                    result.clear()

    # Sauvegarde des résultats si la taille est inférieur à 1000
    if result:
        print("passe la batch")
        append_batch_to_json_file(file_path, result)
                    
    return len(result), total_rules_executed

#     result = []
#     total_rules_executed = 0
#     print(nb_iterations)
#     with tqdm.tqdm(total=nb_iterations) as pbar:
#         while len(result) < nb_iterations:
#             # Génération d'un objet JSON aléatoire
#             data = generate_nested_object(load_yaml_config())
#             variables = variable_instance(data)
#             actions = action_instance(data)

#             # Exécution des règles
#             is_correct_data = run_all(
#                 rule_list=rules,
#                 defined_variables=variables,
#                 defined_actions=actions(data, path_config),
#                 stop_on_first_trigger=True
#             )
#             #print(is_correct_data)

#             if is_correct_data:
#                 result.append(data)
#                 pbar.update(1)  # Met à jour la barre de progression
            
#             total_rules_executed += 1
#    # if nb_iterations < total_rules_executed:

#     print("Nombre de passage ", total_rules_executed)
#     with open ("current/data.json", "w") as file:
#         json.dump(result, file, indent=4)
              



    print("Résultats générés :", len(result))
    print("Nombre total de règles exécutées :", total_rules_executed)
    return len(result), result, total_rules_executed