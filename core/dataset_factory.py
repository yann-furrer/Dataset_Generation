import random
from faker import Faker
import sys, os
from datetime import datetime
# Ajouter le dossier racine (project/) au chemin d'import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from utils.load import load_yaml_config

from utils.load import load_yaml_config

fake = Faker()
config_data = load_yaml_config()


def generate_fake_data(field_name, field_type, faker_method_name, rules) -> tuple:
    """
    Generate fake data for a given field based on the field type and rules
    """
   
    if faker_method_name:
        faker_method = getattr(fake, faker_method_name.split('.')[-1], None)
        if faker_method:
                # Vérifier le type de rules
            if isinstance(rules, set) and rules == {None}:
                # Si c'est un ensemble contenant seulement None, ignorer les paramètres
                valid_params = {}
            elif isinstance(rules, dict):
                # Filtrer les règles pour ignorer les clés ou valeurs invalides
                valid_params = {k: v for k, v in rules.items() if k is not None and v is not None}
            else:
                raise TypeError("rules doit être un dictionnaire ou {None}.")

        # Appeler la méthode Faker avec des paramètres (si valides)
            try:
                return field_name, faker_method(**valid_params)
            except TypeError as e:
                print(f"Erreur lors de l'appel à la méthode Faker : {e}")
    
    if field_type == 'string':
        allowed_values = rules.get('allowedValues', [])
        if allowed_values:
            return field_name, random.choice(allowed_values)
    
    elif field_type == 'integer':
        allowed_values = rules.get('allowedValues', [])
        if allowed_values:
            return field_name, random.choice(allowed_values)
        min_value = rules.get('range', {}).get('min', 0)
        max_value = rules.get('range', {}).get('max', 100)
        return field_name, random.randint(min_value, max_value)
    
    elif field_type == 'date':

        random_date = None
        start_date = datetime.strptime(rules['range']['start'], "%Y-%m-%d")
        end_date = datetime.strptime(rules['range']['end'], "%Y-%m-%d")
        if 'unix' in rules.get('range', {}).get('format', "null"):
            random_date = random.randint(int(start_date.timestamp()), int(end_date.timestamp()))
        else:
            random_date = fake.date_between(start_date=start_date, end_date=end_date)
            random_date = random_date.strftime(rules.get('format', "%Y-%m-%d"))
        return field_name, random_date
    
    elif field_type == 'boolean':
        probability = rules.get('probability', 0.5)
        return field_name, random.random() < probability
    
    elif field_type == 'array':
        # Placeholder for array type fields
        pass
    
    elif field_type == 'object':
        # Placeholder for object type fields
        pass
    
    return field_name, None


def generate_nested_object(yaml_config) -> dict:
    """
    Generate an object strcture based on the yaml config file
    """
  

    dataset = {}
    
    for field in yaml_config['fields']:
        
        field_name = field['fieldName']
        field_types = field.get('type')
        faker_type = field.get('fakerType')
        rules = field.get('rules', {})
        
        # Recursively generate objects for nested fields
        if field_types == 'object' and 'fields' in field:
            dataset[field_name] = generate_nested_object(field)
        
        # Handle array type fields
        elif field_types == 'array':
            
            
            dataset[field_name] = []
            # Put to extract object in array
            for i in range(rules.get('count', 0)):
                for field_ in field["fields"]:
                    faker_type_ = field_.get('fakerType', None)
                    rules_ = field_.get('rules', {None})
                    field_types_ = field_.get('type')
                    field_name_ = field_.get('fieldName')

                    if field_.get('type', None) == 'object':
                        dataset[field_name].append(generate_nested_object(field_))
                    else:
                        _, value = generate_fake_data(field_name_, field_types_, faker_type_ , rules_)
                        dataset[field_name].append(value)

                    
        
        # Handle other types of fields (Normal case)
        else:
            _, value = generate_fake_data(field_name, field_types, faker_type, rules)
            dataset[field_name] = value 
    return dataset





# Cette fonction génère un ensemble de données en fonction des règles et des occurrences définies
def generate_dataset(config_data):
    dataset = []
    #print(config_data['numberOfRecords'])
    for _ in range(config_data['numberOfRecords']):
        dataset.append(generate_nested_object(config_data))
    return dataset
