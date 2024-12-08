import os , sys, random
from tqdm import tqdm
# Ajouter le dossier racine (project/) au chemin d'import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from core.utils_core import update_value_by_path, parse_string
from core.dataset_factory import  generate_nested_object
from utils.extract import append_batch_to_json_file

from business_rules.engine import run_all
from business_rules.variables import BaseVariables
from business_rules.actions import BaseActions, rule_action
from business_rules.fields import FIELD_NUMERIC, FIELD_TEXT, FIELD_NO_INPUT


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


    @rule_action(params={'field_name': FIELD_TEXT, 'value': FIELD_TEXT, 'random_anomalie_number': FIELD_NUMERIC, 'avoid_field': FIELD_TEXT})
    def setNull(self, field_name, value,avoid_field, random_anomalie_number=1):
        value =  parse_string(value)

        if field_name == "all":
            array_of_field_name_copy = self.array_of_field_name.copy()
            i = 0
            while i < random_anomalie_number:
                random_index = random.randint(0, len(array_of_field_name_copy) - 1)
                if array_of_field_name_copy[random_index] not in avoid_field:
                    is_error = update_value_by_path(self.data, self.path_config[random_index], value)
                    #array_of_field_name_copy.pop(random_index)
                  
                    if is_error == False: #garder le même nombre d'anomalies
                        i += 1
           
        elif  isinstance(field_name, list): #on passe une liste de champs
            field_name = [val for val in field_name if val not in avoid_field]
            field_name = random.sample(field_name, random_anomalie_number)
            for field in field_name:
                update_value_by_path(self.data, self.path_config[self.array_of_field_name.index(field)], value)
        else:
            update_value_by_path(self.data, self.path_config[self.array_of_field_name.index(field_name)], value)
       
       
        
        

    @rule_action(params={'rabais': FIELD_NUMERIC})
    def appliquer_rabais(self, rabais):
        print("rabais")
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
