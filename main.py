from operator import add
import random, json, os , sys
from tqdm import tqdm
# Ajouter le dossier racine (project/) au chemin d'import
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from utils.load import load_yaml_config, load_rules
from generator.rules_generator import inverse_json_rules
from core.class_extensions import add_methods_to_class
from core.dataset_factory import  generate_nested_object
from core.engine import VariablesProduit, ActionsProduit, execute_rules, generate_random_data, random_rules_execution
from core.utils_core import get_last_field_names, extract_paths, get_field_types
from utils.extract import create_file





def main():
    # Load the dataset configuration
    config :dict = load_yaml_config()
    sample_data = generate_nested_object(config)
    rules : dict  = load_rules(1)
    path_config : list = extract_paths(sample_data) # Extract the paths from the dataset configuration to array of paths
    field_name : list = get_last_field_names(config) # Extract the last field names from the dataset configuration to array of field names
    nb_iterations = config.get("numberOfRecords", 0)
    dataset_path = create_file("test123.json")
    array_of_type = get_field_types(config)
    print(f"Generating {nb_iterations} records...")
    data = []

    if nb_iterations <= 0:
        raise ValueError("Le nombre d'enregistrements 'numberOfRecords' dans le fichier config  yaml doit être supérieur à zéro.")
        
    #instanciate the class VariablesProduit and ActionsProduit for the rules engine
    data_instance = VariablesProduit
    add_methods_to_class(data_instance, field_name, path_config, array_of_type)
    action_instance= ActionsProduit
    
    print("Executing rules...")
    if not rules:
        data = generate_random_data(nb_iterations, config)
        return
    else:
        
        nb_generated, total_rules_executed = execute_rules(nb_iterations, rules, data_instance, action_instance, path_config, field_name, config, dataset_path )
        print(f"Generated {nb_generated} records.")
        if total_rules_executed < nb_iterations:
            print(f"Only {total_rules_executed} records generated out of {nb_iterations} requested.")
            inverse_json_rules("./config/rules_config.json", "./config/inverted_rules_config.json")
            inversed_rules = load_rules(2)
            nb_generated, total_rules_executed = random_rules_execution((nb_iterations - total_rules_executed), inversed_rules, data_instance, action_instance, path_config, field_name, config, dataset_path)

if __name__ == "__main__":
    main()


